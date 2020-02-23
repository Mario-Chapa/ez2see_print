import inspect
import prettifier
import ez2see_constants as ezc


def ez_to_see_print(header: str, data, style: str = ezc.DEFAULT_STYLE) -> None:
    """
    print helper. Useful when debbuging and want to easily spot a line among a
    stream of logging output.
    """
    log_string = "\n"
    # red is the default
    colors = ezc.styles_ez2c[style]
    # Formatting for pretty-printing of lists and dicts
    type_of_data = str(type(data))
    data = prettifier.prettify(data)

    # Info about the methood from which this print was called
    # We get method name and line number in source file
    # We also obtain all local variables at the moment this call was made
    code_frame = inspect.currentframe().f_back
    local_names = code_frame.f_locals
    local_names_str = "local namespace seen by this frame:" + "\n" + "\n" + prettifier.prettify(local_names) + "\n"
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

    log_string += f"{colors[1]}{__file__.center(ezc.LINE_WIDTH)}{ezc.C_NORMAL}\n"
    log_string += f"{colors[1]}{ezc.LOGSEPARATOR_ST}{ezc.C_NORMAL}\n"
    log_string += f"{colors[0]}{called_from.center(ezc.LINE_WIDTH)}{ezc.C_NORMAL}\n"
    if called_from_frame:
        log_string += f"{colors[0]}{caller_name_str.center(ezc.LINE_WIDTH)}{ezc.C_NORMAL}\n"
        log_string += f"{colors[0]}{line_from_caller_name_str.center(ezc.LINE_WIDTH)}{ezc.C_NORMAL}\n"
    log_string += f"{colors[0]}{header.center(ezc.LINE_WIDTH)}{ezc.C_NORMAL}\n"
    log_string += f"{colors[0]}{type_of_data.center(ezc.LINE_WIDTH)}{ezc.C_NORMAL}\n"
    log_string += colors[2] + "\n"
    log_string += data + "\n"
    log_string += f"{colors[2]}{ezc.LOGSEPARATOR_ST}{ezc.C_NORMAL}\n"
    log_string += f"{colors[2]}{local_names_str.center(ezc.LINE_WIDTH)}{ezc.C_NORMAL}\n"
    log_string += ezc.C_NORMAL + "\n"
    log_string += f"{colors[1]}{ezc.LOGSEPARATOR_DB}{ezc.C_NORMAL}\n"

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
    print(separator)
    print_format_table()
