from terminal_palette import Palette


def test_is_palette_callable():
    assert callable(Palette())


def test_colors():
    palette = Palette()
    assert '\x1b[31mHello, World!\x1b[0m' == palette.red('Hello, World!')
    assert '\x1b[34mSome Tests\x1b[0m' == palette.blue('Some Tests')


def test_rgb():
    palette = Palette()
    assert '\x1b[38;2;10;20;30mHello, World!\x1b[0m' == palette.rgb(
        10, 20, 30)('Hello, World!')


def test_nested():
    P = Palette
    assert '\x1b[31mRED!!\x1b[34mBLUE!!\x1b[0m\x1b[31mRED AGAIN!!\x1b[0m' == P(
    ).red('RED!!' + P().blue('BLUE!!') + 'RED AGAIN!!')
