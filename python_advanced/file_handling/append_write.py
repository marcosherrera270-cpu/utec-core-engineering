#!/usr/bin/env python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 file and return characters added."""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
