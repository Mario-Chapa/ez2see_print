# Back to notmal coloring
C_NORMAL = '\x1b[0m'

# F colors are foreground colored output with black background
F_RED = '\x1b[1;31;40m'
F_GREEN = '\x1b[1;32;40m'
F_ORANGE = '\x1b[1;33;40m'
F_BLUE = '\x1b[1;34;40m'
F_PURPLE = '\x1b[1;35;40m'
F_CYAN = '\x1b[1;36;40m'

# b colors are colored background with black font
B_RED = '\x1b[1;30;41m'
B_GREEN = '\x1b[1;30;42m'
B_ORANGE = '\x1b[1;30;43m'
B_BLUE = '\x1b[1;30;44m'
B_PURPLE = '\x1b[1;30;45m'
B_CYAN = '\x1b[1;30;46m'

# h colors have a white background and colored letters
H_RED = '\x1b[1;31;47m'
H_GREEN = '\x1b[1;32;47m'
H_ORANGE = '\x1b[1;33;47m'
H_BLUE = '\x1b[1;34;47m'
H_PURPLE = '\x1b[1;35;47m'
H_CYAN = '\x1b[1;36;47m'

# styles need 3 colors, for header, separators and contents in that order
styles_ez2c = {
    "red": (H_RED, B_RED, F_ORANGE),
    "orange": (H_ORANGE, B_ORANGE, F_RED),
    "green": (H_GREEN, B_GREEN, F_CYAN),
    "cyan": (H_CYAN, B_CYAN, F_GREEN),
    "blue": (H_BLUE, B_BLUE, F_PURPLE),
    "purple": (H_PURPLE, B_PURPLE, F_BLUE),
}

DEFAULT_STYLE = "red"

LINE_WIDTH = 60
LOGSEPARATOR_DB = "=" * LINE_WIDTH
LOGSEPARATOR_ST = "*" * LINE_WIDTH