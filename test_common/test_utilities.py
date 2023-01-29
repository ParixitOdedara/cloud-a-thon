import unittest
import logging
from common.utilities import Utilities

utils = Utilities()
logging.basicConfig(level=logging.INFO)


class MyTestCase(unittest.TestCase):

    def test_01_fetch_value_from_nested_obj(self):
        logging.info("Test test_01_fetch_value_from_nested_obj")

        obj = {"a": {"b": {"c": "d"}}}
        key = 'a/b/c'
        expected_val = 'd'

        out = utils.fetch_value_from_nested_obj(obj, key)
        logging.info("Obj: {}, Key: {}, Extracted value: '{}'".format(obj, key, out))
        self.assertEqual(expected_val, out)

    def test_02_fetch_value_from_nested_obj(self):
        logging.info("Test test_02_fetch_value_from_nested_obj")

        obj = {"a": {"b": {"c": "d"}, "b1": {"c1": {"d1": {"e1": "hello"}}}}}
        key = 'a/b1/c1/d1/e1'
        expected_val = 'hello'

        out = utils.fetch_value_from_nested_obj(obj, key)
        logging.info("Obj: {}, Key: {}, Extracted value: '{}'".format(obj, key, out))
        self.assertEqual(expected_val, out)

    def test_03_fetch_value_from_nested_obj(self):
        logging.info("Test test_03_fetch_value_from_nested_obj")

        obj = {"a": {"b": {"c": "d"}}}
        key = 'fake_key'
        expected_val = ''

        out = utils.fetch_value_from_nested_obj(obj, key)
        logging.info("Obj: {}, Key: {}, Extracted value: '{}'".format(obj, key, out))
        self.assertEqual(expected_val, out)


if __name__ == '__main__':
    unittest.main()
