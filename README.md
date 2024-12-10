# Python Steganography Toolkit

A powerful and flexible steganography toolkit that allows you to hide images and text messages within carrier images using LSB (Least Significant Bit) techniques.

## Features

- Hide text messages within images using variable LSB encoding (1-4 bits)
- Hide images within other images using 4-bit LSB encoding
- Advanced histogram analysis for LSB patterns detection
- Comprehensive logging system
- Error handling and input validation

## Installation

```bash
git clone https://github.com/yourusername/steganography-toolkit.git
cd steganography-toolkit
pip install -r requirements.txt
```

## Quick Start

### Hide a Text Message in an Image

```python
from encode_decode_message import encode_message_in_image

# Hide a message using 2 LSBs
encode_message_in_image('carrier.png', 'Secret message!', 'output.png', lsb_count=2)
```

### Extract a Hidden Message

```python
from encode_decode_message import decode_message_from_image

# Extract the message
message = decode_message_from_image('output.png', lsb_count=2)
print(f"Decoded message: {message}")
```

### Hide an Image within Another Image

```python
from encode_decode_image import encode_image_in_image

# Hide secret image in carrier image
encode_image_in_image('carrier.png', 'secret.png', 'output.png')
```

### Analyze LSB Patterns

```python
from histogram_analysis import get_lsb_histogram

# Generate LSB histogram analysis
get_lsb_histogram('suspicious_image.png', lsb_count=2)
```

## Documentation

Detailed documentation is available in the `docs/` directory:
- Tutorial: `docs/tutorials/tutorial.md`
- API Reference: `docs/reference/`

## Requirements

- Python 3.8+
- Pillow (PIL)
- NumPy
- Matplotlib

## License

MIT License. See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
