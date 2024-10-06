"""
 -Author: Anish Basnet
 -Email: anishbasnetworld@gmail.com
 -Date: 2024 Oct 6

 This model predict the top 10 classes from the image
"""
from keras._tf_keras.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

from IndoorImage.utils.imgUtils import verifyImage

import matplotlib.pyplot as plt

def InceptionModelPredict(image_path: str=None, NumPrediction:int=5):
    """
    This model predict the image into different label using InceptionV3 model using pre-trained model.
    :param image_path: path -> path of the image to predict
    :param NumPrediction: path -> top prediction made by different classes
    :return:
    """
    global img_array
    # loading the incpetion model
    model = InceptionV3(weights='imagenet')

    # verify if the given path is of image or not
    if verifyImage(image_path):

        # Open the image
        img = Image.open(image_path)

        # check for black and white if exist then convert into RGB
        if img.mode == 'L':
            img = img.convert('RGB')

        # resize the image into the inception model input size
        resize_image = img.resize((299, 299))

        # expand the dim of the image with the batch size 1
        img_array = np.array(resize_image)
        img_array = np.expand_dims(img_array, axis=0)

        # prepare the input images data for model
        img_array = preprocess_input(img_array)


    # passing the image array into the prediction model
    prediction = model.predict(img_array)

    # converting the model output into human-readable format
    decoded_predictions = decode_predictions(prediction, top=5)[0]

    # Print the top N predictions
    label_with_score = [(label, score) for (_, label, score) in decoded_predictions]

    return label_with_score