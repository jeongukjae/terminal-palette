# terminal-palette

[![Build Status](https://travis-ci.org/JeongUkJae/terminal-palette.svg?branch=master)](https://travis-ci.org/JeongUkJae/terminal-palette) [![codecov](https://codecov.io/gh/jeongukjae/terminal-palette/branch/master/graph/badge.svg)](https://codecov.io/gh/jeongukjae/terminal-palette) [![Python Version](https://img.shields.io/pypi/pyversions/terminal-palette.svg)](https://pypi.org/manage/project/terminal-palette/releases/) [![Pypi status](https://img.shields.io/pypi/status/terminal-palette.svg)](https://pypi.org/manage/project/terminal-palette/releases/)

A simple library to color texts in terminal. (using ANSI color codes)

## Quick Start

### 8 Colors (Foreground)

```python
from terminal_palette import Palette

palette = Palette()

print(
    palette.black('Hello, World!') +
    palette.red('Hello, World!') +
    palette.green('Hello, World!') +
    palette.yellow('Hello, World!') +
    palette.blue('Hello, World!') +
    palette.magenta('Hello, World!') +
    palette.cyan('Hello, World!') +
    palette.white('Hello, World!'))
print(
    palette.bright_black('Hello, World!') +
    palette.bright_red('Hello, World!') +
    palette.bright_green('Hello, World!') +
    palette.bright_yellow('Hello, World!') +
    palette.bright_blue('Hello, World!') +
    palette.bright_magenta('Hello, World!') +
    palette.bright_cyan('Hello, World!') +
    palette.bright_white('Hello, World!'))
```

Result:

![8Color Result](./images/8colors.png)

### 8 Colors (Background)

```python
from terminal_palette import Palette

palette = Palette()

print(
    palette.bg_black('Hello, World!') +
    palette.bg_red('Hello, World!') +
    palette.bg_green('Hello, World!') +
    palette.bg_yellow('Hello, World!') +
    palette.bg_blue('Hello, World!') +
    palette.bg_magenta('Hello, World!') +
    palette.bg_cyan('Hello, World!') +
    palette.bg_white('Hello, World!'))
print(
    palette.bg_bright_black('Hello, World!') +
    palette.bg_bright_red('Hello, World!') +
    palette.bg_bright_green('Hello, World!') +
    palette.bg_bright_yellow('Hello, World!') +
    palette.bg_bright_blue('Hello, World!') +
    palette.bg_bright_magenta('Hello, World!') +
    palette.bg_bright_cyan('Hello, World!') +
    palette.bg_bright_white('Hello, World!'))
```

### RGB

```python
from terminal_palette import Palette

palette = Palette()

print(palette.rgb(10, 147, 256)("Hello, World!")) # foreground
print(palette.bg_rgb(10, 147, 147)("Hello, World!")) # background
```

### Text Decoration

```python
from terminal_palette import Palette

palette = Palette()

print(palette.bold('Hello, World!'))
print(palette.underline('Hello, World!'))
print(palette.reversed('Hello, World!'))
```

### Nested Style

```python
from terminal_palette import Palette as P

palette1 = P()
palette2 = P()

print(palette1.red('RED!!' + palette2.blue('BLUE!!') + 'RED AGAIN!!'))
```
