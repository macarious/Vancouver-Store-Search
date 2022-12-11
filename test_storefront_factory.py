'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_storefront_factory

This file is a unit test for:
storefront_factory.py
'''

import unittest
from model.storefront_factory import *
from model.dataset_descriptor import DatasetDescriptor
from model.storefront import Storefront


class TestStorefrontFactory(unittest.TestCase):
    '''
    Class: TestStorefrontFactory
    This class consists of a list of unit tests to test the functions
    in the storefront_factory module
    '''
    def setUp(self):
        self.basic_dataset_name = 'Storefronts'
        self.basic_url = 'https://opendata.vancouver.ca/explore/dataset/storefronts-inventory/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910'
        self.basic_expected_headers = {
            'store id' : 'ID',
            'address unit' : 'Unit',
            'address number' : 'Civic number - Parcel',
            'address street' : 'Street name - Parcel',
            'business name' : 'Business name',
            'retail category': 'Retail category',
            'year recorded' : 'Year recorded',
            'local area' : 'Geo Local Area',
            'coordinates' : 'Geom',
            'coorindates alt' : 'geo_point_2d',
        }
        self.basic_dataset_descriptor_object = DatasetDescriptor(self.basic_dataset_name, self.basic_url, self.basic_expected_headers)

        self.basic_entry_of_data = '1983;N/A;1997;CORNWALL AV;Circle K;Convenience Goods;2020;Kitsilano;"{""type"": ""Point"", ""coordinates"": [489101.79599999916, 5457780.51]}";5457780.51,489101.79599999916\r'
        self.basic_header_list = ['ID', 'Unit', 'Civic number - Parcel', 'Street name - Parcel', 'Business name', 'Retail category', 'Year recorded', 'Geo Local Area', 'Geom', 'geo_point_2d']
        self.basic_storefront_object = Storefront(
            store_id = 1983,
            business_name = 'Circle K',
            address_unit = 'N/A',
            address_number = 1997,
            address_street = 'CORNWALL AV',
            retail_category = 'Convenience Goods',
            coordinates = (489101.79599999916, 5457780.51),
            local_area = 'Kitsilano',
        )


    def test_create_storefront_list_from_url_TypeError(self):
        # No basic tests for opening files
        with self.assertRaises(TypeError):
            self.basic_dataset_descriptor_object.url = 2000
            create_storefront_list_from_url(self.basic_dataset_descriptor_object)


    def test_create_storefront_from_individual_entry_basic(self):
        test_object = create_storefront_from_individual_entry(
            entry_of_data = self.basic_entry_of_data,
            header_list = self.basic_header_list,
            dataset_descriptor = self.basic_dataset_descriptor_object
        )
        expected_object = self.basic_storefront_object
        self.assertEqual(test_object, expected_object)


    def test_create_storefront_from_individual_entry_TypeError(self):
        with self.assertRaises(TypeError):
            test_entry_of_data = 2000
            create_storefront_from_individual_entry(
                test_entry_of_data,
                self.basic_header_list,
                self.basic_dataset_descriptor_object,
            )

        with self.assertRaises(TypeError):
            test_header_list = 2000
            create_storefront_from_individual_entry(
                self.basic_entry_of_data,
                test_header_list,
                self.basic_dataset_descriptor_object,
            )

        with self.assertRaises(TypeError):
            test_header_list = [1000, 2000, 3000]
            create_storefront_from_individual_entry(
                self.basic_entry_of_data,
                test_header_list,
                self.basic_dataset_descriptor_object,
            )

        with self.assertRaises(TypeError):
            self.basic_dataset_descriptor_object.delimiter = 2000
            create_storefront_from_individual_entry(
                self.basic_entry_of_data,
                self.basic_header_list,
                self.basic_dataset_descriptor_object,
            )

        with self.assertRaises(TypeError):
            self.basic_dataset_descriptor_object.expected_headers = [
                'ID',
                'Unit',
                'Civic number - Parcel',
                'Street name - Parcel',
                'Business name',
                'Retail category',
                'Year recorded',
                'Geo Local Area',
                'Geom',
                'geo_point_2d',
            ]
            create_storefront_from_individual_entry(
                self.basic_entry_of_data,
                self.basic_header_list,
                self.basic_dataset_descriptor_object,
            )


    def test_create_storefront_from_individual_entry_ValueError(self):
        with self.assertRaises(ValueError):
            test_header_list = []
            create_storefront_from_individual_entry(
                self.basic_entry_of_data,
                test_header_list,
                self.basic_dataset_descriptor_object,
            )


    def test_create_header_list_basic(self):
        test_start_entry_of_data = 'ID;Unit;Civic number - Parcel;Street name - Parcel;Business name;Retail category;Year recorded;Geo Local Area;Geom;geo_point_2d\r'
        test_header_list = create_header_list(test_start_entry_of_data, self.basic_dataset_descriptor_object)
        expected_header_list = ['ID', 'Unit', 'Civic number - Parcel', 'Street name - Parcel', 'Business name', 'Retail category', 'Year recorded', 'Geo Local Area', 'Geom', 'geo_point_2d']
        self.assertEqual(test_header_list, expected_header_list)


    def test_create_header_list_TypeError(self):
        with self.assertRaises(TypeError):
            test_start_entry_of_data = 2000
            create_header_list(test_start_entry_of_data, self.basic_dataset_descriptor_object)

        with self.assertRaises(TypeError):
            test_start_entry_of_data = 'ID;Unit;Civic number - Parcel;Street name - Parcel;Business name;Retail category;Year recorded;Geo Local Area;Geom;geo_point_2d\r'
            self.basic_dataset_descriptor_object.delimiter = 2000
            create_header_list(test_start_entry_of_data, self.basic_dataset_descriptor_object)


    def test_extract_coordinates_basic(self):
        # Should work whether entry of data requires or not requires cleaning
        test_coordinates_json = '"{""type"": ""Point"", ""coordinates"": [489101.79599999916, 5457780.51]}"'
        test_output = extract_coordinates(test_coordinates_json)
        expected_output = (489101.79599999916, 5457780.51)
        self.assertEqual(test_output, expected_output)

        test_coordinates_json = '{"type"": "Point", "coordinates": [489101.79599999916, 5457780.51]}'
        test_output = extract_coordinates(test_coordinates_json)
        expected_output = (489101.79599999916, 5457780.51)
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
