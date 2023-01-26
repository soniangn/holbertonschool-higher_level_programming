#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as err:
        sys.stderr.write("Exception: {}".format(err))
    except IndexError as err2:
        sys.stderr.write("Exception: {}".format(err2))
        return None
