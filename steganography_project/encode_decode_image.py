import logging
from PIL import Image

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the default logging level to DEBUG
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("image_steganography.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

def encode_image_in_image(carrier_path, secret_path, output_path):
    try:
        logging.info(f"Encoding secret image into carrier image.")
        logging.debug(f"Carrier image: {carrier_path}, Secret image: {secret_path}")

        # Open the carrier and secret images
        carrier_img = Image.open(carrier_path)
        secret_img = Image.open(secret_path)

        # Ensure both images are the same size
        if carrier_img.size != secret_img.size:
            logging.error("The carrier and secret images must be the same size.")
            raise ValueError("The carrier and secret images must be the same size")

        logging.info(f"Image sizes validated: {carrier_img.size}")

        # Load pixel data
        carrier_pixels = carrier_img.load()
        secret_pixels = secret_img.load()
        width, height = carrier_img.size

        # Iterate through each pixel
        for y in range(height):
            for x in range(width):
                # Get RGB values of carrier and secret images
                r_c, g_c, b_c = carrier_pixels[x, y]
                r_s, g_s, b_s = secret_pixels[x, y]

                # Take the 4 MSBs of the secret pixel and place them into the carrier
                r_c = (r_c & 0xF0) | (r_s >> 4)
                g_c = (g_c & 0xF0) | (g_s >> 4)
                b_c = (b_c & 0xF0) | (b_s >> 4)

                # Update the carrier pixel
                carrier_pixels[x, y] = (r_c, g_c, b_c)

        # Save the modified carrier image
        carrier_img.save(output_path, "PNG")
        logging.info(f"Image encoded successfully in {output_path}")

    except Exception as e:
        logging.critical(f"An error occurred while encoding the image: {e}")
        raise


def decode_image_from_image(encoded_path, output_path):
    try:
        logging.info(f"Decoding secret image from encoded image.")
        logging.debug(f"Encoded image: {encoded_path}")

        # Open the encoded image
        encoded_img = Image.open(encoded_path)
        width, height = encoded_img.size

        # Create a new blank image for the decoded secret
        decoded_img = Image.new("RGB", (width, height))
        decoded_pixels = decoded_img.load()
        encoded_pixels = encoded_img.load()

        # Iterate through each pixel
        for y in range(height):
            for x in range(width):
                # Extract the 4 LSBs from the encoded image
                r_e, g_e, b_e = encoded_pixels[x, y]
                r_s = (r_e & 0x0F) << 4
                g_s = (g_e & 0x0F) << 4
                b_s = (b_e & 0x0F) << 4

                # Set the pixel in the decoded image
                decoded_pixels[x, y] = (r_s, g_s, b_s)

        # Save the decoded secret image
        decoded_img.save(output_path, "PNG")
        logging.info(f"Image decoded successfully in {output_path}")

    except Exception as e:
        logging.critical(f"An error occurred while decoding the image: {e}")
        raise
