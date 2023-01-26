#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
