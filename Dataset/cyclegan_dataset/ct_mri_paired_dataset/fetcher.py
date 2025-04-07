from PIL import Image
import os

# Directory containing the original 768x256 images
images_directory = 'test'

# Create output directories
output_directory_mri = 'test/mri'
output_directory_ct = 'test/ct'
output_directory_mask = 'test/mask'

os.makedirs(output_directory_mri, exist_ok=True)
os.makedirs(output_directory_ct, exist_ok=True)
os.makedirs(output_directory_mask, exist_ok=True)

# Get all file names in the 'train' directory
all_files = os.listdir(images_directory)

# Iterate through each image file
for image_file_name in all_files:
    # Construct the path to the current image
    current_image_path = os.path.join(images_directory, image_file_name)

    # Load the current image
    original_image = Image.open(current_image_path)

    # Extract and save each 256x256 subimage into the corresponding folder
    for subimage_number, subimage_type in enumerate(["mri", "ct", "mask"]):
        left = subimage_number * 256
        upper = 0
        right = left + 256
        lower = upper + 256

        # Crop the subimage
        subimage = original_image.crop((left, upper, right, lower))

        # Save the subimage into the corresponding folder
        subimage_folder = [output_directory_mri, output_directory_ct, output_directory_mask][subimage_number]
        os.makedirs(subimage_folder, exist_ok=True)

        # Construct the path to save the subimage
        subimage_path = os.path.join(subimage_folder, f"{os.path.splitext(image_file_name)[0]}_subimage_{subimage_type}.png")
        print(f"Saving subimage to: {subimage_path}")
        
        # Save the subimage
        subimage.save(subimage_path)

print("Subimages extracted and saved successfully.")
