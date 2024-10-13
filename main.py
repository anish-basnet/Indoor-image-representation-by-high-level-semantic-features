import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField

from IndoorImage.slicing import slicing_with_pyspark
from IndoorImage.utils import list_images

if __name__ == '__main__':
    # Create Spark session
    spark = SparkSession.builder.appName('ImageLoader').getOrCreate()

    # Define the path to your image directory
    data_path = os.path.join('data', 'Scene15')

    # list the images
    images_list = list_images(data_path)

    # covert list of image to dataframe of image paths
    path_dir = spark.createDataFrame([(path,) for path in images_list], ["path"])

    #show the dataframe of path
    path_dir.show(truncate=False)

    # load images using spark form the path in the dataframe
    images_df = spark.read.format('image').load(path_dir.rdd.map(lambda row: row.path).collect())

    # Check if images were loaded
    if images_df.count() == 0:
        print("No images were loaded. Please check the file paths and formats.")
    else:
        print(f"Number of images loaded: {images_df.count()}")
        images_df.show(3)
        images_df.printSchema()
        images_df.select('image.width', 'image.height', 'image.nChannels', 'image.mode').show(10)

        # Define the UDF schema
        schema = ArrayType(StructType([
            StructField("x1", IntegerType(), False),
            StructField("y1", IntegerType(), False),
            StructField("x2", IntegerType(), False),
            StructField("y2", IntegerType(), False)
        ]))

        # registering the UDF
        slicing_udf = udf(slicing_with_pyspark, schema)

        images_with_slices_df = images_df.withColumn('sub_image_coordinates',
                                                     slicing_udf(images_df.image.width, images_df.image.height))

        # Show the result
        images_with_slices_df.select('image.width', 'image.height', 'sub_image_coordinates').show(2, truncate=False)

    # Stop Spark session when done
    spark.stop()