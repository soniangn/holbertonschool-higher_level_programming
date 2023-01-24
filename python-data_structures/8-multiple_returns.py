#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return_tup = (len(sentence), None)
    else:
        return_tup = (len(sentence), sentence[0])
    return return_tup
