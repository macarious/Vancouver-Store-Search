'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Module Name -- dataset_table_printer

This file contains functions which creates 'DataFrame' objects. They are
displayed using the 'print' functions. They are used in the terminal
interface.

This file is used in the following file:
terminal_interface.py
'''

# Modules
import pandas


DISTANCE_UNIT = 'm'
HEADER_LINE_SYMBOL = '-'
HEADER_LIST_TRANSIT_STATION = [
    'Station Name',
    'Coordinates',
    'Local Area',
    ]
HEADER_LIST_STOREFRONT = [
    'Store ID',
    'Business Name',
    'Address',
    'Retail Category',
    'Coordinates',
    'Local Area',
    ]
HEADER_LIST_NEARBY_STORE = [
    'Store Name',
    'Distance',
    'Address',
    'Retail Category',
    ]


def create_dataframe_transit_station(list_objects):
    '''
    Function Name: create_dataframe_transit_station
        Creates a 'DataFrame' object from a list of transit stations
    
    Parameters:
        list_objects -- list of TransitStation, list of 'TransitStation' objects
    
    Raises:
        TypeError -- raises if the parameter 'TransitStation' is not a list
    
    Returns:
        DataFrame, 'DataFrame' object used for dispaly
    '''
    if type(list_objects) is not list:
        raise TypeError("TypeError: The parameter 'list_objects' must be a list")
    
    data_list = []
    column_count = len(HEADER_LIST_TRANSIT_STATION)
    for i in range(column_count):
        data_list.append([])

    for object in list_objects:
        row_content = [
            object.station_name,
            object.coordinates,
            object.local_area,
            ]

        for j in range(column_count):
            data_list[j].append(row_content[j])     

    return pandas.DataFrame(dict(zip(HEADER_LIST_TRANSIT_STATION, data_list)))


def create_dataframe_storefront(list_objects):
    '''
    Function Name: create_dataframe_storefront
        Creates a 'DataFrame' object from a list of storefront
    
    Parameters:
        list_objects -- list of Storefront, list of 'Storefront' objects
    
    Raises:
        TypeError -- raises if the parameter 'Storefront' is not a list
    
    Returns:
        DataFrame, 'DataFrame' object used for dispaly
    '''
    if type(list_objects) is not list:
        raise TypeError("TypeError: The parameter 'list_objects' must be a list")
    
    data_list = []
    column_count = len(HEADER_LIST_STOREFRONT)
    for i in range(column_count):
        data_list.append([])

    for object in list_objects:
        row_content = [
            object.store_id,
            object.business_name,
            object.full_address,
            object.retail_category,
            object.coordinates,
            object.local_area,
            ]

        for j in range(column_count):
            data_list[j].append(row_content[j])     

    return pandas.DataFrame(dict(zip(HEADER_LIST_STOREFRONT, data_list)))


def create_dataframe_nearby_store(list_objects):
    '''
    Function Name: create_dataframe_nearby_store
        Creates a 'DataFrame' object from a list of nearby stores
    
    Parameters:
        list_objects -- list of NearbyStore, list of 'NearbyStore' objects
    
    Raises:
        TypeError -- raises if the parameter 'NearbyStore' is not a list
    
    Returns:
        DataFrame, 'DataFrame' object used for dispaly
    '''
    if type(list_objects) is not list:
        raise TypeError("TypeError: The parameter 'list_objects' must be a list")
    
    data_list = []
    column_count = len(HEADER_LIST_NEARBY_STORE)
    for i in range(column_count):
        data_list.append([])

    for object in list_objects:
        row_content = [
            object.storefront.business_name,
            "{:.0f}".format(object.distance) + ' ' + DISTANCE_UNIT,
            object.storefront.full_address,
            object.storefront.retail_category
        ]
    
        for j in range(column_count):
            data_list[j].append(row_content[j])

    dataframe = pandas.DataFrame(dict(zip(HEADER_LIST_NEARBY_STORE, data_list)))
    dataframe.index += 1 # Index to be displayed will start at 1 instead of 0
    
    return dataframe


def print_transit_station(list_objects):
    '''
    Function Name: print_transit_station
        Print a list of transit stations utilizing 'DataFrame' objects
    
    Parameters:
        list_objects -- list of TransitStation, list of 'TransitStation' objects
    
    Raises:
        TypeError -- raises if the parameter 'TransitStation' is not a list
    
    Returns:
        None
    '''
    if type(list_objects) is not list:
        raise TypeError("TypeError: The parameter 'list_objects' must be a list")
    
    print_title('List of Transit Stations')
    if len(list_objects) == 0:
        print('There are no Transit Stations to display')
    else:
        print(create_dataframe_transit_station(list_objects), '\n')


def print_storefront(list_objects):
    '''
    Function Name: print_storefront
        Print a list of storefronts utilizing 'DataFrame' objects
    
    Parameters:
        list_objects -- list of Storefront, list of 'Storefront' objects
    
    Raises:
        TypeError -- raises if the parameter 'list_objects' is not a list
    
    Returns:
        None
    '''
    if type(list_objects) is not list:
        raise TypeError("TypeError: The parameter 'list_objects' must be a list")

    print_title('List of Storefronts')
    if len(list_objects) == 0:
        print('There are no Storefronts to display')
    else:
        print(create_dataframe_storefront(list_objects), '\n')


def print_nearby_store(list_objects, row_count):
    '''
    Function Name: print_nearby_store
        Print a list of nearby stores utilizing 'DataFrame' objects
    
    Parameters:
        list_objects -- list of NearbyStore, list of 'NearbyStore' objects
        row_count -- int, the number of rows to display in the table
    
    Raises:
        TypeError -- raises if the parameter 'list_objects' is not a list
        TypeError -- raises if the parameter 'row_count' is not an integer
    
    Returns:
        None
    '''
    if type(list_objects) is not list:
        raise TypeError("TypeError: The parameter 'list_objects' must be a list")
    
    if type(row_count) is not int:
        raise TypeError("TypeError: The parameter 'row_count' must be an integer")

    print_title('List of Nearby Stores')
    if len(list_objects) == 0:
        print("There are no results to display. Try adjusting your search radius.")
    else:
        pandas.set_option('display.max_rows', None) # Prevents table rows from being truncated
        print(create_dataframe_nearby_store(list_objects).head(row_count), '\n')


def print_title(title):
    '''
    Function Name: print_title
        Print a title
    
    Parameters:
        title -- str, title to be pritned
    
    Raises:
        TypeError -- raises if the parameter 'title' is not a string
    
    Returns:
        None
    '''
    if type(title) is not str:
        raise TypeError("TypeError: The parameter 'title' must be a string")
    
    print(HEADER_LINE_SYMBOL * len(title) + '\n' + title + '\n' + HEADER_LINE_SYMBOL * len(title))