'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Module Name -- nearby_stores_finder

This file contains functions that uses 'Storefront' and 'TransitStation'
objects and create a sorted list of all nearby stores around a specified
transit station. The list contains 'NearbyStore' objects. Store category
and search radius are also used to filter the list of nearby stores.

These functions are used by the driver file:
data_dashboard.py
'''


COORDINATE_COUNT = 2 # Coordinates are represented by 2 values


from model.nearby_store import NearbyStore


VACANT_LABELS = ['Vacant', 'Vacant UC', 'Unknown']


def find_nearby_stores(input, list_storefront):
    '''
    Function Name: find_nearby_stores
        Finds all nearby stores around a transit station and creates a list of
        'NearbyStore' objects from a list of 'Storefront' objects
    
    Parameters:
        input -- dict, input from users (keys are input name; values are user input)
        list_storefront -- list of Storefront, list of 'Storefront' objects
    
    Raises:
        TypeError -- raises if the attribute 'station_name' of class 'TransitStation' is not a string
        TypeError -- raises if the attribute 'coordinates' of class 'TransitStation' is not a tuple
        ValueError -- raises if the attribute 'coordinates' of class 'TransitStation' does not contain exactly 2 floats
        TypeError -- raises if the parameter 'list_storefront' is not a list
        ValueError -- raises if the parameter 'list_storefront' is an empty list
    
    Returns:
        list of NearbyStore, list of sorted and filtered 'NearbyStore' objects
    '''
    if type(input.transit_station.station_name) is not str:
         raise TypeError("TypeError: The attribute 'station_name' from 'TransitStation' object must be a string")
    
    if type(input.transit_station.coordinates) is not tuple:
        raise TypeError("TypeError: The attribute 'coordinates' of class 'TransitStation' must be a tuple")

    if (len(input.transit_station.coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in input.transit_station.coordinates)):
        raise ValueError("ValueError: The attribute 'coordinates' of class 'TransitStation' must contain exactly 2 floats")

    if type(list_storefront) is not list:
         raise TypeError("TypeError: The parameter 'list_storefront' must be a list")
    
    if len(list_storefront) == 0:
        raise ValueError("ValueError: The parameter 'list_storefront' must not be empty")

    list_nearby_stores = []
    filtered_list_storefront = filter_stores_by_category(list_storefront, input.store_category)
    for store in filtered_list_storefront:
        distance = input.transit_station.calculate_distance_to(store.coordinates) # Calculate distance using a TransitStation method
        list_nearby_stores.append(NearbyStore(store, input.transit_station, distance, input.store_category))

    list_nearby_stores = sort_stores_by_distance(list_nearby_stores)
    list_nearby_stores = remove_duplicated_stores(list_nearby_stores)
    list_nearby_stores = filter_stores_by_search_radius(list_nearby_stores, input.search_radius)
    
    return list_nearby_stores
    

def filter_stores_by_category(list_storefront, store_category):
    '''
    Function Name: filter_stores_by_category
        Filters the list of 'Storefront' objects by a specified store category
    
    Parameters:
        list_storefront -- list of Storefront, list of 'Storefront' objects
        store_category -- str, store category used for filtering
    
    Raises:
        TypeError -- raises if the parameter 'list_storefront' is not a list
        ValueError -- raises if the parameter 'list_storefront' is empty
        TypeError -- raises if the parameter 'store_category' is not a string
    
    Returns:
        list of Storefront, list of filtered 'Storefront' objects
    '''
    if type(list_storefront) is not list:
         raise TypeError("TypeError: The parameter 'list_storefront' must be a list")
    
    if len(list_storefront) == 0:
        raise ValueError("ValueError: The parameter 'list_storefront' must not be empty")
    
    if type(store_category) is not str:
        raise TypeError("TypeError: The parameter 'store_category' must be a string")
    
    if store_category == 'All':
        return filter(lambda storefront: storefront.retail_category not in VACANT_LABELS, list_storefront)
    
    return filter(lambda storefront: storefront.retail_category == store_category, list_storefront)


def filter_stores_by_search_radius(list_nearby_stores, search_radius):
    '''
    Function Name: filter_stores_by_search_radius
        Filters the list of 'NearbyStore' objects by a specified search radius
    
    Parameters:
        list_nearby_stores -- list of nearby stores, list of 'NearbyStore' objects
        search_radius -- float, search radius used for filtering
    
    Raises:
        TypeError -- raises if the parameter 'list_nearby_stores' is not a list
        ValueError -- raises if the parameter 'list_nearby_stores' is an empty list
        TypeError -- raises if the parameter 'search_radius' is not a float
    
    Returns:
        list of NearbyStore, list of filtered 'NearbyStore' objects
    '''
    if type(list_nearby_stores) is not list:
         raise TypeError("TypeError: The parameter 'list_nearby_stores' must be a list")
    
    if len(list_nearby_stores) == 0:
        raise ValueError("ValueError: The parameter 'list_storefront' must not be empty")
    
    if type(search_radius) is not float:
        raise TypeError("TypeError: The parameter 'search_radius' must be a float")

    if search_radius == 0: # Returns unfiltered list
        return list_nearby_stores

    index = 0
    while index < len(list_nearby_stores):
        store_distance = list_nearby_stores[index].distance
        if store_distance > search_radius:
            list_nearby_stores.pop(index)
        else:
            index +=1 # Increment index only if no entry is removed
    
    return list_nearby_stores


def sort_stores_by_distance(list_nearby_stores):
    '''
    Function Name: sort_stores_by_distance
        Sorts a list of 'NearbyStore' objects by distance (in ascending order)

    Parameters:
        list_nearby_stores -- list of nearby stores, list of 'NearbyStore' objects
    
    Raises:
        TypeError -- raises if the parameter 'list_nearby_stores' is not a list
        ValueError -- raises if the parameter 'list_nearby_stores' is an empty list
    
    Returns:
        list of NearbyStore, list of filtered 'NearbyStore' objects
    '''
    if type(list_nearby_stores) is not list:
        raise TypeError("TypeError: The parameter 'list_nearby_stores' must be a list")
    
    if len(list_nearby_stores) == 0:
        raise ValueError("ValueError: The parameter 'list_storefront' must not be empty")
    
    return sorted(list_nearby_stores, key = lambda nearby_store: nearby_store.distance)


def remove_duplicated_stores(list_nearby_stores):
    '''
    Function Name: remove_duplicated_stores
        Remove duplicated stores in the list of nearby stores
    
    Parameters:
        list_nearby_stores -- list of nearby stores, list of 'NearbyStore' objects
        ValueError -- raises if the parameter 'list_nearby_stores' is an empty list

    Raises:
        TypeError -- raises if the parameter 'list_nearby_stores' is not a list
    
    Returns:
        list of NearbyStore, list of filtered 'NearbyStore' objects
    '''
    if type(list_nearby_stores) is not list:
        raise TypeError("TypeError: The parameter 'list_nearby_stores' must be a list")
    
    if len(list_nearby_stores) == 0:
        raise ValueError("ValueError: The parameter 'list_storefront' must not be empty")
    
    unique_store_name = set()
    index = 0
    while index < len(list_nearby_stores):
        business_name = list_nearby_stores[index].storefront.business_name
        if business_name not in unique_store_name:
            unique_store_name.add(business_name)
            index += 1 # Increment index only if no entry is removed
        else:
            list_nearby_stores.pop(index)
    
    return list_nearby_stores


