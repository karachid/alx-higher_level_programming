#!/usr/bin/python3
"""
Definess the function "write_file"
"""


def write_file(filename="", text=""):
    """Returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
