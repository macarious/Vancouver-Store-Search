'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_local_area_boundary_factory

This file is a unit test for:
local_area_boundary_factory.py
'''

import unittest
from model.local_area_boundary_factory import *
from model.dataset_descriptor import DatasetDescriptor
from model.local_area_boundary import LocalAreaBoundary


class TestLocalAreaBoundaryFactory(unittest.TestCase):
    '''
    Class: TestLocalAreaBoundaryFactory
    This class consists of a list of unit tests to test the functions
    in the local_area_boundary_factory module
    '''
    def setUp(self):
        self.basic_dataset_name = 'Local Area Boundary'
        self.basic_url = 'https://opendata.vancouver.ca/explore/dataset/local-area-boundary/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910'
        self.basic_expected_headers = {
            'abbreviation' : 'MAPID',
            'local area' : 'Name',
            'area coordinates' : 'Geom',
            'centroid coordinates' : 'geo_point_2d',
        }
        self.basic_dataset_descriptor_object = DatasetDescriptor(self.basic_dataset_name, self.basic_url, self.basic_expected_headers)

        self.basic_entry_of_data = 'OAK;Oakridge;"{""type"": ""Polygon"", ""coordinates"": [[[492310.70745902986, 5453376.091043321], [492269.0509910676, 5451793.061679327], [489794.0144154225, 5451845.011054722], [489837.64126147685, 5453508.59546255], [490678.46469729935, 5453466.396391663], [492310.70745902986, 5453376.091043321]]]}";5452631.7289951695,491042.52665588236\r'
        self.basic_header_list = ['MAPID', 'Name', 'Geom', 'geo_point_2d']
        self.basic_local_area_boundary_object = LocalAreaBoundary(
            abbreviation = 'OAK',
            name = 'Oakridge',
            list_boundary_coordinates = [(492310.70745902986, 5453376.091043321), (492269.0509910676, 5451793.061679327), (489794.0144154225, 5451845.011054722), (489837.64126147685, 5453508.59546255), (490678.46469729935, 5453466.396391663), (492310.70745902986, 5453376.091043321)],
            centroid_coordinates = (491042.52665588236, 5452631.7289951695),
        )


    def test_create_local_area_boundary_list_from_url_TypeError(self):
        # No basic tests for opening files
        with self.assertRaises(TypeError):
            self.basic_dataset_descriptor_object.url = 2000
            create_local_area_boundary_list_from_url(self.basic_dataset_descriptor_object)


    def test_create_local_area_boundary_from_individual_entry_basic(self):
        test_object = create_local_area_boundary_from_individual_entry(
            entry_of_data = self.basic_entry_of_data,
            header_list = self.basic_header_list,
            dataset_descriptor = self.basic_dataset_descriptor_object
        )
        expected_object = self.basic_local_area_boundary_object
        self.assertEqual(test_object, expected_object)


    def test_create_local_area_boundary_from_individual_entry_TypeError(self):
        with self.assertRaises(TypeError):
            test_entry_of_data = 2000
            create_local_area_boundary_from_individual_entry(
                test_entry_of_data,
                self.basic_header_list,
                self.basic_dataset_descriptor_object,
            )

        with self.assertRaises(TypeError):
            test_header_list = 2000
            create_local_area_boundary_from_individual_entry(
                self.basic_entry_of_data,
                test_header_list,
                self.basic_dataset_descriptor_object,
            )

        with self.assertRaises(TypeError):
            test_header_list = [1000, 2000, 3000]
            create_local_area_boundary_from_individual_entry(
                self.basic_entry_of_data,
                test_header_list,
                self.basic_dataset_descriptor_object,
            )

        with self.assertRaises(TypeError):
            self.basic_dataset_descriptor_object.delimiter = 2000
            create_local_area_boundary_from_individual_entry(
                self.basic_entry_of_data,
                self.basic_header_list,
                self.basic_dataset_descriptor_object,
            )

        with self.assertRaises(TypeError):
            self.basic_dataset_descriptor_object.expected_headers = [
                'MAPID',
                'Name',
                'Geom',
                'geo_point_2d',
            ]
            create_local_area_boundary_from_individual_entry(
                self.basic_entry_of_data,
                self.basic_header_list,
                self.basic_dataset_descriptor_object,
            )


    def test_create_local_area_boundary_from_individual_entry_ValueError(self):
        with self.assertRaises(ValueError):
            test_header_list = []
            create_local_area_boundary_from_individual_entry(
                self.basic_entry_of_data,
                test_header_list,
                self.basic_dataset_descriptor_object,
            )


    def test_create_header_list_basic(self):
        test_start_entry_of_data = 'MAPID;Name;Geom;geo_point_2d\r'
        test_header_list = create_header_list(test_start_entry_of_data, self.basic_dataset_descriptor_object)
        expected_header_list = ['MAPID', 'Name', 'Geom', 'geo_point_2d']
        self.assertEqual(test_header_list, expected_header_list)


    def test_create_header_list_TypeError(self):
        with self.assertRaises(TypeError):
            test_start_entry_of_data = 2000
            create_header_list(test_start_entry_of_data, self.basic_dataset_descriptor_object)

        with self.assertRaises(TypeError):
            test_start_entry_of_data = 'OAK;Oakridge;"{""type"": ""Polygon"", ""coordinates"": [[[492310.70745902986, 5453376.091043321], [492269.0509910676, 5451793.061679327], [489794.0144154225, 5451845.011054722], [489837.64126147685, 5453508.59546255], [490678.46469729935, 5453466.396391663], [492310.70745902986, 5453376.091043321]]]}";5452631.7289951695,491042.52665588236\r'
            self.basic_dataset_descriptor_object.delimiter = 2000
            create_header_list(test_start_entry_of_data, self.basic_dataset_descriptor_object)


    def test_extract_coordinates_basic(self):
        # Should work whether entry of data requires or not requires cleaning
        test_coordinates_json = '"{""type"": ""Polygon"", ""coordinates"": [[[492310.70745902986, 5453376.091043321], [492269.0509910676, 5451793.061679327], [489794.0144154225, 5451845.011054722], [489837.64126147685, 5453508.59546255], [490678.46469729935, 5453466.396391663], [492310.70745902986, 5453376.091043321]]]}"'
        test_output = extract_coordinates(test_coordinates_json)
        expected_output = [(492310.70745902986, 5453376.091043321), (492269.0509910676, 5451793.061679327), (489794.0144154225, 5451845.011054722), (489837.64126147685, 5453508.59546255), (490678.46469729935, 5453466.396391663), (492310.70745902986, 5453376.091043321)]
        self.assertEqual(test_output, expected_output)

        test_coordinates_json = '{"type": "Polygon", "coordinates": [[[492310.70745902986, 5453376.091043321], [492269.0509910676, 5451793.061679327], [489794.0144154225, 5451845.011054722], [489837.64126147685, 5453508.59546255], [490678.46469729935, 5453466.396391663], [492310.70745902986, 5453376.091043321]]]}'
        test_output = extract_coordinates(test_coordinates_json)
        expected_output = [(492310.70745902986, 5453376.091043321), (492269.0509910676, 5451793.061679327), (489794.0144154225, 5451845.011054722), (489837.64126147685, 5453508.59546255), (490678.46469729935, 5453466.396391663), (492310.70745902986, 5453376.091043321)]
        self.assertEqual(test_output, expected_output)


    def test_extract_coordinates_TypeError(self):
        with self.assertRaises(TypeError):
            test_coordinates_json = 2000
            extract_coordinates(test_coordinates_json)


# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
