from PIL import Image, ImageFilter


# image = Image.open("../image.jpg")
# with image as img:
#     img.load()
#     blur_img = img.filter(ImageFilter.BoxBlur(2))
#     # blur_img.show()
#
# blur_img.save("out.png")
def out_of_range_processing(color):
    if color < 0:
        return 0

    if color > 255:
        return 255

    return color


def get_smoothing_image(image, filter_kernel):
    source_image_pixels = image.load()
    final_image = image.copy()
    final_image_pixels = final_image.load()
    width, height = image.size
    # print("ширина", image.width)
    # print("высота", image.height)
    # ширина 1024
    # высота 768
    indent = (len(filter_kernel) - 1) // 2
    # print(indent)

    # Проходим по всем пикселям картинки
    for x in range(indent, width - indent):
        for y in range(indent, height - indent):
            # print("x_1", x, "y_1", y)
            new_red_color = 0
            new_green_color = 0
            new_blue_color = 0

            for matrix_x in range(-indent, indent + 1):
                for matrix_y in range(-indent, indent + 1):
                    # print("x_2", matrix_x, "y_2", matrix_y)
                    source_pixel = source_image_pixels[x + matrix_x, y + matrix_y]

                    new_red_color += source_pixel[0] * kernel[matrix_x + indent][matrix_y + indent]
                    new_green_color += source_pixel[1] * kernel[matrix_x + indent][matrix_y + indent]
                    new_blue_color += source_pixel[2] * kernel[matrix_x + indent][matrix_y + indent]

            new_red_color = out_of_range_processing(new_red_color)
            new_green_color = out_of_range_processing(new_green_color)
            new_blue_color = out_of_range_processing(new_blue_color)

            final_image_pixels[x, y] = (round(new_red_color), round(new_green_color), round(new_blue_color))

    return final_image


kernel = [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]
user_image = Image.open("../image.jpg")

user_final_image = get_smoothing_image(user_image, kernel)
user_final_image.save("out.png")
