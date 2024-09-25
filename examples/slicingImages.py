"""
 -AUTHOR: Anish Basnet
 -EMAIL: anishbasnetworld@gmail.com
 -DATE : 9/25/2024

 This is the example of slicing the images into sub-images.
"""

import argparse
from IndoorImage.slicing import slicing  # Assuming you have slicing logic in this module

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="This script slices the images into sub-images."
    )
    parser.add_argument("-isDir", action="store_true",
                        help="Set True if it's a directory containing images in categories (Default: False)")
    parser.add_argument("--sN", required=False, default=9, type=int,
                        help="Number of sub-images per image.")
    parser.add_argument("--src", required=True, type=str,
                        help="Source directory path (for class images) or image path (for a single image).")
    parser.add_argument("--dest", required=True, type=str,
                        help="Destination for the sub-images.")
    parser.add_argument("--num", default=100, type=int,
                        help="Number of images per category (Default 100).")
    parser.add_argument("--random", required=False, default=False, type=bool,
                            help="Randomize images per category (Default: False).")
    # Parse the initial arguments
    args = parser.parse_args()

    # Output the parsed arguments for verification
    print(f"isDir: {args.isDir}")
    print(f"Source: {args.src}")
    print(f"Destination: {args.dest}")
    print(f"Sub-images per image: {args.sN}")
    print(f"Number of images per category: {args.num}")
    print(f"Random: {args.random}")

    slicing(src=args.src, dest=args.dest, isCategory=False, numSubImages=args.sN)
