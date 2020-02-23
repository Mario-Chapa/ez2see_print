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

def get_local_vars_trace_str(header: str, style: str = ezc.DEFAULT_STYLE) -> None:

    # try to obtain the specified style, fallback to DEFAULT
    colors = ezc.styles_ez2c.get(style, ezc.styles_ez2c[ezc.DEFAULT_STYLE])

    # Info about the method from which this print was called
    # We get method name and line number in source file
    # We also obtain all local variables at the moment this call was made
    code_frame = inspect.currentframe().f_back
    local_names = code_frame.f_locals
    local_names_str = "local namespace seen by this frame:" + "\n" + "\n" + prettifier.prettify(local_names) + "\n"
    caller_frame = inspect.currentframe().f_back
    method_name = caller_frame.f_code.co_name
    called_from = f"Method's name: {method_name}() from L{str(caller_frame.f_lineno)}"

    # And one level up, to the method that called the method from which this print
    # was called
    called_from_frame = caller_frame.f_back

    if called_from_frame:
        line_num_in_caller = called_from_frame.f_lineno
        caller_name = called_from_frame.f_code.co_name
        caller_name_str = f"{method_name}()'s caller name: {str(caller_name)} from L{str(line_num_in_caller)}"

    log_string = _get_colorized_line_str(LOGSEPARATOR_DB, colors[1])
    log_string += _get_colorized_line_str(_get_centered_str(header), colors[0])
    log_string += _get_colorized_line_str(_get_centered_str(f"File name: {__file__}"), colors[0])
    log_string += _get_colorized_line_str(_get_centered_str(called_from), colors[0])
    if called_from_frame:
        log_string += _get_colorized_line_str(_get_centered_str(caller_name_str), colors[0])
    log_string += _get_colorized_line_str(LOGSEPARATOR_ST, colors[2])
    log_string += _get_colorized_line_str(_get_centered_str(local_names_str), colors[2])
    log_string += _get_colorized_line_str(LOGSEPARATOR_ST, colors[2])
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

    def testing_tracer():
        test_var = 0
        another_var = ["a", "b", "c"]
        print(get_local_vars_trace_str("Showcasing get_local_vars_trace_str", "green"))

    res = input("Show get_colored_data_str()? y/n >>> ")
    if res.lower() == 'y':
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

    res = input("Show get_local_vars_trace_str()? y/n >>> ")
    if res.lower() == 'y':
        testing_tracer()

    res = input("Show Colors Format table? y/n >>> ")
    if res.lower() == 'y':
        print_format_table()
