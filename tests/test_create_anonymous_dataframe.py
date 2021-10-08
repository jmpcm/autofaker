import unittest

from pyautodata import Autodata


class StaffTests(unittest.TestCase):

    def test_create_pandas_dataframe_returns_not_none(self):
        pdf = Autodata.create_pandas_dataframe(SimpleClass)
        print(pdf)
        self.assertIsNotNone(pdf)


class SimpleClass:
    id = 123
    text = 'test'
