from PIL import Image


def get_blurring_image(image, filter_matrix):
    output_image = image.copy()
    input_image_pixels = image.load()
    output_image_pixels = output_image.load()
    width, height = image.size
    shift = (len(filter_matrix) - 1) // 2

    for image_x in range(shift, width - shift):
        for image_y in range(shift, height - shift):
            red_color = 0
            green_color = 0
            blue_color = 0

            for filter_x in range(-shift, shift + 1):
                for filter_y in range(-shift, shift + 1):
                    pixel = input_image_pixels[image_x + filter_x, image_y + filter_y]
                    red_color += pixel[0] * matrix[filter_x + shift][filter_y + shift]
                    green_color += pixel[1] * matrix[filter_x + shift][filter_y + shift]
                    blue_color += pixel[2] * matrix[filter_x + shift][filter_y + shift]

            red_color = saturation(red_color)
            green_color = saturation(green_color)
            blue_color = saturation(blue_color)
            output_image_pixels[image_x, image_y] = (round(red_color), round(green_color), round(blue_color))

    return output_image


def saturation(color):
    max_rgb = 255

    if color < 0:
        return 0

    if color > max_rgb:
        return max_rgb

    return color


input_image = Image.open("../image.jpg")
matrix = [[1/9, 1/9, 1/9],
          [1/9, 1/9, 1/9],
          [1/9, 1/9, 1/9]]

result_image = get_blurring_image(input_image, matrix)
result_image.save("out.png")
