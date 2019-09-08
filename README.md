# Easy to see print (ez2see_print)

Sometimes you need to do some good 'ol printf() debugging. Sometimes whatever information we are trying to obtain from our print statements get drowned by a stream of other logging output.

In such cases migth be convenient to make your printed information standout from everything else in that stream. ez2see_print will give you a hand in achieving that goal.

## Features

- Comes with 6 styles, that are the combination of colors on which the messages will be printed
- Takes care of formating dict and list types for prettier printing
- Shows the file name from where the print function was called

## Usage
This module exposes just one method. It accepts three arguments, "header" that its used as a title for the printed block, "data" which is the information of interest we want to print, and style which can be one of:
- red (default)
- orange
- green
- blue
- purple
- cyan

```python
ez_to_see_print(header: str, data, style: str = "red") -> None
```

## Screenshots