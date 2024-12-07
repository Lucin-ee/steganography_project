import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'steganography_project')))

from steganography_project.encode_decode_image import encode_image_in_image
from steganography_project.encode_decode_image import decode_image_from_image

carrier = "img5.png"
secret = "img6.png"


# Encode secret image into carrier image
encode_image_in_image(carrier, secret, "img6inimg5.png")

# Decode secret image from encoded image
decode_image_from_image("img6inimg5.png", "decodedimg6.png")


