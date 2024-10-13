"""
 -AUTHOR: Anish Basnet
 -EMAIL: anishbasnetworld@gmail.com
 -DATE : Oct 5 2024

 This is the example of predicting the sub-images into category using inceptionV3 model.
"""

import argparse
from IndoorImage.model import InceptionModelPredict

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="This script provides the co-ordinate of the sub-image from image."
    )
    parser.add_argument("-n", required=False, default=10, type=int,
                        help="Number of top prediction.")
    parser.add_argument("--src", required=True, type=str,
                        help="Source image path (for a single image).")

    # Parse the initial arguments
    args = parser.parse_args()

    # Output the parsed arguments for verification
    print(f"Sour ce: {args.src}")
    print(f"Sub-images per image: {args.n}")

    label_with_score = InceptionModelPredict(image_path=args.src, NumPrediction=args.n)

    print(label_with_score)