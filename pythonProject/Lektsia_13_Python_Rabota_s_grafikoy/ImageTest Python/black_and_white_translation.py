from PIL import Image

image = Image.open("../image.jpg")
pixels = image.load()
MAX_RGB = 255
width, height = image.size

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        index_rgb = (int(0.3 * pixel[0]) + int(0.59 * pixel[1]) + int(0.11 * pixel[2]))
        pixels[x, y] = (index_rgb, index_rgb, index_rgb)

image.save("out.png")
