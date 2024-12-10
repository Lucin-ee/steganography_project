import logging
from PIL import Image

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the default logging level to DEBUG
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("steganography.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

def encode_message_in_image(image_path, message, output_path, lsb_count=1):

    """
    Encodes a secret message into an image using the least significant bits (LSB).

    Args:
        image_path (str): Path to the carrier image.
        message (str): The secret message to encode.
        output_path (str): Path to save the encoded image.
        lsb_count (int, optional): Number of LSBs to use for encoding. Defaults to 1.

    Returns:
        None
    """

    if not (1 <= lsb_count <= 4):
        logging.error("lsb_count must be between 1 and 4")
        raise ValueError("lsb_count must be between 1 and 4")

    logging.info(f"Encoding message into image: {image_path}")
    logging.debug(f"Message: {message}")
    logging.debug(f"LSB Count: {lsb_count}")

    # Convert the message to binary and add a null terminator
    message += chr(0)
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    message_length = len(binary_message)

    # Open the image and calculate the total capacity of the image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    total_capacity = width * height * 3 * lsb_count

    logging.info(f"Image dimensions: {width}x{height}")
    logging.debug(f"Total encoding capacity (bits): {total_capacity}")
    logging.debug(f"Message length (bits): {message_length}")

    # Check if the message fits in the image
    if message_length > total_capacity:
        logging.warning(
            f"Message too large for the image. Can only encode {total_capacity // 8} characters. "
            "Truncating message."
        )
        binary_message = binary_message[:total_capacity]
        message_length = len(binary_message)

    idx = 0  # Keeps track of our position in the binary message

    for y in range(height):
        for x in range(width):
            if idx < message_length:
                # Get the pixel RGB values
                r, g, b = pixels[x, y]

                # Encode the binary message into the LSBs
                if idx < message_length:
                    r = (r & (~((1 << lsb_count) - 1))) | int(binary_message[idx:idx+lsb_count], 2)
                if idx + lsb_count < message_length:
                    g = (g & (~((1 << lsb_count) - 1))) | int(binary_message[idx+lsb_count:idx+2*lsb_count], 2)
                if idx + 2 * lsb_count < message_length:
                    b = (b & (~((1 << lsb_count) - 1))) | int(binary_message[idx+2*lsb_count:idx+3*lsb_count], 2)

                # Update pixel with modified RGB values
                pixels[x, y] = (r, g, b)

                # Move to the next bits in the binary message
                idx += 3 * lsb_count
            else:
                break

    # Save the modified image
    img.save(output_path, "PNG")
    logging.info(f"Message encoded successfully in {output_path}")


def decode_message_from_image(image_path, lsb_count=1):

    """
    Decodes a secret message from an image using the least significant bits (LSB).

    Args:
        image_path (str): Path to the encoded image.
        lsb_count (int, optional): Number of LSBs used for encoding. Defaults to 1.

    Returns:
        message (str): Message that was encoded        
    """

    if not (1 <= lsb_count <= 4):
        logging.error("lsb_count must be between 1 and 4")
        raise ValueError("lsb_count must be between 1 and 4")

    logging.info(f"Decoding message from image: {image_path}")
    logging.debug(f"LSB Count: {lsb_count}")

    # Open the image and load the pixels
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    binary_message = ''
    for y in range(height):
        for x in range(width):
            # Get the pixel RGB values
            r, g, b = pixels[x, y]

            # Extract the `lsb_count` bits from each channel
            binary_message += format(r & ((1 << lsb_count) - 1), f'0{lsb_count}b')
            binary_message += format(g & ((1 << lsb_count) - 1), f'0{lsb_count}b')
            binary_message += format(b & ((1 << lsb_count) - 1), f'0{lsb_count}b')

    # Convert the binary message back to text, stopping at the null terminator
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        if char == chr(0):  # Stop at the null terminator
            break
        message += char

    logging.info("Message decoded successfully")
    logging.debug(f"Decoded Message: {message}")

    return message
