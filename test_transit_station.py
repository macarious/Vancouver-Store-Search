'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_transit_station

This file is a unit test for:
transit_station.py
'''

import unittest
from model.transit_station import TransitStation


class TestTransitStation(unittest.TestCase):
    '''
    Class: TestTransitStation
    This class consists of a list of unit tests to test each of the methods
    within the 'TransitStation' class
    '''
    def setUp(self):
        self.basic_name = 'WATERFRONT'
        self.basic_coordinates = (491757.59371811966, 5459218.857871494)
        self.basic_local_area = 'Downtown'
        self.basic_object = TransitStation(self.basic_name, self.basic_coordinates, self.basic_local_area)


    def test_init_basic(self):
        self.assertEqual(self.basic_object.station_name, 'WATERFRONT')
        self.assertEqual(self.basic_object.coordinates, (491757.59371811966, 5459218.857871494))
        self.assertEqual(self.basic_object.local_area, 'Downtown')


    def test_init_TypeError(self):
        with self.assertRaises(TypeError):
            test_name = 1000
            TransitStation(test_name, self.basic_coordinates, self.basic_local_area)

        with self.assertRaises(TypeError):
            test_coordinates = [1.0, 2.0]
            TransitStation(self.basic_name, test_coordinates, self.basic_local_area)
            
        with self.assertRaises(TypeError):
            test_local_area = 1000
            TransitStation(self.basic_name, self.basic_coordinates, test_local_area)


    def test_init_ValueError(self):
        with self.assertRaises(ValueError):
            test_coordinates = ()
            TransitStation(self.basic_name, test_coordinates, self.basic_local_area)

        with self.assertRaises(ValueError):
            test_coordinates = (1.0, 2.0, 3.0)
            TransitStation(self.basic_name, test_coordinates, self.basic_local_area)

        with self.assertRaises(ValueError):
            test_coordinates = (1.0, 'Two')
            TransitStation(self.basic_name, test_coordinates, self.basic_local_area)

        with self.assertRaises(ValueError):
            test_coordinates = ('One', 'Two')
            TransitStation(self.basic_name, test_coordinates, self.basic_local_area)

    
    def test_str_basic(self):
        self.assertEqual(str(self.basic_object), "Name: WATERFRONT\nCoordinates: (491757.59371811966, 5459218.857871494)\nLocal Area: Downtown\n")


    def test_str_TypeError(self):
        with self.assertRaises(TypeError):
            self.basic_object.station_name = 1000
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.coordinates = [1.0, 2.0]
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.local_area = 1000
            str(self.basic_object)

    
    def test_str_ValueError(self):
        with self.assertRaises(ValueError):
            self.basic_object.coordinates = ()
            str(self.basic_object)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = (1.0, 2.0, 3.0)
            str(self.basic_object)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = (1.0, 'Two')
            str(self.basic_object)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = ('One', 'Two')
            str(self.basic_object)


    def test_eq_True(self):
        other_name = 'WATERFRONT'
        other_coordinates = (491757.59371811966, 5459218.857871494)
        other_local_area = 'Downtown'
        other_object = TransitStation(other_name, other_coordinates, other_local_area)
        self.assertTrue(self.basic_object == other_object)


    def test_eq_False(self):
        other_name = 'MARINE DRIVE'
        other_coordinates = (491473.12822691567, 5450757.244252066)
        other_local_area = 'Marpole'
        other_object = TransitStation(other_name, other_coordinates, other_local_area)
        self.assertFalse(self.basic_object == other_object)


    def test_eq_TypeError(self):
        with self.assertRaises(TypeError):
            other_object = 2000
            self.basic_object == other_object
            
        other_name = 'MARINE DRIVE'
        other_coordinates = (491473.12822691567, 5450757.244252066)
        other_local_area = 'Marpole'
        other_object = TransitStation(other_name, other_coordinates, other_local_area)

        with self.assertRaises(TypeError):
            self.basic_object.station_name = 2000
            other_object.station_name = 'MARINE DRIVE'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.station_name = 'WATERFRONT'
            other_object.station_name = 2000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.station_name = 2000
            other_object.station_name = 2000
            self.basic_object == other_object


    def test_calculate_distance_to_basic(self):
        destination_coordinates = (491828.5353999988, 5459317.5562)
        self.assertAlmostEqual(self.basic_object.calculate_distance_to(destination_coordinates), 121.54868274791987)


    def test_calculate_distance_to_TyperError(self):
        with self.assertRaises(TypeError):
            self.basic_object.coordinates = 2000
            destination_coordinates = (491473.12822691567, 5450757.244252066)
            self.basic_object.calculate_distance_to(destination_coordinates)

        with self.assertRaises(TypeError):
            self.basic_object.coordinates = (491828.5353999988, 5459317.5562)
            destination_coordinates = 2000
            self.basic_object.calculate_distance_to(destination_coordinates)


    def test_calculate_distance_to_ValueError(self):
        with self.assertRaises(ValueError):
            self.basic_object.coordinates = (1.0, 'Two')
            destination_coordinates = (491473.12822691567, 5450757.244252066)
            self.basic_object.calculate_distance_to(destination_coordinates)

            self.basic_object.coordinates = ('One', 'Two')
            destination_coordinates = (491473.12822691567, 5450757.244252066)
            self.basic_object.calculate_distance_to(destination_coordinates)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = ()
            destination_coordinates = (491473.12822691567, 5450757.244252066)
            self.basic_object.calculate_distance_to(destination_coordinates)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = (1.0, 2.0, 3.0)
            destination_coordinates = (491473.12822691567, 5450757.244252066)
            self.basic_object.calculate_distance_to(destination_coordinates)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = (491828.5353999988, 5459317.5562)
            destination_coordinates = (1.0, 'Two')
            self.basic_object.calculate_distance_to(destination_coordinates)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = (491828.5353999988, 5459317.5562)
            destination_coordinates = ('One', 'Two')
            self.basic_object.calculate_distance_to(destination_coordinates)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = (491828.5353999988, 5459317.5562)
            destination_coordinates = ()
            self.basic_object.calculate_distance_to(destination_coordinates)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = (491828.5353999988, 5459317.5562)
            destination_coordinates = (1.0, 2.0, 3.0)
            self.basic_object.calculate_distance_to(destination_coordinates)


# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
