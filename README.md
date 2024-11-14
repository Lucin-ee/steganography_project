# **Steganography Project**

This project provides a simple Python-based tool for hiding and extracting messages within images using the least significant bit (LSB) steganography method. It includes functionality for encoding and decoding messages, analyzing image histograms for potential hidden data, and basic steganalysis.

## **Features**

Message Encoding: Hides a text message within an image using the specified number of LSBs.
Message Decoding: Extracts a hidden message from an image.
LSB Histogram Analysis: Generates histograms of LSB patterns in images to detect possible hidden data.
Prerequisites

Python 3.8+
Poetry: Used for dependency management, versioning, and packaging. Install Poetry from Poetry's installation guide.
Installation

### Clone the repository:
git clone https://github.com/yourusername/steganography_project.git
cd steganography_project
Install dependencies with Poetry:
poetry install
Usage

### Encoding and Decoding Messages
You can encode a message in an image, decode it, and analyze the image’s LSB histograms.

### Encoding a Message
To encode a message, use the following command:

poetry run encode <input_image_path> "<message>" <output_image_path> <lsb_count>
Example:

poetry run encode img.png "Hello, World!" encoded_img.png 2
Decoding a Message
To decode a message from an image, use:

poetry run decode <encoded_image_path> <lsb_count>
Example:

poetry run decode encoded_img.png 2
Histogram Analysis for Steganalysis
Generate LSB histograms for each color channel in an image:

poetry run histogram <image_path> <lsb_count>
Example:

poetry run histogram encoded_img.png 2
This will save a histogram plot as a PNG file in the current directory.
Running Tests
To run the test suite, use:

poetry run pytest
Project Structure

steganography_project/
├── steganography_project/
│   ├── __init__.py                # Initializes the package
│   ├── encode_decode.py           # Encoding and decoding functions
│   └── histogram_analysis.py      # LSB histogram analysis function
├── tests/                         # Test suite for functions
├── README.md                      # Project documentation
└── pyproject.toml                 # Poetry configuration file


All parameters, including the LSB count (up to 4), can be configured directly through the command line when running the encode, decode, and histogram analysis commands.
