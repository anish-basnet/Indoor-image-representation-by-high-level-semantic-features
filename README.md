
# Indoor Image Representation by High Level Semantic Features with PySpark

## Overview

This project utilizes PySpark to load and process images from a specified directory. It includes functions for slicing images into sub-images and extracting their properties such as width, height, and number of channels.
And sub-images are predicated top 10 keywords using InceptionV3 model.

## Table of Contents
- [Technologies Used](#Technologies Used)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used

- **Python**: The programming language used for development.
- **Apache Spark**: For distributed data processing.
- **Keras**: A high-level neural networks API for building and training deep learning models.
- **InceptionV3**: A pre-trained deep learning model used for image classification.
- **IndoorImage Library**: Custom utility functions for image slicing and loading.


## Features

- Load images from a specified directory using PySpark.
- Display image properties such as width, height, and channels.
- Slice images into smaller sub-images based on defined coordinates.

## Requirements

- Python 3.x
- PySpark
- Required libraries for image processing:
  - IndoorImage (includes `slicing_with_pyspark` and `list_images` functions)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure that Spark is installed and properly configured on your system.

## Usage

To run the image processing script, execute the following command:

```bash
python main.py
```

### Parameters

- **data_path**: Update the `data_path` variable in `main.py` to point to your image directory.

## Functions

- **list_images(data_path)**: This function lists all image file paths in the specified directory.
- **slicing_with_pyspark(width, height)**: A user-defined function (UDF) that generates coordinates for slicing images into smaller parts.
- **InceptionModelViaPyspark(image_data, sub_image_cords, topN:int=10)**: A user-defined function to predict the topN images label of sub-images
## Example Output

When you run the script, you will see the following outputs:

1. A list of image paths loaded from the specified directory.
2. A count of images successfully loaded.
3. The properties of the images, including dimensions and channel information.
4. The sub-image coordinates generated for slicing the images.

```plaintext
Number of images loaded: 4485
+--------------------+
|               image|
+--------------------+
|{file:///home/ani...|
|{file:///home/ani...|
|{file:///home/ani...|
+--------------------+

+-----+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|width|height|sub_image_coordinates                                                                                                                                                               |
+-----+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|509  |220   |[{0, 0, 169, 73}, {169, 0, 338, 73}, {338, 0, 507, 73}, {0, 73, 169, 146}, {169, 73, 338, 146}, {338, 73, 507, 146}, {0, 146, 169, 219}, {169, 146, 338, 219}, {338, 146, 507, 219}]|
+-----+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```


```
[
    {
        "coordinates": [0, 0, 169, 73],
        "predictedWords": [
            "comic_book", "cassette", "screen", "rocking_chair", 
            "scoreboard", "book_jacket", "television", "folding_chair", 
            "cinema", "mousetrap"
        ]
    },
    {
        "coordinates": [169, 0, 338, 73],
        "predictedWords": [
            "sewing_machine", "pay-phone", "gas_pump", "cassette", 
            "hard_disc", "vending_machine", "mousetrap", "packet", 
            "washer", "comic_book"
        ]
    },
    {
        "coordinates": [338, 0, 507, 73],
        "predictedWords": [
            "comic_book", "jigsaw_puzzle", "tobacco_shop", "fire_screen", 
            "book_jacket", "oscilloscope", "prayer_rug", "mousetrap", 
            "toyshop", "sewing_machine"
        ]
    },
    {
        "coordinates": [0, 73, 169, 146],
        "predictedWords": [
            "tobacco_shop", "dishwasher", "bakery", "plate_rack", 
            "confectionery", "grocery_store", "shopping_basket", 
            "shoe_shop", "chain", "pretzel"
        ]
    },
    {
        "coordinates": [169, 73, 338, 146],
        "predictedWords": [
            "dishwasher", "tobacco_shop", "accordion", "slot", 
            "carpenter's_kit", "toaster", "typewriter_keyboard", 
            "plate_rack", "refrigerator", "sewing_machine"
        ]
    },
    {
        "coordinates": [338, 73, 507, 146],
        "predictedWords": [
            "tobacco_shop", "cup", "comic_book", "slot", 
            "pickelhaube", "strainer", "breastplate", "saltshaker", 
            "buckle", "pitcher"
        ]
    },
    {
        "coordinates": [0, 146, 169, 219],
        "predictedWords": [
            "breastplate", "cuirass", "pickelhaube", "gong", 
            "shield", "buckle", "throne", "pedestal", 
            "comic_book", "triceratops"
        ]
    },
    {
        "coordinates": [169, 146, 338, 219],
        "predictedWords": [
            "thimble", "steel_drum", "cocktail_shaker", "beaker", 
            "bottlecap", "pop_bottle", "safety_pin", 
            "water_bottle", "Petri_dish", "nematode"
        ]
    },
    {
        "coordinates": [338, 146, 507, 219],
        "predictedWords": [
            "can_opener", "pencil_sharpener", "washbasin", 
            "corkscrew", "toilet_seat", "plunger", 
            "barbershop", "Petri_dish", "syringe", "barber_chair"
        ]
    }
]
```

## Code Overview

- The script begins by setting up a Spark session and loading images from the specified directory.
- It defines User Defined Functions (UDFs) for image slicing and for making predictions with the InceptionV3 model.
- The images are processed in parallel using Spark, improving efficiency when handling large datasets.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.