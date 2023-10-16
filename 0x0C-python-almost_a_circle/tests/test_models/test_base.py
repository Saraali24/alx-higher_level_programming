#!/usr/bin/python3
import unittest
from models.base import Base


class BaseTestCases(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    def test_nb_obj(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)
