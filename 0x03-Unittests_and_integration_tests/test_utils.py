#!/usr/bin/env python3
"""
Test utils.
task 0, 1, 2 and 3.
"""

from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        tests that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Use the assertRaises context manager to test that a KeyError is
        raised.
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual("KeyError('{}')".format(expected), repr(e.exception))


class TestGetJson(unittest.TestCase):
    """
    TestGetJson
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        test that utils.get_json returns the expected result.
        We don’t want to make any actual external HTTP calls.
        Use unittest.mock.patch to patch requests.get.
        Make sure it returns a Mock object with a
        json method that returns test_payload which you
        parametrize alongside the test_url.
        """
        # The patch() decorator / context manager makes it easy to
        # mock classes or objects in a module under test.
        # The object you specify will be replaced with a mock
        # (or other object) during the test and restored when
        # the test ends
        config = {"return_value.json.return_value": test_payload}
        decorator = patch("requests.get", **config)
        mock = decorator .start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        decorator.stop()


class TestMemoize(unittest.TestCase):
    """
    TestMemoize using utils.memoize decorator.
    """

    def test_memoize(self):
        """
        Test that when calling a_property twice,
        the correct result is returned but a_method
        is only called once using assert_called_once.
        """

        class TestClass:
            """
            given class.
            """

            def a_method(self):
                """
                a method.
                """
                return 42

            @memoize
            def a_property(self):
                """
                a proprety.
                """
                return self.a_method()

        with patch.object(TestClass, "a_method") as m:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            m.assert_called_once()
