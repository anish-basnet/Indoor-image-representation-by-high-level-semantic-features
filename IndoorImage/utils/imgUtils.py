"""
 -Author: Anish Basnet
 -Email: anishbasnetworld@gmail.com
 -Date: Oct 6, 2024

 This file has the utility function related to images.
"""
from PIL import Image
import os, re
import numpy as np

def verifyImage(imgPath: str) -> bool:
    """
    This function will verify for the image.
    :param imgPath: String -> Path of the image
    :return: Boolean -> True if the given path is image else False
    """
    src_path = os.path.join(*re.split(r"[\\/]", imgPath))
    print(src_path)
    assert os.path.isfile(src_path), f"{src_path} is not file type"
    try:
        with Image.open(imgPath) as img:
            img.load()
            return True
    except (IOError, SyntaxError):
        print(f"{imgPath} : Image is not valid or is corrupted")
        return False

def toImageFromPySpark(image_data):
    """
    This function return pyspark image data structure into pillow image structure by converting the image into RBG.
    :param image_data:
    :return:
    """
    img_data = image_data.data  # Access the image data
    img_width = image_data.width
    img_height = image_data.height

    # Convert image data to a numpy array
    img_array = np.frombuffer(img_data, np.uint8)  # Load as uint8

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
    return img