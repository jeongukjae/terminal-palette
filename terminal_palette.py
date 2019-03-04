__version__ = '0.0.3'

ESCAPE = '\x1b'
RESET = '0'
BRIGHT = '1'

COLOR8 = ('BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN',
          'WHITE')
LOWERED_COLOR8 = [color.lower() for color in COLOR8]
LOWERED_COLOR8.extend(('bright_' + color) for color in LOWERED_COLOR8[:])
BG_LOWERED_COLOR8 = [('bg_' + color) for color in LOWERED_COLOR8[:]]

DECORATIONS = ('BOLD', 'UNDERLINE', 'REVERSED')
LOWERED_DECORATIONS = [decor.lower() for decor in DECORATIONS]


class BGColor:
    BLACK = '40'
    RED = '41'
    GREEN = '42'
    YELLOW = '43'
    BLUE = '44'
    MAGENTA = '45'
    CYAN = '46'
    WHITE = '47'

    RGB = '48'
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


class Decoration:
    BOLD = '1'
    UNDERLINE = '4'
    REVERSED = '7'


def get_color_code(color, bright=False, rgb=None):
    return ESCAPE + "[" + color + (";" + BRIGHT if bright else "") + (
        (";2;" + ";".join(map(str, rgb))) if rgb else "") + "m"


class Palette:
    def __init__(self):
        self._bg_style = self._fg_style = self._decor_style = None
        self.bg_black = self.bg_blue = self.bg_bright_black = self.bg_bright_blue = self.bg_bright_cyan = self.bg_bright_green = self.bg_bright_magenta = self.bg_bright_red = self.bg_bright_white = self.bg_bright_yellow = self.bg_cyan = self.bg_green = self.bg_magenta = self.bg_red = self.bg_white = self.bg_yellow = self.black = self.blue = self.bold = self.bright_black = self.bright_blue = self.bright_cyan = self.bright_green = self.bright_magenta = self.bright_red = self.bright_white = self.bright_yellow = self.cyan = self.green = self.magenta = self.red = self.reversed = self.underline = self.white = self.yellow = self

    def __call__(self, message):
        final_style = ''

        for style in (self._bg_style, self._fg_style, self._decor_style):
            if style is not None:
                final_style += style

        if final_style == '':
            return message

        if '\x1b[0m' in message:
            message = message.replace('\x1b[0m', '\x1b[0m' + final_style)
        return final_style + message + get_color_code(RESET)

    def __getattribute__(self, key):
        if key in LOWERED_COLOR8:
            self._fg_style = get_color_code(
                FGColor.__getattribute__(FGColor,
                                         key.split('_')[-1].upper()),
                'bright' in key)

            return self

        if key in BG_LOWERED_COLOR8:
            self._bg_style = get_color_code(
                BGColor.__getattribute__(BGColor,
                                         key.split('_')[-1].upper()),
                'bright' in key)

            return self

        if key in LOWERED_DECORATIONS:
            self._decor_style = get_color_code(
                Decoration.__getattribute__(Decoration,
                                            key.split('_')[-1].upper()))

            return self

        return super().__getattribute__(key)

    def rgb(self, r, g, b):
        self._fg_style = get_color_code(FGColor.RGB, rgb=(r, g, b))
        return self

    def bg_rgb(self, r, g, b):
        self._bg_style = get_color_code(BGColor.RGB, rgb=(r, g, b))
        return self

    @property
    def default(self):
        self._fg_style = get_color_code(FGColor.DEFAULT)
        return self

    @property
    def bg_default(self):
        self._bg_style = get_color_code(BGColor.DEFAULT)
        return self

    @property
    def reset(self):
        self._bg_style = None
        self._fg_style = None
        self._decor_style = None

        return self
