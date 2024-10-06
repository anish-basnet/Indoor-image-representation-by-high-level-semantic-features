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
        description="This script provides the co-ordinate of the sub-image from image."
    )
    parser.add_argument("--sN", required=False, default=9, type=int,
                        help="Number of sub-images per image.")
    parser.add_argument("--src", required=True, type=str,
                        help="Source image path (for a single image).")

    # Parse the initial arguments
    args = parser.parse_args()

    # Output the parsed arguments for verification
    print(f"Source: {args.src}")
    print(f"Sub-images per image: {args.sN}")

    cord = slicing(src=args.src, numSubImages=args.sN)
    print(cord)