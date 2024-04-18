#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
import typing


def safely_get_value(dct: typing.Mapping[typing.Any, typing.Any],
                     key: typing.Any,
                     default: typing.Optional[typing.Any] = None) -> typing.Any:
    if key in dct:
        return dct[key]
    else:
        return default
