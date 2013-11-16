### ConsensusTreeVisualizer, a Claremont Colleges Hackathon project.
### Dates: 15-16 November 2013
### Authors: Coline Devin, Benjamin Johnson, Rachel Sherman, Sophia Williams
### School: Harvey Mudd College

### bitstrings.py
### Author: Benjamin Johnson
### A terrible set of functions to perform bitwise operations on python
### strings of 1s and 0s
### Dennis Ritchie is turning in his grave

import random

def SBxor(a, b):
    """Calculates a^b.

    Assumes the input consists of two python strings of the same length
    consisting of 1s and 0s (as charatcers).

    If the strings are of different lengths, the end of the longer string
    will be ignored.
    """
    return ''.join([str(int(a[i])^int(b[i]))
                    for i in range(min(len(a), len(b)))])

def SBnot(a):
    """Calculates ~a.

    Assumes the input consists of a python string consisting of 1s and 0s
    """
    return ''.join(['0' if (ai != '0') else '1' for ai in a])

def SBand(a, b):
    """Calculates a&b.

    Assumes the input consists of two python strings of the same length
    consisting of 1s and 0s (as charatcers).

    If the strings are of different lengths, the end of the longer string
    will be ignored.
    """
    return ''.join([str(int(a[i])&int(b[i]))
                    for i in range(min(len(a), len(b)))])

def SBor(a, b):
    """Calculates a|b.

    Assumes the input consists of two python strings of the same length
    consisting of 1s and 0s (as charatcers).

    If the strings are of different lengths, the end of the longer string
    will be ignored.
    """
    return ''.join([str(int(a[i])|int(b[i]))
                    for i in range(min(len(a), len(b)))])

def SBmatchList(bitstrings):
    """Bitwise; bit x is 1 if all bitstrings in the list have the same
    value in bit x.

    Assumes the input consists of a list of python strings of the same
    length consisting of 1s and 0s (as charatcers).

    If the strings are of different lengths, the end of the longer strings
    will be ignored.
    """
    if len(bitstrings) == 0:
        return ''
    pairwise = [SBnot(SBxor(bitstrings[0], s)) for s in bitstrings]
    anded = reduce(SBand, pairwise)
    return anded

def randomBitstring(length):
    """Gives a random bitstring as a python string of 1s and 0s"""
    return [random.choice(['0','1']) for i in range(length)]
