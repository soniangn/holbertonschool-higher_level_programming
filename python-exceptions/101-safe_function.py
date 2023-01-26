#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError) as err:
        sys.stderr.write("Exception: {}".format(err))
        return None
