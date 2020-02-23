import inspect
import prettifier
from os import get_terminal_size
import ez2see_constants as ezc

LINE_WIDTH = 60
LOGSEPARATOR_DB = "=" * LINE_WIDTH
LOGSEPARATOR_ST = "*" * LINE_WIDTH

def _get_colorized_line_str(text, color):
    color_str = f"{color}{text}{ezc.C_NORMAL}\n"
    return color_str

def _get_centered_str(text):
    return text.center(LINE_WIDTH)

def get_colored_data_str(header: str, data, style: str = ezc.DEFAULT_STYLE) -> None:
    """
    print helper. Useful when debbuging and want to easily spot a line among a
    stream of logging output.
    """

    # try to obtain the specified style, fallback to DEFAULT
    colors = ezc.styles_ez2c.get(style, ezc.styles_ez2c[ezc.DEFAULT_STYLE])

    # Formatting for pretty-printing of lists and dicts
    type_of_data = "The type of this Data is: " + str(type(data))
    data = prettifier.prettify(data)

    log_string = _get_colorized_line_str(LOGSEPARATOR_DB, colors[1])
    log_string += _get_colorized_line_str(_get_centered_str(header), colors[0])
    log_string += _get_colorized_line_str(_get_centered_str(type_of_data), colors[0])
    log_string += _get_colorized_line_str(LOGSEPARATOR_ST, colors[2])
    log_string += _get_colorized_line_str(data, colors[2])
    log_string += _get_colorized_line_str(LOGSEPARATOR_ST, colors[2])
    log_string += _get_colorized_line_str(_get_centered_str(" "), colors[0])
    log_string += _get_colorized_line_str(LOGSEPARATOR_DB, colors[1])

    return log_string


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

    print(get_colored_data_str("Test with a string, red style", test_string, "red"))
    print(separator)  # print a white line
    print(get_colored_data_str("Test with a list, orange style", test_list, "orange"))
    print(separator)
    print(get_colored_data_str("Test with a dict, green style", test_dict, "green"))
    print(separator)
    print(get_colored_data_str("Test with a string, blue style", test_string, "blue"))
    print(separator)
    print(get_colored_data_str("Test with a list, purple style", test_list, "purple"))
    print(separator)
    print(get_colored_data_str("Test with a dict, cyan style", test_dict, "cyan"))
    print(separator)
    print_format_table()
