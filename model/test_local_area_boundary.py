'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_local_area_boundary

This file is a unit test for:
local_area_boundary.py
'''

import unittest
from local_area_boundary import LocalAreaBoundary


class TestLocalAreaBoundary(unittest.TestCase):
    '''
    Class: TestLocalAreaBoundary
    This class consists of a list of unit tests to test each of the methods
    within the 'LocalAreaBoundary' class
    '''
    def setUp(self):
        self.basic_abbreviation = 'OAK'
        self.basic_name = 'Oakridge'
        self.basic_list_boundary_coordinates = [(492310.70745902986, 5453376.091043321), (492269.0509910676, 5451793.061679327), (489794.0144154225, 5451845.011054722), (489837.64126147685, 5453508.59546255), (490678.46469729935, 5453466.396391663), (492310.70745902986, 5453376.091043321)]
        self.basic_centroid_coordinates = (5452631.7289951695, 491042.52665588236)
        self.basic_object = LocalAreaBoundary(
            self.basic_abbreviation,
            self.basic_name,
            self.basic_list_boundary_coordinates,
            self.basic_centroid_coordinates
            )


    def test_init_basic(self):
        self.assertEqual(self.basic_object.abbreviation, 'OAK')
        self.assertEqual(self.basic_object.name, 'Oakridge')
        self.assertEqual(self.basic_object.list_boundary_coordinates, [(492310.70745902986, 5453376.091043321), (492269.0509910676, 5451793.061679327), (489794.0144154225, 5451845.011054722), (489837.64126147685, 5453508.59546255), (490678.46469729935, 5453466.396391663), (492310.70745902986, 5453376.091043321)])
        self.assertEqual(self.basic_object.centroid_coordinates, (5452631.7289951695, 491042.52665588236))


    def test_init_TypeError(self):
        with self.assertRaises(TypeError):
            test_abbreviation = 2000
            self.basic_object = LocalAreaBoundary(
                test_abbreviation,
                self.basic_name,
                self.basic_list_boundary_coordinates,
                self.basic_centroid_coordinates
                )

        with self.assertRaises(TypeError):
            test_name = 2000
            self.basic_object = LocalAreaBoundary(
                self.basic_abbreviation,
                test_name,
                self.basic_list_boundary_coordinates,
                self.basic_centroid_coordinates
                )

        with self.assertRaises(TypeError):
            test_list_boundary_coordinates = ((492310.70745902986, 5453376.091043321), (492269.0509910676, 5451793.061679327), (489794.0144154225, 5451845.011054722), (489837.64126147685, 5453508.59546255), (490678.46469729935, 5453466.396391663), (492310.70745902986, 5453376.091043321))
            self.basic_object = LocalAreaBoundary(
                self.basic_abbreviation,
                self.basic_name,
                test_list_boundary_coordinates,
                self.basic_centroid_coordinates
                )

        with self.assertRaises(TypeError):
            test_centroid_coordinates = [5452631.7289951695, 491042.52665588236]
            self.basic_object = LocalAreaBoundary(
                self.basic_abbreviation,
                self.basic_name,
                self.basic_list_boundary_coordinates,
                test_centroid_coordinates
                )


    def test_init_ValueError(self):
        with self.assertRaises(ValueError):
            test_list_boundary_coordinates = []
            self.basic_object = LocalAreaBoundary(
                self.basic_abbreviation,
                self.basic_name,
                test_list_boundary_coordinates,
                self.basic_centroid_coordinates
                )


    def test_init_ValueError(self):
        with self.assertRaises(ValueError):
            test_list_boundary_coordinates = [set(), set(), set()]
            self.basic_object = LocalAreaBoundary(
                self.basic_abbreviation,
                self.basic_name,
                test_list_boundary_coordinates,
                self.basic_centroid_coordinates
                )

        with self.assertRaises(ValueError):
            test_centroid_coordinates = ()
            self.basic_object = LocalAreaBoundary(
                self.basic_abbreviation,
                self.basic_name,
                self.basic_list_boundary_coordinates,
                test_centroid_coordinates
                )

        with self.assertRaises(ValueError):
            test_centroid_coordinates = (1.0, 2.0, 3.0)
            self.basic_object = LocalAreaBoundary(
                self.basic_abbreviation,
                self.basic_name,
                self.basic_list_boundary_coordinates,
                test_centroid_coordinates
                )

        with self.assertRaises(ValueError):
            test_centroid_coordinates = (1.0, 'Two')
            self.basic_object = LocalAreaBoundary(
                self.basic_abbreviation,
                self.basic_name,
                self.basic_list_boundary_coordinates,
                test_centroid_coordinates
                )

        with self.assertRaises(ValueError):
            test_centroid_coordinates = ('One', 'Two')
            self.basic_object = LocalAreaBoundary(
                self.basic_abbreviation,
                self.basic_name,
                self.basic_list_boundary_coordinates,
                test_centroid_coordinates
                )

    
    def test_str_basic(self):
        self.assertEqual(str(self.basic_object), "Abbreviation: OAK\nName: Oakridge\nCoordinates of Centroid: (5452631.7289951695, 491042.52665588236)\n")


    def test_str_TypeError(self):
        with self.assertRaises(TypeError):
            self.basic_object.abbreviation = 2000
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.name = 2000
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.centroid_coordinates = [5452631.7289951695, 491042.52665588236]
            str(self.basic_object)

    
    def test_str_ValueError(self):
        with self.assertRaises(ValueError):
            self.basic_object.centroid_coordinates = ()
            str(self.basic_object)

        with self.assertRaises(ValueError):
            self.basic_object.centroid_coordinates = (1.0, 2.0, 3.0)
            str(self.basic_object)

        with self.assertRaises(ValueError):
            self.basic_object.centroid_coordinates = (1.0, 'Two')
            str(self.basic_object)

        with self.assertRaises(ValueError):
            self.basic_object.centroid_coordinates = ('One', 'Two')
            str(self.basic_object)


    def test_eq_True(self):
        other_abbreviation = 'OAK'
        other_name = 'Oakridge'
        other_list_boundary_coordinates = [(492310.70745902986, 5453376.091043321), (492269.0509910676, 5451793.061679327), (489794.0144154225, 5451845.011054722), (489837.64126147685, 5453508.59546255), (490678.46469729935, 5453466.396391663), (492310.70745902986, 5453376.091043321)]
        other_centroid_coordinates = (5452631.7289951695, 491042.52665588236)
        other_object = LocalAreaBoundary(
            other_abbreviation,
            other_name,
            other_list_boundary_coordinates,
            other_centroid_coordinates,
            )
        self.assertTrue(self.basic_object == other_object)


    def test_eq_False(self):
        other_abbreviation = 'GW'
        other_name = 'Grandview-Woodland'
        other_list_boundary_coordinates = [(494399.4616453806, 5459725.039424128), (495071.2898342053, 5459708.280744998), (495446.2721377341, 5459644.768848708), (495460.81964618707, 5459793.6101129325), (495892.65275480703, 5460083.7676818995), (495882.8355803871, 5456602.905781702), (494363.54977730464, 5456622.063910625), (494367.75457073154, 5456933.75961796), (494399.4616453806, 5459725.039424128)]
        other_centroid_coordinates = (5458189.142341714,495146.3975207777)
        other_object = LocalAreaBoundary(
            other_abbreviation,
            other_name,
            other_list_boundary_coordinates,
            other_centroid_coordinates,
            )
        self.assertFalse(self.basic_object == other_object)


    def test_eq_TypeError(self):
        other_abbreviation = 'GW'
        other_name = 'Grandview-Woodland'
        other_list_boundary_coordinates = [(494399.4616453806, 5459725.039424128), (495071.2898342053, 5459708.280744998), (495446.2721377341, 5459644.768848708), (495460.81964618707, 5459793.6101129325), (495892.65275480703, 5460083.7676818995), (495882.8355803871, 5456602.905781702), (494363.54977730464, 5456622.063910625), (494367.75457073154, 5456933.75961796), (494399.4616453806, 5459725.039424128)]
        other_centroid_coordinates = (5458189.142341714,495146.3975207777)
        other_object = LocalAreaBoundary(
            other_abbreviation,
            other_name,
            other_list_boundary_coordinates,
            other_centroid_coordinates,
            )

        with self.assertRaises(TypeError):
            self.basic_object.name = 2000
            other_object.name = 'Grandview-Woodland'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.name = 'Oakridge'
            other_object.name = 2000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.name = 2000
            other_object.name = 2000
            self.basic_object == other_object

# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
