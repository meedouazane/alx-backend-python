#!/usr/bin/env python3
""" Parameterize a unit test """
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ test that the method returns what it is supposed to """

    @parameterized.expand([
        ({"a": 1}, 'a', 1),
        ({"a": {"b": 2}}, 'a', {"b": 2}),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_nested(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
