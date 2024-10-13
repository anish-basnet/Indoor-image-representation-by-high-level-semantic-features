import os

from keras._tf_keras.keras.applications.inception_v3 import InceptionV3

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField, StringType

from IndoorImage.slicing import slicing_with_pyspark
from IndoorImage.utils import list_images
from IndoorImage.model import InceptionModelViaPyspark

if __name__ == '__main__':
    # Create Spark session
    spark = SparkSession.builder.appName('ImageLoader').getOrCreate()

    # Define the path to your image directory
    data_path = os.path.join('data', 'Scene15')

    # list the images
    images_list = list_images(data_path)

    # covert list of image to dataframe of image paths
    path_dir = spark.createDataFrame([(path,) for path in images_list], ["path"])

    # load images using spark form the path in the dataframe
    images_df = spark.read.format('image').load(path_dir.rdd.map(lambda row: row.path).collect())

    # Check if images were loaded
    if images_df.count() == 0:
        print("No images were loaded. Please check the file paths and formats.")
    else:
        print(f"Number of images loaded: {images_df.count()}")

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

        images_with_slices_df.show()
        images_with_slices_df.printSchema()

        # Define the schema
        schema = ArrayType(
            StructType([
                StructField("coordinates", ArrayType(IntegerType()), False),  # Array of integers for coordinates
                StructField("words", ArrayType(StringType()), False)  # Array of strings for words
            ])
        )
        model = InceptionV3(weights='imagenet')
        #  registering the UDF
        inceptionV3_prediction_udf = udf(InceptionModelViaPyspark, schema)
        # #


        predict_images_label_df = (images_with_slices_df.withColumn
                                 ('predictedWords',inceptionV3_prediction_udf( images_with_slices_df.image,
                                images_with_slices_df.sub_image_coordinates)))

        predict_images_label_df.show()
        predict_images_label_df.printSchema()
        predict_images_label_df.select('predictedWords').show(1, truncate=False)

    # Stop Spark session when done
    spark.stop()