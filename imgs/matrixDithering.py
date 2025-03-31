from PIL import Image

def dithering(image):
    width, height = image.size
    matrix = [
        [230, 51, 128],
        [25, 102, 179],
        [154, 205, 77]
    ]

    # Create a new image for the output
    output_image = Image.new("RGBA", (width, height))
    pixels = output_image.load()

    # Iterate over each pixel and apply the dithering logic
    for y in range(height):
        for x in range(width):
            r, g, b, a = image.getpixel((x, y))
            i, j = x % 3, y % 3
            matrix_value = matrix[j][i]
            r = 255 if r >= matrix_value else 0
            g = 255 if g >= matrix_value else 0
            b = 255 if b >= matrix_value else 0
            pixels[x, y] = (r, g, b, a)

    return output_image

# Example usage
input_image = Image.open("input_image.png")
output_image = dithering(input_image)
output_image.save("dithered_image.png")

'''Key Features:
   - Matrix: It uses the same 3x3 matrix for dithering as in your Lua code.
   - Color Threshold: Pixels are adjusted based on whether their value is greater than the corresponding matrix value.
   - Pillow Library: Facilitates image manipulation in Python.
You'll need to install the Pillow library if you haven't already. Use pip install pillow to get started. Let me know if you need further explanations or tweaks!
