'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_dataset_downloader

This file is a unit test for:
dataset_downloader.py
'''

import unittest
from model.dataset_downloader import *


class TestDatasetDownloader(unittest.TestCase):
    '''
    Class: TestDatasetDownloader
    This class consists of a list of unit tests to test the functions
    in the dataset_downloader module
    '''
    def setUp(self):
        pass


    def test_read_url_basic(self):
        # Opening files not tested
        test_url = 'https://opendata.vancouver.ca/explore/dataset/rapid-transit-stations/download/?format=csv&timezo=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910'
        test_output = read_url(test_url)

        # Instead, check output's type; ensure it's a string
        self.assertTrue(type(test_output), str)


    def test_read_url_TypeError(self):
        test_url = 9000
        with self.assertRaises(TypeError):
            read_url(test_url)

        test_url = True
        with self.assertRaises(TypeError):
            read_url(test_url)


    def test_read_url_HTTPError(self):
        # Connection-related errors not tested
        pass


    def test_read_url_ConnectionError(self):
        # Connection-related errors not tested
        pass


    def test_read_url_TooManyRedirects(self):
        # Connection-related errors not tested
        pass


    def test_read_url_Timeout(self):
        # Connection-related errors not tested
        pass


# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
