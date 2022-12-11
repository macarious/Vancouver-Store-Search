'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_user_input

This file is a unit test for:
user_input.py
'''

import unittest
from model.transit_station import TransitStation
from user_interface.user_input import UserInput


class TestUserInput(unittest.TestCase):
    '''
    Class: TestUserInput
    This class consists of a list of unit tests to test each of the methods
    within the 'UserInput' class
    '''
    def setUp(self):
        self.basic_object = UserInput()

        # Instantiate a basic 'TransitStation'
        self.basic_station_name = 'WATERFRONT'
        self.basic_coordinates = (491757.59371811966, 5459218.857871494)
        self.basic_local_area = 'Downtown'
        self.basic_object.transit_station = TransitStation(self.basic_station_name, self.basic_coordinates, self.basic_local_area)
        
        self.basic_object.store_category = 'All'
        self.basic_object.search_radius = 500.00000
        self.basic_object.max_display_count = 50


    def test_init_basic(self):
        test_object = UserInput()
        self.assertEqual(test_object.name, 'User Input')
        self.assertEqual(test_object.transit_station, None)
        self.assertEqual(test_object.store_category, 'All')
        self.assertEqual(test_object.search_radius, 0.0)
        self.assertEqual(test_object.max_display_count, 50)

    
    def test_str_basic(self):
        self.assertEqual(str(self.basic_object), "User Input\nTransit Station: WATERFRONT\nStore Category: All\nSearch Radius: 500.0\nMax Display: 50\n")


    def test_str_TypeError(self):
        with self.assertRaises(TypeError):
            self.basic_object.name = 1000
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.transit_station.station_name = 1000
            str(self.basic_object)
            
        with self.assertRaises(TypeError):
            self.basic_object.store_category = 1000
            str(self.basic_object)
            
        with self.assertRaises(TypeError):
            self.basic_object.search_radius = 'zero'
            str(self.basic_object)
            
        with self.assertRaises(TypeError):
            self.basic_object.max_display_count = 'Fifty'
            str(self.basic_object)

    
    def test_str_ValueError(self):
        with self.assertRaises(ValueError):
            self.basic_object.transit_station = None
            str(self.basic_object)


    def test_eq_True(self):
        other_object = UserInput()
        other_station_name = 'WATERFRONT'
        other_coordinates = (491757.59371811966, 5459218.857871494)
        other_local_area = 'Downtown'
        other_object.transit_station = TransitStation(other_station_name, other_coordinates, other_local_area)
        other_object.store_category = 'All'
        other_object.search_radius = 500.00000
        other_object.max_display_count = 50
        self.basic_object == other_object


    def test_eq_False(self):
        other_object = UserInput()
        other_station_name = 'MARINE DRIVE'
        other_coordinates = (491473.12822691567, 5450757.244252066)
        other_local_area = 'Marpole'
        other_object.transit_station = TransitStation(other_station_name, other_coordinates, other_local_area)
        other_object.store_category = 'All'
        other_object.search_radius = 500.00000
        other_object.max_display_count = 50
        self.basic_object == other_object

        other_object = UserInput()
        other_station_name = 'WATERFRONT'
        other_coordinates = (491757.59371811966, 5459218.857871494)
        other_local_area = 'Downtown'
        other_object.transit_station = TransitStation(other_station_name, other_coordinates, other_local_area)
        other_object.store_category = 'Food & Beverage'
        other_object.search_radius = 500.00000
        other_object.max_display_count = 50
        self.basic_object == other_object

        other_object = UserInput()
        other_station_name = 'WATERFRONT'
        other_coordinates = (491757.59371811966, 5459218.857871494)
        other_local_area = 'Downtown'
        other_object.transit_station = TransitStation(other_station_name, other_coordinates, other_local_area)
        other_object.store_category = 'All'
        other_object.search_radius = 1000.00000
        other_object.max_display_count = 50
        self.basic_object == other_object

        other_object = UserInput()
        other_station_name = 'WATERFRONT'
        other_coordinates = (491757.59371811966, 5459218.857871494)
        other_local_area = 'Downtown'
        other_object.transit_station = TransitStation(other_station_name, other_coordinates, other_local_area)
        other_object.store_category = 'All'
        other_object.search_radius = 500.00000
        other_object.max_display_count = 100
        self.basic_object == other_object

        other_object = UserInput()
        other_station_name = 'MARINE DRIVE'
        other_coordinates = (491473.12822691567, 5450757.244252066)
        other_local_area = 'Marpole'
        other_object.transit_station = TransitStation(other_station_name, other_coordinates, other_local_area)
        other_object.store_category = 'Food & Beverage'
        other_object.search_radius = 1000.00000
        other_object.max_display_count = 100
        self.basic_object == other_object


    def test_eq_TypeError(self):
        with self.assertRaises(TypeError):
            other_object = 2000
            self.basic_object == other_object
            
        other_object = UserInput()
        other_station_name = 'MARINE DRIVE'
        other_coordinates = (491473.12822691567, 5450757.244252066)
        other_local_area = 'Marpole'
        other_object.transit_station = TransitStation(other_station_name, other_coordinates, other_local_area)
        other_object.store_category = 'Food & Beverage'
        other_object.search_radius = 1000.00000
        other_object.max_display_count = 100

        with self.assertRaises(TypeError):
            self.basic_object.name = 2000
            other_object.name = 'User Input'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.name = 'User Input'
            other_object.name = 2000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.name = 2000
            other_object.name = 2000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.transit_station.station_name = 2000
            other_object.transit_station.station_name = 'MARPOLE'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.transit_station.station_name = 'WATERFRONT'
            other_object.transit_station.station_name = 2000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.transit_station.station_name = 2000
            other_object.transit_station.station_name = 2000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.store_category = 2000
            other_object.store_category = 'Food & Beverage'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.store_category = 'All'
            other_object.store_category = 2000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.store_category = 2000
            other_object.store_category = 2000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.search_radius = 'Five hundred'
            other_object.search_radius = 1000.00000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.search_radius = 500.00000
            other_object.search_radius = 'One thousand'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.search_radius = 'Five hundred'
            other_object.search_radius = 'One thousand'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.max_display_count = 'Fifty'
            other_object.max_display_count = 100
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.max_display_count = 50
            other_object.max_display_count = 'One hundred'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.max_display_count = 'Fifty'
            other_object.max_display_count = 'One hundred'
            self.basic_object == other_object


# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
