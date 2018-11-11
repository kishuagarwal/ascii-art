from camera import get_webcam_image
import colorama
from colorama import ansi

MAX_TERMINAL_IMAGE_SIZE = 50
MAX_BRIGHTNESS_LEVEL = 255

ascii_brightness_levels = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def get_ascii_for_pixel(pixel, algo = "AVG"):
    """
    Given a pixel it returns the corresponding the ascii character which denotes the pixel brightness.
    """
    if algo == "AVG":
        avg_brightness = (pixel[0] + pixel[1] + pixel[2]) // 3
    elif algo == "L":
        avg_brightness = int(0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2])
    elif algo == "MIN_MAX":
        avg_brightness = (max(pixel[0], pixel[1], pixel[2]) + min(pixel[0], pixel[1], pixel[2])) // 2

    max_ascii_level = len(ascii_brightness_levels) - 1
    return ascii_brightness_levels[int((max_ascii_level / MAX_BRIGHTNESS_LEVEL) * avg_brightness)]


if __name__ == "__main__":
    # input_image = Image.open("input.jpg")
    colorama.init()

    # Clear the screen before outputting the ascii image
    print(ansi.clear_screen())

    try:
        while True:
            input_image = get_webcam_image()
            width, height = input_image.size

            resize_to = min(width, height, MAX_TERMINAL_IMAGE_SIZE)
            input_image = input_image.resize((resize_to, resize_to))

            output_matrix = []
            for y in range(resize_to):
                current_matrix_row = []
                for x in range(resize_to):
                    pixel = input_image.getpixel((x, y))
                    ascii_char = get_ascii_for_pixel(pixel, algo="L")
                    current_matrix_row.append(ascii_char)
                    current_matrix_row.append(ascii_char)
                    current_matrix_row.append(ascii_char)
                output_matrix.append(''.join(current_matrix_row))

            # Resets the cursor at position at the start for redrawing
            print(ansi.Cursor.POS(1, 1))
            output_str = '\n'.join(output_matrix)

            # Printing in this way, really speeds up the output. Otherwise two loops will really
            # slow it down
            print(output_str)
    except KeyboardInterrupt as e:
        # Clear the screen when the user presses interrupts the program CTRL ^ C
        print(ansi.clear_screen())
