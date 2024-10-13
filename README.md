
# Indoor Image Processing with PySpark

## Overview

This project utilizes PySpark to load and process images from a specified directory. It includes functions for slicing images into sub-images and extracting their properties such as width, height, and number of channels.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

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

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.