#!/usr/bin/env python3
""" Let's duck type an iterable object """
import typing
from typing import Tuple


def element_length(lst: typing.Iterable[typing.Sequence]) ->\
        Tuple[typing.Sequence, int]:
    """function’s parameters and return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
