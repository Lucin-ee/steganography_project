# Steganography Toolkit Tutorial

This tutorial will guide you through the basic usage of the Steganography Toolkit. We'll cover how to hide both messages and images within carrier images, and how to analyze images for potential hidden content.

## 1. Hiding Text Messages in Images

### Basic Message Encoding

Let's start with a simple example of hiding a text message in an image:

```python
from encode_decode_message import encode_message_in_image

# Your secret message
message = "Hello, this is a secret message!"

# Encode the message into an image
encode_message_in_image(
    image_path="original.png",
    message=message,
    output_path="encoded.png",
    lsb_count=1  # Using 1 LSB for subtle changes
)
```

### Extracting Hidden Messages

To extract a hidden message:

```python
from encode_decode_message import decode_message_from_image

# Decode the message
message = decode_message_from_image("encoded.png", lsb_count=1)
print(f"Retrieved message: {message}")
```

### Advanced Usage: Multiple LSB Encoding

For higher capacity (but more visible changes), you can use more LSBs:

```python
# Encode using 3 LSBs for more capacity
encode_message_in_image(
    image_path="original.png",
    message="A longer secret message that needs more space...",
    output_path="encoded.png",
    lsb_count=3
)
```

## 2. Hiding Images within Images

### Image Steganography

To hide one image inside another:

```python
from encode_decode_image import encode_image_in_image

# Hide the secret image in the carrier image
encode_image_in_image(
    carrier_path="carrier.png",
    secret_path="secret.png",
    output_path="encoded.png"
)
```

### Extracting Hidden Images

To extract a hidden image:

```python
from encode_decode_image import decode_image_from_image

# Extract the hidden image
decode_image_from_image(
    encoded_path="encoded.png",
    output_path="decoded_secret.png"
)
```

## 3. Analyzing Images for Hidden Content

The toolkit includes powerful analysis tools to detect potential steganography:

```python
from histogram_analysis import get_lsb_histogram

# Analyze LSB patterns
get_lsb_histogram("suspicious.png", lsb_count=2)
```

This will generate a histogram plot showing the distribution of LSB values, which can help detect anomalies that might indicate hidden data.

## Best Practices

1. Always use PNG format for output images to avoid lossy compression
2. For text messages, start with 1 LSB and only increase if needed
3. Ensure carrier images are significantly larger than secret data
4. Keep carrier and secret images the same size for image-in-image steganography
5. Use the histogram analysis tool to verify the subtlety of your encoding

## Common Issues and Solutions

### Image Size Mismatch

If you get a size mismatch error when hiding images:

```python
from PIL import Image

# Resize secret image to match carrier
secret_img = Image.open("secret.png")
secret_img = secret_img.resize((800, 600))  # Match carrier dimensions
secret_img.save("secret_resized.png")
```

### Message Too Large

If your message is too large for the carrier image:
1. Use a larger carrier image
2. Increase the LSB count (up to 4)
3. Compress your message before encoding

## Next Steps

- Experiment with different LSB counts to find the balance between capacity and visibility
- Try combining techniques (e.g., hiding both text and images)
- Use the histogram analysis to understand how your steganography affects the image
