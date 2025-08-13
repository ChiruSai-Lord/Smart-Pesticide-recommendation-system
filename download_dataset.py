#!/usr/bin/env python3
"""
Dataset downloader for PlantVillage dataset
Downloads and prepares the dataset for training
"""

import os
import requests
import zipfile
import tarfile
from tqdm import tqdm
import argparse
import shutil

def download_file(url, filename):
    """Download a file with progress bar"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            pbar.update(size)

def extract_archive(archive_path, extract_to):
    """Extract archive file"""
    print(f"📦 Extracting {archive_path}...")
    
    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    elif archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
        with tarfile.open(archive_path, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_to)
    else:
        print(f"❌ Unsupported archive format: {archive_path}")
        return False
    
    print(f"✅ Extraction completed to {extract_to}")
    return True

def organize_dataset(data_dir, output_dir):
    """Organize the dataset into proper structure"""
    print(f"🗂️  Organizing dataset from {data_dir} to {output_dir}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all image files and organize by class
    classes = set()
    image_files = []
    
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Extract class name from path
                path_parts = root.split(os.sep)
                if len(path_parts) > 1:
                    class_name = path_parts[-1]
                    classes.add(class_name)
                    image_files.append((os.path.join(root, file), class_name))
    
    print(f"🏷️  Found {len(classes)} classes: {sorted(classes)}")
    print(f"🖼️  Found {len(image_files)} images")
    
    # Create class directories and copy images
    for class_name in classes:
        class_dir = os.path.join(output_dir, class_name)
        os.makedirs(class_dir, exist_ok=True)
    
    # Copy images to organized structure
    for img_path, class_name in tqdm(image_files, desc="Organizing images"):
        filename = os.path.basename(img_path)
        dest_path = os.path.join(output_dir, class_name, filename)
        
        # Handle duplicate filenames
        counter = 1
        while os.path.exists(dest_path):
            name, ext = os.path.splitext(filename)
            dest_path = os.path.join(output_dir, class_name, f"{name}_{counter}{ext}")
            counter += 1
        
        shutil.copy2(img_path, dest_path)
    
    print(f"✅ Dataset organized successfully in {output_dir}")
    return len(classes), len(image_files)

def main():
    parser = argparse.ArgumentParser(description='Download and prepare PlantVillage dataset')
    parser.add_argument('--output_dir', type=str, default='./dataset', 
                       help='Output directory for the dataset')
    parser.add_argument('--download', action='store_true', 
                       help='Download the dataset (if not already present)')
    parser.add_argument('--organize', action='store_true', 
                       help='Organize the dataset into proper structure')
    parser.add_argument('--cleanup', action='store_true', 
                       help='Clean up temporary files after organization')
    
    args = parser.parse_args()
    
    print("🌱 PlantVillage Dataset Downloader")
    print("=" * 40)
    
    # Dataset URLs (you can add more sources)
    dataset_urls = {
        'plantvillage': 'https://data.mendeley.com/public-files/datasets/tywbtsjrj3/1/files/d5652a28-c1d8-4c76-8c2c-4f1f37a9b5b0/PlantVillage.zip',
        'plantvillage_alternative': 'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz'
    }
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    if args.download:
        print("📥 Downloading PlantVillage dataset...")
        
        # Download main dataset
        dataset_file = os.path.join(args.output_dir, 'PlantVillage.zip')
        if not os.path.exists(dataset_file):
            try:
                download_file(dataset_urls['plantvillage'], dataset_file)
                print(f"✅ Downloaded: {dataset_file}")
            except Exception as e:
                print(f"❌ Download failed: {e}")
                print("🔄 Trying alternative dataset...")
                
                # Try alternative dataset
                alt_file = os.path.join(args.output_dir, 'flower_photos.tgz')
                download_file(dataset_urls['plantvillage_alternative'], alt_file)
                print(f"✅ Downloaded alternative: {alt_file}")
        else:
            print(f"📁 Dataset already exists: {dataset_file}")
    
    if args.organize:
        print("🗂️  Organizing dataset...")
        
        # Find downloaded files
        downloaded_files = []
        for file in os.listdir(args.output_dir):
            if file.endswith(('.zip', '.tar.gz', '.tgz')):
                downloaded_files.append(os.path.join(args.output_dir, file))
        
        if not downloaded_files:
            print("❌ No dataset files found. Use --download first.")
            return
        
        # Extract and organize
        for archive_file in downloaded_files:
            print(f"📦 Processing {archive_file}...")
            
            # Extract to temporary directory
            temp_dir = os.path.join(args.output_dir, 'temp_extract')
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
            
            if extract_archive(archive_file, temp_dir):
                # Organize the extracted data
                organized_dir = os.path.join(args.output_dir, 'organized')
                num_classes, num_images = organize_dataset(temp_dir, organized_dir)
                
                print(f"📊 Dataset summary:")
                print(f"   - Classes: {num_classes}")
                print(f"   - Images: {num_images}")
                print(f"   - Organized in: {organized_dir}")
                
                if args.cleanup:
                    print("🧹 Cleaning up temporary files...")
                    shutil.rmtree(temp_dir)
                    os.remove(archive_file)
                    print("✅ Cleanup completed")
    
    print("\n🎯 Next steps:")
    print("1. Train the model: python app/train_model.py --data_dir ./dataset/organized")
    print("2. Use the trained model in your app")
    print("3. Enjoy better disease detection accuracy!")

if __name__ == '__main__':
    main()
