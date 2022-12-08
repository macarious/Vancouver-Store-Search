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
import model.dataset_downloader as dataset_downloader
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
        if response_text_row[i] != '': # Skip empty rows
            local_area_boundary_object = create_local_area_boundary_from_individual_entry(response_text_row[i], header_list, dataset_descriptor)
            local_area_boundary_list.append(local_area_boundary_object)

    return local_area_boundary_list


def create_local_area_boundary_from_individual_entry(data_entry, header_list, dataset_descriptor):
    '''
    Function Name: create_local_area_boundary_from_individual_entry
        Instantiates a 'LocalAreaBoundary' by reading data from a row of text
        separated by delimiters
    
    Parameters:
        data_entry -- str, row of text, which contains data separated by delimiters
        header_list -- str, list of headers, read from the first row of text
        dataset_descriptor -- DatasetDescriptor, object containing properties
            relating to a dataset
    
    Raises:
        TypeError -- raises if the parameter 'data_entry' is not a string
        TypeError -- raises if the parameter 'header_list' is not a list
        ValueError -- raises if the parameter 'header_list' is an empty list
        TypeError -- raises if the parameter 'header_list' does not contain elements of type string
        TypeError -- raises if the attribute 'delimiter' of class 'DatasetDescriptor' is not a string
        TypeError -- raises if the attribute 'expected_header' of class 'DatasetDescriptor' is not a dictionary
    
    Returns:
        LocalAreaBoundary, object representing a local area boundary
    '''
    if type(data_entry) is not str:
        raise TypeError("TypeError: The parameter 'data_entry' must be a string")

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

    data_entry_list = data_entry.strip().split(dataset_descriptor.delimiter)

    abbreviation = None
    name = None
    list_boundary_coordinates = None
    centroid_coordinates = None

    # Map each data into the correct object attributes matching the correct column index
    for i in range(len(data_entry_list)):
        if i == header_list.index(dataset_descriptor.expected_headers['abbreviation']):
            abbreviation = data_entry_list[i]

        elif i == header_list.index(dataset_descriptor.expected_headers['local area']):
            name = data_entry_list[i]

        elif i == header_list.index(dataset_descriptor.expected_headers['area coordinates']):
            list_boundary_coordinates = extract_coordinates(data_entry_list[i])

        elif i == header_list.index(dataset_descriptor.expected_headers['centroid coordinates']):
            # x- and y-coordinates in dataset are in reversed order; needs to be reversed
            centroid_coordinates = map(float, data_entry_list[i].split(COORDINATES_SEPARATOR)[::-1])
            centroid_coordinates = tuple(centroid_coordinates)

    return LocalAreaBoundary(abbreviation, name, list_boundary_coordinates, centroid_coordinates)


def create_header_list(start_data_entry, dataset_descriptor):
    '''
    Function Name: create_header_list
        Creates a list of headers from a text of row separated by delimiters
    
    Parameters:
        start_data_entry -- str, the first row of text, which contains the headers
        dataset_descriptor -- DatasetDescriptor, object containing dataset properies
    
    Raises:
        TypeError -- raises if the parameter 'start_data_entry' is not a string
        TypeError -- raises if the attribute 'delimiter' of class 'DatasetDescriptor' is not a string
    
    Returns:
        list of str, list of headers
    '''
    if type(start_data_entry) is not str:
        raise TypeError("TypeError: The parameter 'start_data_entry' must be a string")
    
    if type(dataset_descriptor.delimiter) is not str:
        raise TypeError("TypeError: The attribute 'delimiter' of class 'DatasetDescriptor must be a string")
    
    header_list = start_data_entry.strip().split(dataset_descriptor.delimiter)
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




    
