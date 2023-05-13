from PIL import Image

# ASCII characters used to represent the image
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=50):
    """
    Resize the image while preserving the aspect ratio.
    """
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def convert_to_grayscale(image):
    """
    Convert the image to grayscale.
    """
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    """
    Map each pixel to an ASCII character based on the pixel value.
    """
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value / range_width)] for pixel_value in pixels_in_image]
    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=50):
    """
    Convert the image to ASCII art.
    """
    image = resize_image(image, new_width=new_width)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)

    len_pixels_to_chars = len(pixels_to_chars)
    ascii_image = [pixels_to_chars[index: index + new_width] for index in range(0, len_pixels_to_chars, new_width)]

    return "\n".join(ascii_image)

# Replace the file path with the path to your image
file_path = "img.jpg"
image = Image.open(file_path)

ascii_art = convert_image_to_ascii(image)
print(ascii_art)
