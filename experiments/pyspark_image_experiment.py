import os
from pyspark.sql import SparkSession
from PIL import Image
import numpy as np

if __name__ == '__main__':
    # Create Spark session
    spark = SparkSession.builder.appName('ImageLoader').getOrCreate()

    # Define the path to your image directory
    data_path = os.path.join('data', '6.jpg')

    # Load the image
    img_df = spark.read.format('image').load(data_path)

    # Show DataFrame contents and schema
    img_df.show()
    img_df.printSchema()

    # Extract the first image record
    img_row = img_df.first()  # Get the first row
    img_data = img_row.image.data  # Access the image data
    img_width = img_row.image.width
    img_height = img_row.image.height

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
    img.show()  # Optionally display the image
