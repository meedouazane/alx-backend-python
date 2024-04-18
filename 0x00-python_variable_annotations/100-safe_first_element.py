#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
import typing
from typing import Sequence, Optional


def safe_first_element(lst: Sequence[typing.Any]) -> Optional[typing.Any]:
    """ Duck typing - first element of a sequence """
    if lst:
        return lst[0]
    else:
        return None
