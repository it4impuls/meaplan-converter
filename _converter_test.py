""" Module. """
import os
import logging
import unittest
from _converter import Converter
from _exceptions import MenuReaderException


class TestMenuConverter(unittest.TestCase):

    def test_object_created(self):
        with self.assertRaises(MenuReaderException):
            obj = Converter("table_with_right_condition_and_not_all_fields_set.pdf")


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
    unittest.main()
