from terminal_palette import Palette

palette = Palette()

print(f"{palette.red('Hello, World!')} {palette.green('Hello, World!')} " +
      f"{palette.blue('Hello, World!')} {palette.yellow('Hello, World!')}")
print(f"{palette.bright_red('Hello, World!')} " +
      f"{palette.bright_green('Hello, World!')} " +
      f"{palette.bright_blue('Hello, World!')} " +
      f"{palette.bright_yellow('Hello, World!')}")

for i in range(4):
    string_for_print = ""
    for j in range(4):
        g = 16 * (i * 4 + j)
        string_for_print += f"{palette.rgb(g, g, g)('Hello, World!')} "

    print(string_for_print)

palette = Palette()

print(f"{palette.bg_red('Hello, World!')} " +
      f"{palette.bg_green('Hello, World!')} " +
      f"{palette.bg_blue('Hello, World!')} " +
      f"{palette.bg_yellow('Hello, World!')}")

for i in range(4):
    string_for_print = ""
    for j in range(4):
        g = 16 * (i * 4 + j)
        string_for_print += f"{palette.bg_rgb(g, g, g)('Hello, World!')} "

    print(string_for_print)

palette = Palette()

print(f"{palette.bold('Hello, World!')} " +
      f"{palette.underline('Hello, World!')} " +
      f"{palette.reversed('Hello, World!')}")
