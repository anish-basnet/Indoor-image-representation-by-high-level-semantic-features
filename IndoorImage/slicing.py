"""
 -AUTHOR: Anish Basnet
 -EMAIL: anishbasnetworld@gmail.com
 -DATE : 9/25/2024

 This is the module which slice the images into sub-images.
"""
import os, re
from ctypes import windll
from idlelib.sidebar import LineNumbers

from PIL import Image

def slicing(src: str, dest: str, isCategory: bool = False, numSubImages: int = 9, numImagePerCategory: int = 100, Random: bool = False):
    """
    This function slice image into sub image.
    :param src: String -> Source of the image or directory of classes
    :param dest: String -> Destination of the sub-images or directory of sub-images
    :param isCategory: Boolean -> Set True if it's a directory containing images (default: False)
    :param numSubImages: Integer -> Number of slice of an image (default: 9)
    :param numImagePerCategory: Integer -> Number of Image Per category (default: 100)
    :param Random: Boolean -> Randomly select images per category or not? (default: False)
    :return:
    """
    def _verifyImage(imgPath: str) -> bool:
        """
        This function will verify for the image.
        :param imgPath: String -> Path of the image
        :return: Boolean -> True if the given path is image else False
        """
        try:
            with Image.open(imgPath) as img:
                img.verify()
                return True
        except (IOError, SyntaxError) as e:
            print(f"{imgPath} : Image is not valid or is corrupted")
            return False

    def _sliceImage(imgPath: str, numSubImages: int):
        """
        This private function slice the image into parts
        :param imgPath:
        :return:
        """
        with Image.open(imgPath) as img:
            print(img.size)
            sliceSize: int = 0
            for i in range(1, numSubImages):
                if i*i == numSubImages:
                    sliceSize = i
                    break
                assert i*i > numSubImages, f"Number of sub-images per image -> {numSubImages} should be squared number"
            print(sliceSize)
            #TODO : slice the image into sliceSize and write the image into dest

    srcPath = os.path.join(*re.split(r"[\\/]", src))
    print('srcpath',srcPath)
    if isCategory:
        assert os.path.isdir(srcPath)
    else:
        print('check for file')
        assert os.path.isfile(srcPath)
        isImage = _verifyImage(srcPath)
        if isImage:
            _sliceImage(srcPath, numSubImages=numSubImages)
