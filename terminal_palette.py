__version__ = '0.0.2'

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


def set_color(color, bright):
    def wrap_with_term_color(content):
        return get_color_code(color, bright) + content + get_color_code(RESET)

    return wrap_with_term_color


class Palette:
    _bg_style = None
    _fg_style = None
    _decor_style = None

    def __call__(self, message):
        final_style = ''

        for style in (self._bg_style, self._fg_style, self._decor_style):
            if style is not None:
                final_style += style

        if final_style == '':
            return message

        return final_style + message + get_color_code(RESET)

    def __getattr__(self, key):
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

        raise AttributeError

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
