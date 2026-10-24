#!/usr/bin/env python3
"""Module for writing text to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 file and return the number of characters."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
