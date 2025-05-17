import sys
import time

def clear_last_line() :
    # time.sleep(1)
    sys.stdout.write(f'\x1b[1A')
    sys.stdout.write('\x1b[2K')
    sys.stdout.flush()


RESET = '\033[0m'

def get_color_escape(color, background=False):
    if color is None : return ""
    color = color_to_tuple(color)
    r, g, b = color
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def color_to_tuple(color) :
    if isinstance(color, int) :
        color = fix_color_int(color)
    if isinstance(color, str) :
        color = color_string_to_tuple(color)
    if isinstance(color, tuple) :
        return color

def color_string_to_tuple(color) :
    red = color[0:2]
    green = color[2:4]
    blue = color[4:6]
    return (int(red, base = 16), int(green, base = 16), int(blue, base = 16))

def fix_color_int(color) :
    return str(hex(color))[2:]

def print_color(text, end = "\n", color = "red", background_color = None) :

    if isinstance(color, str) :
        if color.lower() == "red" : color = (255, 0, 0)
        elif color.lower() == "green" : color = (0, 255, 0)
        elif color.lower() == "blue" : color = (0, 0, 255)
    if isinstance(background_color, str) :
        if background_color.lower() == "red" : background_color = (255, 0, 0)
        elif background_color.lower() == "green" : background_color = (0, 255, 0)
        elif background_color.lower() == "blue" : background_color = (0, 0, 255)
    
    print(get_color_escape(color) + get_color_escape(background_color, True) + str(text) + RESET, end = str(end))
