'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_transit_station_factory

This file is a unit test for:
transit_station_factory.py
'''

import unittest
from model.transit_station_factory import *
from model.dataset_descriptor import DatasetDescriptor
from model.transit_station import TransitStation


class TestTransitStationFactory(unittest.TestCase):
    '''
    Class: TestTransitStationFactory
    This class consists of a list of unit tests to test the functions
    in the transit_station_factory module
    '''
    def setUp(self):
        self.basic_dataset_name = 'Transit Stations'
        self.basic_url = 'https://opendata.vancouver.ca/explore/dataset/rapid-transit-stations/download/?format=csv&timezo=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910'
        self.basic_expected_headers = {'station name' : 'STATION', 'coordinates' : 'Geom', 'local area' : 'Geo Local Area',}
        self.basic_dataset_descriptor_object = DatasetDescriptor(self.basic_dataset_name, self.basic_url, self.basic_expected_headers)

        self.basic_entry_of_data = 'WATERFRONT;"{""type"": ""Point"", ""coordinates"": [491874.0992580385, 5459264.233111048]}";Downtown\r'
        self.basic_header_list = ['STATION', 'Geom', 'Geo Local Area']
        self.basic_transit_station_object = TransitStation('WATERFRONT', (491757.59371811966, 5459218.857871494), 'Downtown')


    def test_create_transit_station_list_from_url_TypeError(self):
        # No basic tests for opening files
        with self.assertRaises(TypeError):
            self.basic_dataset_descriptor_object.url = 2000
            create_transit_station_list_from_url(self.basic_dataset_descriptor_object)


    def test_create_transit_station_from_individual_entry_basic(self):
        test_object = create_transit_station_from_individual_entry(
            entry_of_data = self.basic_entry_of_data,
            header_list = self.basic_header_list,
            dataset_descriptor = self.basic_dataset_descriptor_object
        )
        expected_object = self.basic_transit_station_object
        self.assertEqual(test_object, expected_object)


    def test_create_transit_station_from_individual_entry_TypeError(self):
        with self.assertRaises(TypeError):
            test_entry_of_data = 2000
            create_transit_station_from_individual_entry(
                test_entry_of_data,
                self.basic_header_list,
                self.basic_dataset_descriptor_object
            )

        with self.assertRaises(TypeError):
            test_header_list = 2000
            create_transit_station_from_individual_entry(
                self.basic_entry_of_data,
                test_header_list,
                self.basic_dataset_descriptor_object
            )

        with self.assertRaises(TypeError):
            test_header_list = [1000, 2000, 3000]
            create_transit_station_from_individual_entry(
                self.basic_entry_of_data,
                test_header_list,
                self.basic_dataset_descriptor_object
            )

        with self.assertRaises(TypeError):
            self.basic_dataset_descriptor_object.delimiter = 2000
            create_transit_station_from_individual_entry(
                self.basic_entry_of_data,
                self.basic_header_list,
                self.basic_dataset_descriptor_object
            )

        with self.assertRaises(TypeError):
            self.basic_dataset_descriptor_object.expected_headers = 2000
            create_transit_station_from_individual_entry(
                self.basic_entry_of_data,
                self.basic_header_list,
                self.basic_dataset_descriptor_object
            )


    def test_create_transit_station_from_individual_entry_ValueError(self):
        with self.assertRaises(ValueError):
            test_header_list = []
            create_transit_station_from_individual_entry(
                self.basic_entry_of_data,
                test_header_list,
                self.basic_dataset_descriptor_object
            )


    def test_create_header_list_basic(self):
        test_start_entry_of_data = 'STATION;Geom;Geo Local Area\r'
        test_header_list = create_header_list(test_start_entry_of_data, self.basic_dataset_descriptor_object)
        expected_header_list = ['STATION', 'Geom', 'Geo Local Area']
        self.assertEqual(test_header_list, expected_header_list)


    def test_create_header_list_TypeError(self):
        with self.assertRaises(TypeError):
            test_start_entry_of_data = 2000
            create_header_list(test_start_entry_of_data, self.basic_dataset_descriptor_object)

        with self.assertRaises(TypeError):
            test_start_entry_of_data = 'STATION;Geom;Geo Local Area\r'
            self.basic_dataset_descriptor_object.delimiter = 2000
            create_header_list(test_start_entry_of_data, self.basic_dataset_descriptor_object)


    def test_normalize_station_name_basic(self):
        # Should work whether entry of data requires or not requires cleaning
        test_raw_station_name = 'WATERFRONT'
        test_output = normalize_station_name(test_raw_station_name)
        expected_output = 'WATERFRONT'
        self.assertEqual(test_output, expected_output)
        
        test_raw_station_name = 'LANGARA-\n49th AVE.'
        test_output = normalize_station_name(test_raw_station_name)
        expected_output = 'LANGARA - 49th AVE.'
        self.assertEqual(test_output, expected_output)

        test_raw_station_name = 'YALETOWN-/nROUNDHOUSE'
        test_output = normalize_station_name(test_raw_station_name)
        expected_output = 'YALETOWN - ROUNDHOUSE'
        self.assertEqual(test_output, expected_output)


    def test_normalize_station_name_TypeError(self):
        with self.assertRaises(TypeError):
            test_raw_station_name = 2000
            normalize_station_name(test_raw_station_name)


    def test_extract_coordinates_basic(self):
        # Should work whether entry of data requires or not requires cleaning
        test_coordinates_json = '"{""type"": ""Point"", ""coordinates"": [491874.0992580385, 5459264.233111048]}"'
        test_output = extract_coordinates(test_coordinates_json)
        expected_output = (491874.0992580385, 5459264.233111048)
        self.assertEqual(test_output, expected_output)

        test_coordinates_json = '{"type"": "Point", "coordinates": [491874.0992580385, 5459264.233111048]}'
        test_output = extract_coordinates(test_coordinates_json)
        expected_output = (491874.0992580385, 5459264.233111048)
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
