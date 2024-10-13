"""
 -Author: Anish Basnet
 -Email: anishbasnetworld@gmail.com
 -Date: Oct 6, 2024

 This file has the utility function related to images.
"""
from PIL import Image
import os, re

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