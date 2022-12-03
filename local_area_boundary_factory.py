'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Module Name -- local_area_boundary

This file contains functions that create 'LocalAreaBoundary' objects.

This file is used by the driver file:
graphical_user_interface.py
'''

# Modules
import dataset_downloader
import json


# Classes
from model.local_area_boundary import LocalAreaBoundary


COORDINATES_SEPARATOR = ','


def create_local_area_boundary_list_from_url(dataset_descriptor):
    '''
    Function Name: create_local_area_boundary_list_from_url
        Create a list of 'LocalAreaBoundary' objects from a url containg a text
        file with multiple rows, where each row contains data separated by
        delimiters
    
    Parameters:
        url -- str, URL for accessing the dataset online
        dataset_descriptor -- DatasetDescriptor, object containing properties
            relating to a dataset
    
    Raises:
        TypeError -- raises if the attribute 'url' of class 'DatasetDescriptor is not a string
        TypeError -- raises if the attribute 'delimiter' of class 'DatasetDescriptor is not a string
    
    Returns:
    '''
    if type(dataset_descriptor.url) is not str:
        raise TypeError("TypeError: The attribute 'url' of class 'DatasetDescriptor must be a string")

    if type(dataset_descriptor.delimiter) is not str:
        raise TypeError("TypeError: The attribute 'delimiter' of class 'DatasetDescriptor must be a string")

    response_text = dataset_downloader.read_url(dataset_descriptor.url)
    response_text_row = response_text.split('\n')

    # First extract header list from 0th row
    header_list = create_header_list(response_text_row[0], dataset_descriptor)
    local_area_boundary_list = []

    # Instantiate LocalAreaBoundary objects from 1st row onward
    for i in range(1, len(response_text_row)):
        if response_text_row[i] != '': # Skip empty rows; there exists an empty final row if the dataset ends with a new-line character
            local_area_boundary_list.append(create_local_area_boundary_from_row(response_text_row[i], header_list, dataset_descriptor))

    return local_area_boundary_list


def create_local_area_boundary_from_row(row_text, header_list, dataset_descriptor):
    '''
    Function Name: create_local_area_boundary_from_row
        Instantiates a 'LocalAreaBoundary' by reading data from a row of text
        separated by delimiters
    
    Parameters:
        row_text -- str, row of text, which contains data separated by delimiters
        header_list -- str, list of headers, read from the first row of text
        dataset_descriptor -- DatasetDescriptor, object containing properties
            relating to a dataset
    
    Raises:
        TypeError -- raises if the parameter 'row_text' is not a string
        TypeError -- raises if the parameter 'header_list' is not a list
        ValueError -- raises if the parameter 'header_list' is an empty list
        TypeError -- raises if the parameter 'header_list' does not contain elements of type string
        TypeError -- raises if the attribute 'delimiter' of class 'DatasetDescriptor' is not a string
        TypeError -- raises if the attribute 'expected_header' of class 'DatasetDescriptor' is not a dictionary
    
    Returns:
        LocalAreaBoundary, object representing a local area boundary
    '''
    if type(row_text) is not str:
        raise TypeError("TypeError: The parameter 'row_text' must be a string")

    if type(header_list) is not list:
        raise TypeError("TypeError: The parameter 'header_list' must be a list")

    if len(header_list) == 0:
        raise ValueError("ValueError: The parameter 'header_list' cannot be empty")

    if not all(type(value) is str for value in header_list):
        raise TypeError("TypeError: The parameter 'header_list' must contain elements of type string")

    if type(dataset_descriptor.delimiter) is not str:
        raise TypeError("TypeError: The attribute 'delimiter' of class 'DatasetDescriptor' must be a string")

    if type(dataset_descriptor.expected_headers) is not dict:
        raise TypeError("TypeError: The attribute 'expected_headers' of class 'DatasetDescriptor' must be a dictionary")

    row_text_list = row_text.strip().split(dataset_descriptor.delimiter)

    abbreviation = None
    name = None
    list_boundary_coordinates = None
    centroid_coordinates = None

    # Map each data into the correct object attributes matching the correct column index
    for i in range(len(row_text_list)):
        if i == header_list.index(dataset_descriptor.expected_headers['abbreviation']):
            abbreviation = row_text_list[i]

        elif i == header_list.index(dataset_descriptor.expected_headers['local area']):
            name = row_text_list[i]

        elif i == header_list.index(dataset_descriptor.expected_headers['area coordinates']):
            list_boundary_coordinates = extract_coordinates(row_text_list[i])

        elif i == header_list.index(dataset_descriptor.expected_headers['centroid coordinates']):
            # 2D x and y coordinates in dataset are in reversed order
            centroid_coordinates = map(float, row_text_list[i].split(COORDINATES_SEPARATOR)[::-1])
            centroid_coordinates = tuple(centroid_coordinates)

    return LocalAreaBoundary(abbreviation, name, list_boundary_coordinates, centroid_coordinates)


def create_header_list(start_row_text, dataset_descriptor):
    '''
    Function Name: create_header_list
        Creates a list of headers from a text of row separated by delimiters
    
    Parameters:
        start_row_text -- str, the first row of text, which contains the headers
        dataset_descriptor -- DatasetDescriptor, object containing dataset properies
    
    Raises:
        TypeError -- raises if the parameter 'start_row_text' is not a string
        TypeError -- raises if the attribute 'delimiter' of class 'DatasetDescriptor' is not a string
    
    Returns:
        list of str, list of headers
    '''
    if type(start_row_text) is not str:
        raise TypeError("TypeError: The parameter 'start_row_text' must be a string")
    
    if type(dataset_descriptor.delimiter) is not str:
        raise TypeError("TypeError: The attribute 'delimiter' of class 'DatasetDescriptor must be a string")
    
    header_list = start_row_text.strip().split(dataset_descriptor.delimiter)
    return header_list

        
def extract_coordinates(coordinates_json):
    '''
    Function Name: extract_coordinates
        Extract coordinates from the json format data read from the text file
    
    Parameters:
        raw_station_name -- str, coordinates data read from text file
    
    Raises:
        TypeError -- raises if parameter 'coordinates_json' is not a string
    
    Returns:
        tuple of (float, float), coordinates extracted from raw coordinates data
    '''
    if type(coordinates_json) is not str:
        raise TypeError("TypeError: The parameter 'coordinates_json' must be a string")

    # Remove extra double-quotations (added when reading the data with requests) from raw data
    # and deserialize the json-format string to a dictionary
    coordinates_dictionary = json.loads(coordinates_json.replace('""', '"').strip('"'))
    list_coordinates = []
    for coordinates in coordinates_dictionary['coordinates'][0]:
        list_coordinates.append(tuple(coordinates))

    return list_coordinates




    