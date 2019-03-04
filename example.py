from terminal_palette import Palette

palette = Palette()

print(
    palette.red('Hello, World!') + palette.green('Hello, World!') +
    palette.blue('Hello, World!') + palette.yellow('Hello, World!'))
print(
    palette.bright_red('Hello, World!') +
    palette.bright_green('Hello, World!') +
    palette.bright_blue('Hello, World!') +
    palette.bright_yellow('Hello, World!'))

for i in range(4):
    string_for_print = ""
    for j in range(4):
        g = 16 * (i * 4 + j)
        string_for_print += palette.rgb(g, g, g)('Hello, World!')

    print(string_for_print)

palette = Palette()

print(
    palette.bg_red('Hello, World!') + palette.bg_green('Hello, World!') +
    palette.bg_blue('Hello, World!') + palette.bg_yellow('Hello, World!'))

for i in range(4):
    string_for_print = ""
    for j in range(4):
        g = 16 * (i * 4 + j)
        string_for_print += palette.bg_rgb(g, g, g)('Hello, World!')

    print(string_for_print)

palette = Palette()

print(
    palette.bold('Hello, World!') + palette.underline('Hello, World!') +
    palette.reversed('Hello, World!'))

palette1 = Palette()
palette2 = Palette()
palette3 = Palette()

print(
    palette1.red('Hello, World!' + palette2.blue(
        'Hel' + palette3.black.bg_cyan.underline('lo, ') + 'World!') +
                 'Hello, World!'))
