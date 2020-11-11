# import all the relative packages
from bread_factory import NaanFactory
import unittest
import pytest

# create a class to test the  methods
class test_factory(unittest.TestCase):
    factory = NaanFactory()

    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough('water', 'flour'), 'dough')
        self.assertEqual(self.factory.make_dough('water', 'egg'), 'Both water and flour is needed')

    def test_bake_dough(self):
        self.assertEqual(self.factory.bake_bread('Yes'), 'naan')
        self.assertEqual(self.factory.bake_bread('no'), 'make the dough')

    def test_run_factory(self):
        self.assertEqual(self.factory.run_factory(True), 'factory is ready to run')
        self.assertEqual(self.factory.run_factory(False), 'bake the naan')
