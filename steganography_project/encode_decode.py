from PIL import Image
import matplotlib.pyplot as plt
import numpy as np



def encode_message_in_image(image_path, message, output_path, lsb_count=1):
    if not (1 <= lsb_count <= 4):
        raise ValueError("lsb_count must be between 1 and 4")
    
    # Convert the message to binary
    message += chr(0)  # Add a null terminator to mark the end of the message
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    message_length = len(binary_message)
    
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()
    
    width, height = img.size
    idx = 0  # Keeps track of our position in the binary message

    for y in range(height):
        for x in range(width):
            if idx < message_length:
                # Get the pixel RGB values
                r, g, b = pixels[x, y]

                # Calculate the new RGB values by encoding `lsb_count` bits of the message
                if idx < message_length:
                    r = (r & (~((1 << lsb_count) - 1))) | int(binary_message[idx:idx+lsb_count], 2)
                if idx + lsb_count < message_length:
                    g = (g & (~((1 << lsb_count) - 1))) | int(binary_message[idx+lsb_count:idx+2*lsb_count], 2)
                if idx + 2*lsb_count < message_length:
                    b = (b & (~((1 << lsb_count) - 1))) | int(binary_message[idx+2*lsb_count:idx+3*lsb_count], 2)

                # Update pixel with modified RGB values
                pixels[x, y] = (r, g, b)
                
                # Move to the next bits in the binary message
                idx += 3 * lsb_count
            else:
                break

    # Save the modified image
    img.save(output_path, "PNG")

def decode_message_from_image(image_path, lsb_count=1):
    if not (1 <= lsb_count <= 4):
        raise ValueError("lsb_count must be between 1 and 4")
    
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    binary_message = ''

    for y in range(height):
        for x in range(width):
            # Get the pixel RGB values
            r, g, b = pixels[x, y]

            # Extract `lsb_count` bits from each color channel
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

    return message
