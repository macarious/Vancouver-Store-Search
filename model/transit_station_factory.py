'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Module Name -- transit_station_factory

This file contains functions that create 'TransitStation' objects.

This file is used by the driver file:
graphical_user_interface.py
'''

# Modules
import model.dataset_downloader as dataset_downloader
import json
import re


# Classes
from model.transit_station import TransitStation


# Regex pattern replace the unnecessary '\n' and '/n' characters with one white space
NAME_REGEX_SUBSTITUTE_1 = {'pattern' : '([/\\\]n)', 'replacement' : ' '}
# Regex pattern to provide consistent spacing before and after '-'
NAME_REGEX_SUBSTITUTE_2 = {'pattern' : '(\s*-\s*)', 'replacement' : ' - '}


def create_transit_station_list_from_url(dataset_descriptor):
    '''
    Function Name: create_transit_station_list_from_url
        Create a list of 'TransitStation' objects from a url containg a text
        file with multiple rows, where each row contains data separated by
        delimiters
    
    Parameters:
        dataset_descriptor -- DatasetDescriptor, object containing properties
            relating to a dataset
    
    Raises:
        TypeError -- raises if the attribute 'url' of class 'DatasetDescriptor is not a string
    
    Returns:
    '''
    if type(dataset_descriptor.url) is not str:
        raise TypeError("TypeError: The attribute 'url' of class 'DatasetDescriptor must be a string")

    response_text = dataset_downloader.read_url(dataset_descriptor.url)
    response_text_row = response_text.split('\n')

    # First extract header list from 0th row
    header_list = create_header_list(response_text_row[0], dataset_descriptor)
    
    transit_station_list = []
    # Instantiate TransitStation objects from 1st row onward
    for i in range(1, len(response_text_row)):
        if response_text_row[i] != '': # Skip empty rows
            transit_station_object = create_transit_station_from_individual_entry(response_text_row[i], header_list, dataset_descriptor)
            transit_station_list.append(transit_station_object)

    return transit_station_list


def create_transit_station_from_individual_entry(entry_of_data, header_list, dataset_descriptor):
    '''
    Function Name: create_transit_station_from_individual_entry
        Instantiates a 'TransitStation' by reading data from a row of text
        separated by delimiters
    
    Parameters:
        entry_of_data -- str, row of text, which contains data separated by delimiters
        header_list -- str, list of headers, read from the first row of text
        dataset_descriptor -- DatasetDescriptor, object containing properties
            relating to a dataset
    
    Raises:
        TypeError -- raises if the parameter 'entry_of_data' is not a string
        TypeError -- raises if the parameter 'header_list' is not a list
        ValueError -- raises if the parameter 'header_list' is an empty list
        TypeError -- raises if the parameter 'header_list' does not contain elements of type string
        TypeError -- raises if the attribute 'delimiter' of class 'DatasetDescriptor' is not a string
        TypeError -- raises if the attribute 'expected_header' of class 'DatasetDescriptor' is not a dictionary
    
    Returns:
        TransitStation, object representing a transit station
    '''
    if type(entry_of_data) is not str:
        raise TypeError("TypeError: The parameter 'entry_of_data' must be a string")

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

    entry_of_data_list = entry_of_data.strip().split(dataset_descriptor.delimiter)

    name = None
    coordinates = None
    local_area = None

    # Map each data into the correct object attributes matching the correct column index
    for i in range(len(entry_of_data_list)):
        if i == header_list.index(dataset_descriptor.expected_headers['station name']):
            name = normalize_station_name(entry_of_data_list[i])

        elif i == header_list.index(dataset_descriptor.expected_headers['coordinates']):
            coordinates = extract_coordinates(entry_of_data_list[i])

        elif i == header_list.index(dataset_descriptor.expected_headers['local area']):
            local_area = entry_of_data_list[i]

    return TransitStation(name, coordinates, local_area)


def create_header_list(start_entry_of_data, dataset_descriptor):
    '''
    Function Name: create_header_list
        Creates a list of headers from a text of row separated by delimiters
    
    Parameters:
        start_entry_of_data -- str, the first row of text, which contains the headers
        dataset_descriptor -- DatasetDescriptor, object containing dataset properies
    
    Raises:
        TypeError -- raises if the parameter 'start_entry_of_data' is not a string
        TypeError -- raises if the attribute 'delimiter' of class 'DatasetDescriptor' is not a string
    
    Returns:
        list of str, list of headers
    '''
    if type(start_entry_of_data) is not str:
        raise TypeError("TypeError: The parameter 'start_entry_of_data' must be a string")
    
    if type(dataset_descriptor.delimiter) is not str:
        raise TypeError("TypeError: The attribute 'delimiter' of class 'DatasetDescriptor must be a string")
    
    header_list = start_entry_of_data.strip().split(dataset_descriptor.delimiter)
    return header_list


def normalize_station_name(raw_station_name):
    '''
    Function Name: normalize_station_name
        Normalizes station name data by removing unnecessary characters and providing
        consistent spacing before and after '-'s
    
    Parameters:
        raw_station_name -- str, station name read from text file
    
    Raises:
        TypeError -- raises if parameter 'raw_station_name' is not a string
    
    Returns:
        str, normalized station name
    '''
    if type(raw_station_name) is not str:
        raise TypeError("TypeError: The parameter 'raw_station_name' must be a string")
    
    temp_station_name = re.sub(NAME_REGEX_SUBSTITUTE_1['pattern'], NAME_REGEX_SUBSTITUTE_1['replacement'], raw_station_name)
    return re.sub(NAME_REGEX_SUBSTITUTE_2['pattern'], NAME_REGEX_SUBSTITUTE_2['replacement'], temp_station_name)

        
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
    coordinates_json_cleaned = coordinates_json.replace('""', '"').strip('"')
    coordinates_dictionary = json.loads(coordinates_json_cleaned)

    return tuple(coordinates_dictionary['coordinates'])




    
