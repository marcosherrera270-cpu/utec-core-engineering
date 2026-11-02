#!/usr/bin/env python3
"""Defines the Square class."""

Square = __import__('1-square').Square


class Square(Square):
    """Represent a square."""

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
