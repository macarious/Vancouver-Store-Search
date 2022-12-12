'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_graphical_user_interface

This file is a unit test for:
graphical_user_interface.py
'''

import unittest
from user_interface.graphical_user_interface import GraphicalUserInterface


class TestGraphicalUserInterface(unittest.TestCase):
    '''
    Class: TestGraphicalUserInterface
    This class consists of a list of unit tests to test the methods from
    the 'GraphicalUserInterface' class. GUI related methods are not tested.
    '''
    def setUp(self):
        # Instantiate a basic 'GraphicalUserInterface'
        self.basic_object = GraphicalUserInterface()        


    def test_init_basic(self):
        self.assertEqual(self.basic_object.name, 'Graphical User Interface')
        self.assertEqual(self.basic_object.user_input, None)
        self.assertEqual(self.basic_object.list_transit_stations, [])
        self.assertEqual(self.basic_object.list_storefronts, [])
        self.assertEqual(self.basic_object.list_local_area_boundaries, [])
        self.assertEqual(self.basic_object.list_station_names, [])
        self.assertEqual(self.basic_object.list_store_categories, [])
        self.assertEqual(self.basic_object.list_nearby_stores, [])


    def test_str_basic(self):
        self.assertEqual(str(self.basic_object), 'Graphical User Interface')


    def test_eq_True(self):
        test_object = self.basic_object
        other_object = GraphicalUserInterface()
        self.assertTrue(test_object == other_object)


    def test_eq_False(self):
        test_object = self.basic_object
        other_object = GraphicalUserInterface()
        other_object.name = 'Not a Graphical User Interface'
        self.assertFalse(test_object == other_object)


    def test_eq_TypeError_1(self):
        test_object = self.basic_object
        other_object = 2000
        with self.assertRaises(TypeError):
            test_object == other_object


    def test_eq_TypeError_2(self):
        test_object = self.basic_object
        other_object = GraphicalUserInterface()
        test_object.name = 2000
        with self.assertRaises(TypeError):
            test_object == other_object

        test_object = self.basic_object
        other_object = GraphicalUserInterface()
        other_object.name = 2000
        with self.assertRaises(TypeError):
            test_object == other_object

        test_object = self.basic_object
        other_object = GraphicalUserInterface()
        test_object.name = 2000
        other_object.name = 2000
        with self.assertRaises(TypeError):
            test_object == other_object


# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
