from PIL import Image


def get_limited_color(color):
    if color <= 0:
        return 0
    elif color >= 255:
        return 255
    else:
        return round(color)


def get_filter_image(source_image, filter_kernel):
    width, height = source_image.size
    source_image_pixels = source_image.load()
    resultant_image = source_image.copy()
    result_image_pixels = resultant_image.load()
    indent = len(filter_kernel) // 2

    # Проходим по пикселям картинки
    for x in range(indent, width - indent):
        for y in range(indent, height - indent):
            new_red_color = 0
            new_green_color = 0
            new_blue_color = 0

            for shift_by_center_x in range(-indent, indent + 1):
                for shift_by_center_y in range(-indent, indent + 1):
                    source_pixel = source_image_pixels[x + shift_by_center_x, y + shift_by_center_y]

                    new_red_color += source_pixel[0] * kernel[shift_by_center_x + indent][shift_by_center_y + indent]
                    new_green_color += source_pixel[1] * kernel[shift_by_center_x + indent][shift_by_center_y + indent]
                    new_blue_color += source_pixel[2] * kernel[shift_by_center_x + indent][shift_by_center_y + indent]

            new_red_color = get_limited_color(new_red_color)
            new_green_color = get_limited_color(new_green_color)
            new_blue_color = get_limited_color(new_blue_color)

            result_image_pixels[x, y] = (new_red_color, new_green_color, new_blue_color)

    return resultant_image


kernel = [
    [1 / 9, 1 / 9, 1 / 9],
    [1 / 9, 1 / 9, 1 / 9],
    [1 / 9, 1 / 9, 1 / 9]
]
user_source_image = Image.open("../image.jpg")

user_result_image = get_filter_image(user_source_image, kernel)
user_result_image.save("out.png")
