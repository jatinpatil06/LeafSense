import os
import random
import shutil

# Path to your dataset
dataset_path = "background_removed_soydata"
output_path = "oversampled_no_background_dataset"

# Create output directory
os.makedirs(output_path, exist_ok=True)

# Get class-wise image counts
class_counts = {cls: len(os.listdir(os.path.join(dataset_path, cls))) for cls in os.listdir(dataset_path)}
max_samples = max(class_counts.values())  # Find max class size

print("Original Class Counts:", class_counts)

# Oversample each class
for class_name, count in class_counts.items():
    class_path = os.path.join(dataset_path, class_name)
    output_class_path = os.path.join(output_path, class_name)
    os.makedirs(output_class_path, exist_ok=True)

    images = os.listdir(class_path)

    # Copy existing images first
    for img in images:
        shutil.copy(os.path.join(class_path, img), output_class_path)

    # Duplicate random images until class has max_samples
    while len(os.listdir(output_class_path)) < max_samples:
        img_to_copy = random.choice(images)
        new_name = f"copy_{random.randint(10000,99999)}_{img_to_copy}"  # Unique name
        shutil.copy(os.path.join(class_path, img_to_copy), os.path.join(output_class_path, new_name))

print("✅ Dataset Oversampled! New Class Counts:")
new_counts = {cls: len(os.listdir(os.path.join(output_path, cls))) for cls in os.listdir(output_path)}
print(new_counts)
