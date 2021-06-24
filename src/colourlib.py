# 
# Copyright harvey298 2021 GPL
#
import sys
class colours:
    black: str = 30
    red: str = 31
    green: str = 32
    yellow: str = 33
    blue: str = 34
    magenta: str = 35
    cyan: str = 36
    white: str = 37
    reset: str = 0

class formats:
    bold: str = "1m"
    dim: str = "2m"
    italic: str = "3m"
    underline: str = "4m"
    blink: str = "5m"
    no_seen: str = "8m"
    hide_cursor: str = "?25l"
    unhide_cursor: str = "?25h"
    reset: str = "0m"

class useful_vars:
    escape_octal: str = "\033["
    escape_unicode: str = "\u001b["
    escape_hex: str = "\x1b["

def fetch_colour(colour):
    if colour == "black":
        return colours.black

    elif colour == "red":
        return colours.red

    elif colour == "green":
        return colours.green

    elif colour == "yellow":
        return colours.yellow

    elif colour == "blue":
        return colours.blue

    elif colour == "magenta":
        return colours.magenta

    elif colour == "cyan":
        return colours.cyan

    elif colour == "white":
        return colours.white

    elif colour == "reset":
        return colours.reset

    else:
        return False

def fetch_format(format):
    if format == "bold":
        return formats.bold
    elif format == "dim":
        return formats.dim
    elif format == "italic":
        return formats.italic
    elif format == "underline":
        return formats.underline
    elif format == "blink":
        return formats.blink
    elif format == "no_seen":
        return formats.no_seen
    elif format == "hide_cursor":
        return formats.hide_cursor
    elif format == "unhide_cursor":
        return formats.unhide_cursor
    elif format == "reset":
        return formats.reset
    else:
        return False

def mkstr(item):
    return str(item)

def merge_format(format,colour):

    if fetch_colour(colour) != False: # Colour check
        if fetch_format(format) != False: # Format check
            input = useful_vars.escape_octal+mkstr(fetch_colour(colour))+";"+mkstr(fetch_format(format))
            return input
        else:
            print("Failed format check")
    else:
        if colour == "reset":
            if fetch_format(format) != False: # Format check
                input = useful_vars.escape_octal+mkstr(fetch_format(format))+";"+mkstr(fetch_colour(colour)) #+useful_vars.escape_octal+
                return input

def colour_txt(format,colour,txt):
    if fetch_colour(colour) != False: # Colour check
        if fetch_format(format) != False: # Format check
            input = useful_vars.escape_octal+mkstr(fetch_colour(colour))+useful_vars.escape_octal+mkstr(fetch_format(format))+mkstr(txt)+format_reset(0)
            return input
        else:
            print("Failed format check")
    else:
        if colour == "reset":
            if fetch_format(format) != False: # Format check
                input = useful_vars.escape_octal+mkstr(fetch_colour(colour))+useful_vars.escape_octal+mkstr(fetch_format(format))+mkstr(txt)+format_reset(0)
                return input

def format_reset(type):
    if type == 0: # Reset all formatting
        return mkstr(useful_vars.escape_octal)+mkstr(fetch_colour("reset"))+mkstr(useful_vars.escape_octal)+(fetch_format("reset"))
    elif type == 1: # Reset colour formatting
        return mkstr(useful_vars.escape_octal)+mkstr(fetch_colour("reset"))
    elif type == 2: # Reset format formatting
        return mkstr(useful_vars.escape_octal)+mkstr(fetch_format("reset"))
    else:
        return mkstr(type)+" isn't a vaild option!\nVaild Options: \n0 - reset all formating\n1 - reset all colour formatting\n2 - reset formatting e.g. bold, underline, italic\nDon't make it a string it must be a int!!"


# shorter short cuts
def fmst(type):
    return format_reset(type)

def fhmt(format):
    return fetch_format(format)

def ftcr(colour):
    return mkstr(fetch_colour(colour))