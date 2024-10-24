#!/usr/bin/python3
def multiple_returns(sentence):
    if  sentence:
        s_length = len(sentence)
        f_letter = sentence[0]
    else:
        s_length = 0
        f_letter = None

    return tuple((s_length, f_letter))

