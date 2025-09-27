from pathlib import Path
from rembg import remove
from PIL import Image

# Define input and output directories
input_root = Path("resized_partial_dataset")  # Change this to your actual input directory
output_root = Path("background_removed_soydata")  # Change this to your desired output directory

# Supported image extensions
image_extensions = ["*.png", "*.jpg", "*.jpeg", "*.JPG", "*.JPEG", "*.PNG"]

# Process all images recursively
for ext in image_extensions:
    for file in input_root.rglob(ext):
        # Compute relative path from input root
        relative_path = file.relative_to(input_root)
        
        # Create corresponding output path with PNG extension
        output_path = output_root / relative_path.with_suffix(".png")

        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            # Open image using PIL
            input_image = Image.open(file).convert("RGBA")  # Convert to support transparency
            
            # Remove background
            output_image = remove(input_image)
            
            # Save output as PNG
            output_image.save(output_path, format="PNG")
            
            print(f"Processed: {file} -> {output_path}")
        except Exception as e:
            print(f"Error processing {file}: {e}")
