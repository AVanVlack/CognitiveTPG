import pillow


def convert_image(image):
    """
    Converts an image to a bytearray
    """
    return bytearray(image.tobytes())
