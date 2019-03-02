ESCAPE = '\x1b'
RESET = '0'
BRIGHT = '1'

COLOR8 = ('BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN',
          'WHITE')
LOWERCASED_COLOR8 = [color.lower for color in COLOR8]


def get_color_code(color, bright=None):
    return ESCAPE + "[" + color + (";" + BRIGHT if bright else "") + "m"


class BGColor:
    BLACK = '40'
    RED = '41'
    GREEN = '42'
    YELLOW = '43'
    BLUE = '44'
    MAGENTA = '45'
    CYAN = '46'
    WHITE = '47'

    RGB = '38'
    DEFAULT = '49'


class FGColor:
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'

    RGB = '38'
    DEFAULT = '39'


class Color:
    bg = BGColor
    fg = FGColor


class Decoration:
    BOLD = '1'
    UNDERLINE = '4'
    REVERSED = '7'


class BGPalette:
    pass


class FGPalette:
    pass


class Palette:
    fg = FGPalette
    bg = BGPalette


def set_color(color, bright):
    @staticmethod
    def wrap_with_term_color(content):
        return get_color_code(color, bright) + content + get_color_code(RESET)

    return wrap_with_term_color


bg = BGColor()
fg = FGColor()

for color in COLOR8:
    lower_name = color.lower()
    for bright in (True, False):
        setattr(BGPalette, lower_name,
                set_color(BGColor.__getattribute__(bg, color), bright))
        setattr(FGPalette, lower_name,
                set_color(FGColor.__getattribute__(fg, color), bright))
