import tensorflow as tf
import os

def process_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image, channels=3)  # Force 3 channels (RGB)

    shape = tf.shape(image)[:2]  # Get height and width
    min_dim = tf.reduce_min(shape)  # Find the smallest dimension
    offset = (shape - min_dim) // 2  # Compute crop offset

    cropped = tf.image.crop_to_bounding_box(image, offset[0], offset[1], min_dim, min_dim)
    resized = tf.image.resize(cropped, [512, 512])
    return tf.cast(resized, tf.uint8)  # Convert to uint8

def process_images_in_directory(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".png")  # Save as PNG

        image = process_image(input_path)
        encoded_image = tf.io.encode_png(image)  # Save as PNG

        tf.io.write_file(output_path, encoded_image)
        print(f"Processed: {filename} -> {output_path}")

# Usage
input_directory = "new_partial_dataset/downey_mildew"
output_directory = "downey_mildew_resized"
process_images_in_directory(input_directory, output_directory)
