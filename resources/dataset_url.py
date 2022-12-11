'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Module Name -- dataset_url

This program contains the parameters of each dataset. The paremeters
are used to instantiate 'DatasetDescriptor' and they are used to
download and process the dataset.

This file is used by the file:
graphical_user_interface.py
'''

# Rapid Transit Stations of Vancouver
TRANSIT_STATIONS_DATASET = {
    'dataset_name' : 'Transit Stations',
    'url' : 'https://opendata.vancouver.ca/explore/dataset/rapid-transit-stations/download/?format=csv&timezo=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910',
    'expected_headers' : {
        'station name' : 'STATION',
        'coordinates' : 'Geom',
        'local area' : 'Geo Local Area',
    }
}


# Storefronts Inventory of Vancouver
STOREFRONTS_DATASET = {
    'dataset_name' : 'Storefronts',
    'url' : 'https://opendata.vancouver.ca/explore/dataset/storefronts-inventory/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910',
    'expected_headers' : {
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
}


# Local Area Boundary
LOCAL_AREA_BOUNDARY = {
    'dataset_name' : 'Local Area Boundary',
    'url' : 'https://opendata.vancouver.ca/explore/dataset/local-area-boundary/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910',
    'expected_headers' : {
        'abbreviation' : 'MAPID',
        'local area' : 'Name',
        'area coordinates' : 'Geom',
        'centroid coordinates' : 'geo_point_2d',
    }
}