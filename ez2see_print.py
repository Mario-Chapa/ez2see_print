import json  # for dict pretty formating

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

# You can use this to test the colors output in your terminal
def print_colors_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


# styles need 3 colors, for header, separators and contents in that order
styles_ez2c = {
    "red": (H_RED, B_RED, F_ORANGE),
    "orange": (H_ORANGE, B_ORANGE, F_RED),
    "green": (H_GREEN, B_GREEN, F_CYAN),
    "cyan": (H_CYAN, B_CYAN, F_GREEN),
    "blue": (H_BLUE, B_BLUE, F_PURPLE),
    "purple": (H_PURPLE, B_PURPLE, F_BLUE),
}

LINE_WIDTH = 60
LOGSEPARATOR_DB = "=" * LINE_WIDTH
LOGSEPARATOR_ST = "*" * LINE_WIDTH


def ez_to_see_print(header: str, data, style: str = "red") -> None:
    """
    print helper. Useful when debbuging and want to easily spot a line amont a
    stream of logging output.
    """
    # red is the default
    colors = styles_ez2c.get(style, styles_ez2c["red"])
    # Formatting for pretty-printing of lists and dicts
    if isinstance(data, dict):
        data = json.dumps(data, indent=4, sort_keys=True)
    elif isinstance(data, list):
        data = '\n'.join(data)

    print(f"{colors[1]}{__file__.center(LINE_WIDTH)}{C_NORMAL}")
    print(f"{colors[1]}{LOGSEPARATOR_ST}{C_NORMAL}")
    print(f"{colors[0]}{header.center(LINE_WIDTH)}{C_NORMAL}")
    print(colors[2])
    print(data)
    print(C_NORMAL)
    print(f"{colors[1]}{LOGSEPARATOR_DB}{C_NORMAL}")


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


if __name__ == "__main__":
    test_string = "test this is a test, i want to see this string."
    test_list = ["test", "another", "one more"]
    test_dict = {"test": "value", "another_key": "last", "key": "val"}
    separator = "\n" * 3

    ez_to_see_print("Test with a string, red style", test_string, "red")
    print(separator)  # print a white line
    ez_to_see_print("Test with a list, orange style", test_list, "orange")
    print(separator)
    ez_to_see_print("Test with a dict, green style", test_dict, "green")
    print(separator)
    ez_to_see_print("Test with a string, blue style", test_string, "blue")
    print(separator)
    ez_to_see_print("Test with a list, purple style", test_list, "purple")
    print(separator)
    ez_to_see_print("Test with a dict, cyan style", test_dict, "cyan")
