"""
 -AUTHOR: Anish Basnet
 -EMAIL: anishbasnetworld@gmail.com
 -DATE : 9/25/2024

 This is the module provides the slice-coordinate of the sub-images.
"""
import os
import re
from typing import Union, LiteralString, List, Tuple, Optional

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
            slice_size: int = _getNumberSubSlice(numSubImgs)
            slices = _getSlices(img.size[0], img.size[1], slice_size)
            return slices

    src_path = os.path.join(*re.split(r"[\\/]", src))
    assert os.path.isfile(src_path), f"{src_path} is the file type"
    is_image = verifyImage(src_path)
    if is_image:
        slices = _sliceImage(src_path, numSubImgs=numSubImages)
        return slices
    else:
        return None

def _getNumberSubSlice(numSubImages: int) -> int:
    slice_size: int = 0
    for i in range(1, numSubImages):
        if i * i == numSubImages:
            slice_size = i
            break
        assert i * i <= numSubImages, f"Number of sub-images per image -> {numSubImages} should be squared number"
    return slice_size

def _getSlices(width: int, height: int, slice_size: int) -> List[Tuple[int, int, int, int]]:
    X, Y = width // slice_size, height // slice_size
    slices = []
    _X, _Y = 0, 0
    for i in range(slice_size):
        for j in range(slice_size):
            if i == j == 0:
                slices.append((0, 0, _X + X, _Y + Y))
                _X += X
            else:
                slices.append((_X, _Y, _X + X, _Y + Y))
                _X += X
        _X = 0
        _Y += Y
    return slices

def slicing_with_pyspark(width: int, height: int, numSubImages: int = 9) -> Optional[List[Tuple[int, int, int, int]]]:
    slice_size: int = _getNumberSubSlice(numSubImages)
    slices = _getSlices(width, height, slice_size)
    return slices