# [python - How to pretty print nested dictionaries? - Stack Overflow](https://stackoverflow.com/questions/3229419/how-to-pretty-print-nested-dictionaries#3314411)

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

import inspect

def prettify_this(value, htchar='\t', lfchar='\n', indent=0):
    nlch = lfchar + htchar * (indent + 1)
    if type(value) is dict:
        items = [
            nlch + repr(key) + ': ' + prettify_this(value[key], htchar, lfchar, indent + 1)
            for key in value
        ]
        return '{%s}' % (','.join(items) + lfchar + htchar * indent)
    elif type(value) is list:
        items = [
            nlch + prettify_this(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        return '[%s]' % (','.join(items) + lfchar + htchar * indent)
    elif type(value) is tuple:
        items = [
            nlch + prettify_this(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        return '(%s)' % (','.join(items) + lfchar + htchar * indent)
    else:
        return repr(value)

def ez_to_see_print(header: str, data, style: str = DEFAULT_STYLE) -> None:
    """
    print helper. Useful when debbuging and want to easily spot a line among a
    stream of logging output.
    """
    log_string = "\n"
    # red is the default
    colors = styles_ez2c.get(style, styles_ez2c[DEFAULT_STYLE])
    # Formatting for pretty-printing of lists and dicts
    type_of_data = str(type(data))
    data = prettify_this(data)

    # Info about the methood from which this print was called
    # We get method name and line number in source file
    # We also obtain all local variables at the moment this call was made
    code_frame = inspect.currentframe().f_back
    local_names = code_frame.f_locals
    local_names_str = "local namespace seen by this frame:" + "\n" + "\n" + prettify_this(local_names) + "\n"
    caller_frame = inspect.currentframe().f_back
    called_from = caller_frame.f_code.co_name + ": L" + str(caller_frame.f_lineno)

    # And one level up, to the method that called the method from which this print
    # was called
    called_from_frame = caller_frame.f_back
    if called_from_frame:
        line_num_in_caller = called_from_frame.f_lineno
        caller_name = called_from_frame.f_code.co_name
        caller_name_str = "This Method's Caller's name: " + str(caller_name)
        line_from_caller_name_str = "L" + str(line_num_in_caller)

    log_string += f"{colors[1]}{__file__.center(LINE_WIDTH)}{C_NORMAL}\n"
    log_string += f"{colors[1]}{LOGSEPARATOR_ST}{C_NORMAL}\n"
    log_string += f"{colors[0]}{called_from.center(LINE_WIDTH)}{C_NORMAL}\n"
    if called_from_frame:
        log_string += f"{colors[0]}{caller_name_str.center(LINE_WIDTH)}{C_NORMAL}\n"
        log_string += f"{colors[0]}{line_from_caller_name_str.center(LINE_WIDTH)}{C_NORMAL}\n"
    log_string += f"{colors[0]}{header.center(LINE_WIDTH)}{C_NORMAL}\n"
    log_string += f"{colors[0]}{type_of_data.center(LINE_WIDTH)}{C_NORMAL}\n"
    log_string += colors[2] + "\n"
    log_string += data + "\n"
    log_string += f"{colors[2]}{LOGSEPARATOR_ST}{C_NORMAL}\n"
    log_string += f"{colors[2]}{local_names_str.center(LINE_WIDTH)}{C_NORMAL}\n"
    log_string += C_NORMAL + "\n"
    log_string += f"{colors[1]}{LOGSEPARATOR_DB}{C_NORMAL}\n"

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

    print(ez_to_see_print("Test with a string, red style", test_string, "red"))
    print(separator)  # print a white line
    print(ez_to_see_print("Test with a list, orange style", test_list, "orange"))
    print(separator)
    print(ez_to_see_print("Test with a dict, green style", test_dict, "green"))
    print(separator)
    print(ez_to_see_print("Test with a string, blue style", test_string, "blue"))
    print(separator)
    print(ez_to_see_print("Test with a list, purple style", test_list, "purple"))
    print(separator)
    print(ez_to_see_print("Test with a dict, cyan style", test_dict, "cyan"))
