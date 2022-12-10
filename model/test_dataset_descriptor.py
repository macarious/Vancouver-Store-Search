'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_dataset_descriptor

This file is a unit test for:
dataset_descriptor.py
'''

import unittest
from dataset_descriptor import DatasetDescriptor


class TestDatasetDescriptor(unittest.TestCase):
    '''
    Class: TestDatasetDescriptor
    This class consists of a list of unit tests to test each of the methods
    within the 'DatasetDescriptor' class
    '''
    def setUp(self):
        self.basic_dataset_name = 'Transit Stations'
        self.basic_url = 'https://opendata.vancouver.ca/explore/dataset/rapid-transit-stations/download/?format=csv&timezo=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910'
        self.basic_expected_headers = {'station name' : 'STATION', 'coordinates' : 'Geom', 'local area' : 'Geo Local Area',}
        self.basic_object = DatasetDescriptor(self.basic_dataset_name, self.basic_url, self.basic_expected_headers)


    def test_init_basic(self):
        self.assertEqual(self.basic_object.dataset_name, 'Transit Stations')
        self.assertEqual(self.basic_object.url, 'https://opendata.vancouver.ca/explore/dataset/rapid-transit-stations/download/?format=csv&timezo=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910')
        self.assertEqual(self.basic_object.expected_headers, {'station name' : 'STATION', 'coordinates' : 'Geom', 'local area' : 'Geo Local Area',})
        self.assertEqual(self.basic_object.delimiter, ';')


    def test_init_TypeError(self):
        with self.assertRaises(TypeError):
            test_dataset_name = 1000
            DatasetDescriptor(test_dataset_name, self.basic_url, self.basic_expected_headers)

        with self.assertRaises(TypeError):
            test_url = 2000
            DatasetDescriptor(self.basic_dataset_name, test_url, self.basic_expected_headers)
            
        with self.assertRaises(TypeError):
            test_expected_headers = ['STATION', 'GEOM', 'Geo Local Area']
            DatasetDescriptor(self.basic_dataset_name, self.basic_url, test_expected_headers)
            
        with self.assertRaises(TypeError):
            test_expected_headers = {1 : 'STATION', 2 : 'Geom', 3 : 'Geo Local Area',}
            DatasetDescriptor(self.basic_dataset_name, self.basic_url, test_expected_headers)
            
        with self.assertRaises(TypeError):
            test_expected_headers = {'station name' : 1000, 'coordinates' : 2000, 'local area' : 3000,}
            DatasetDescriptor(self.basic_dataset_name, self.basic_url, test_expected_headers)
            
        with self.assertRaises(TypeError):
            test_delimiter = 1000
            DatasetDescriptor(self.basic_dataset_name, self.basic_url, self.basic_expected_headers, test_delimiter)

    
    def test_str_basic(self):
        self.assertEqual(str(self.basic_object), "Dataset Name: Transit Stations\nURL: https://opendata.vancouver.ca/explore/dataset/rapid-transit-stations/download/?format=csv&timezo=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910\nDelimiter: ;\n")


    def test_str_TypeError(self):
        with self.assertRaises(TypeError):
            self.basic_object.dataset_name = 2000
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.url = 2000
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.delimiter = 2000
            str(self.basic_object)


    def test_eq_True(self):
        other_dataset_name = 'Transit Stations'
        other_url = 'https://opendata.vancouver.ca/explore/dataset/rapid-transit-stations/download/?format=csv&timezo=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910'
        other_expected_headers = {'station name' : 'STATION', 'coordinates' : 'Geom', 'local area' : 'Geo Local Area',}
        other_object = DatasetDescriptor(other_dataset_name, other_url, other_expected_headers)
        self.assertTrue(self.basic_object == other_object)


    def test_eq_False(self):
        other_dataset_name = 'Storefronts'
        other_url = 'https://opendata.vancouver.ca/explore/dataset/storefronts-inventory/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910'
        other_expected_headers = {
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
        other_object = DatasetDescriptor(other_dataset_name, other_url, other_expected_headers)
        self.assertFalse(self.basic_object == other_object)


    def test_eq_TypeError(self):
        other_dataset_name = 'Transit Stations'
        other_url = 'https://opendata.vancouver.ca/explore/dataset/rapid-transit-stations/download/?format=csv&timezo=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910'
        other_expected_headers = {'station name' : 'STATION', 'coordinates' : 'Geom', 'local area' : 'Geo Local Area',}
        other_object = DatasetDescriptor(other_dataset_name, other_url, other_expected_headers)

        with self.assertRaises(TypeError):
            self.basic_object.dataset_name = 2000
            other_object.dataset_name = 'Transit Stations'
            self.basic_object == other_object
        
        with self.assertRaises(TypeError):
            self.basic_object.dataset_name = 'Transit Stations'
            other_object.dataset_name = 2000
            self.basic_object == other_object
        
        with self.assertRaises(TypeError):
            self.basic_object.dataset_name = 2000
            other_object.dataset_name = 2000
            self.basic_object == other_object


# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
