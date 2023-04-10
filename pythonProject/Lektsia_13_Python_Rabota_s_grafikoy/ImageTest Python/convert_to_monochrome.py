from PIL import Image

image = Image.open("../image.jpg")
pixels = image.load()

MAX_RGB = 255

width, height = image.size

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        grey_color = round(0.3 * pixel[0] + 0.59 * pixel[1] + 0.11 * pixel[2])
        pixels[x, y] = (grey_color, grey_color, grey_color)

image.save("out.png")
