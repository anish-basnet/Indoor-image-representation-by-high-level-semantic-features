import numpy as np
from PIL import Image


def get_image_size(image_data):
    img_data = image_data.data  # Access the image data
    img_width = image_data.width
    img_height = image_data.height

    print(img_width, img_height)
    # Convert image data to a numpy array
    img_array = np.frombuffer(img_data, np.uint8)  # Load as uint8

    # Print size of img_array for debugging
    print(f"Image data size: {img_array.size}, Expected size for ({img_height}, {img_width}, 3): {img_height * img_width * 3}")

    # Check number of channels based on size
    expected_size = img_height * img_width

    # Determine if the image is grayscale or RGB based on data size
    if img_array.size == expected_size:  # Grayscale image
        img_array = img_array.reshape((img_height, img_width))  # Reshape to height x width
        img_array = np.stack((img_array,) * 3, axis=-1)  # Convert grayscale to RGB
        img = Image.fromarray(img_array, 'RGB')
    elif img_array.size == expected_size * 3:  # RGB image
        img_array = img_array.reshape((img_height, img_width, 3))  # Reshape to height x width x channels
        img = Image.fromarray(img_array, 'RGB')
    else:
        raise ValueError("Image data size does not match expected dimensions")

    # Print the PIL image object
    print(img)

    # Load the binary image data
    width, height = img.size
    print(f"Image size: {width}x{height}")  # Debug prin

    return (width, height)  # Return the width and height as a tuple
