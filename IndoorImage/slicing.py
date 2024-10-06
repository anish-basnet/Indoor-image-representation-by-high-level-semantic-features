"""
 -AUTHOR: Anish Basnet
 -EMAIL: anishbasnetworld@gmail.com
 -DATE : 9/25/2024

 This is the module provides the slice-coordinate of the sub-images.
"""
import os
import re
from typing import Union, LiteralString
from PIL import Image
from .utils.imgUtils import verifyImage

def slicing(src: str, numSubImages: int = 9):
    """
    This function gives co-ordinate of sub images.
    :param src: String -> Source of the image or directory of classes
    :param numSubImages: Integer -> Number of slice of an image (default: 9)
    :return:
    """

    def _sliceImage(imgPath: Union[LiteralString, str, bytes], numSubImgs: int):

        """
        This private function provides the co-ordinate of sub-images
        :param imgPath:
        :return: [x1, x2, y1, y2] --> co-ordinate of image as (x1, x2): top-left corner, (y1, y2): bottom-right corner
        """
        with Image.open(imgPath) as img:
            slice_size: int = 0
            for i in range(1, numSubImgs):
                if i*i == numSubImgs:
                    slice_size = i
                    break
                assert i * i <= numSubImgs, f"Number of sub-images per image -> {numSubImgs} should be squared number"
            X, Y = img.size[0]//slice_size, img.size[1]//slice_size
            slices = []
            _X, _Y = 0, 0
            for i in range(slice_size):
                for j in range(slice_size):
                    if i==j==0:
                        slices.append((0, 0, _X + X, _Y + Y))
                        _X += X
                    else:
                        slices.append((_X, _Y, _X+X, _Y+Y))
                        _X += X
                _X = 0
                _Y += Y
            return slices

    src_path = os.path.join(*re.split(r"[\\/]", src))
    assert os.path.isfile(src_path), f"{src_path} is the file type"
    is_image = verifyImage(src_path)
    if is_image:
        slices = _sliceImage(src_path, numSubImgs=numSubImages)
        return slices
    else:
        return None