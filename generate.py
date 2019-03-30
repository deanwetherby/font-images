import os
import re
import string
import argparse

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from random import randint


def generate_characters(font_file, output_folder, image_size):

    characters = string.digits + string.ascii_letters

    black_colors = (0, 10, 20, 30)
    gray_colors = (135, 145, 155)
    white_colors = (215, 225, 235, 245)
    background_colors = white_colors + black_colors + gray_colors

    small_sizes = (8, 12, 16)
    medium_sizes = (20, 24, 28)
    large_sizes = (32, 36, 40)
    font_sizes = small_sizes + medium_sizes + large_sizes

    font_resource_file = os.path.abspath(font_file)

    i = 1
    for char in characters:
        for font_size in font_sizes:
            if font_size > 0:
                for background_color in background_colors:
                    character = char
                    char_image = Image.new('L', (image_size, image_size),
                                           background_color)
                    draw = ImageDraw.Draw(char_image)
                    font = ImageFont.truetype(font_resource_file, font_size)
                    (font_width, font_height) = font.getsize(character)

                    x = (image_size - font_width) / 2
                    y = (image_size - font_height) / 2

                    font_color = 245 if background_color < 200 else 10
                    draw.text((x, y),
                              character,
                              font_color + randint(0, 10),
                              font=font)
                    file_name = output_folder + '/' + str(i) + '_' + str(
                        font_size) + '_' + str(
                            background_color) + '_' + character + '.png'
                    char_image.save(file_name)
                    print(file_name)

                    i = i + 1
    return


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--font', help='True Type Font file (.ttf)')
    parser.add_argument(
        '-s', '--size', type=int, default=64, help='Character image size')
    parser.add_argument(
        '-o', '--output', help='Output folder to place character images')
    return parser.parse_args()


def main():
    args = parse_args()
    generate_characters(args.font, args.output, args.size)


if __name__ == '__main__':
    main()
