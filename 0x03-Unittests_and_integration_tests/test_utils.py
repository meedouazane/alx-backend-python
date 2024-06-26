#!/usr/bin/env python3
""" Parameterize a unit test """
import unittest
from utils import (
    access_nested_map,
    get_json,
    memoize
)
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """ test that the method returns what it is supposed to """

    @parameterized.expand([
        ({"a": 1}, 'a', 1),
        ({"a": {"b": 2}}, 'a', {"b": 2}),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test for access nested map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, "a"),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test for access nested map exception """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Mock HTTP calls """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ test for get json """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response) as mock:
            self.assertEqual(get_json(test_url), test_payload)
            mock.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Memoize test class
    """
    def test_memoize(self):
        """ Parameterize and patch """

        class TestClass:
            """ test class for memoize """
            def a_method(self):
                """ a method """
                return 42

            @memoize
            def a_property(self):
                """ a property """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_res:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_res.assert_called_once()


if __name__ == '__main__':
    unittest.main()
