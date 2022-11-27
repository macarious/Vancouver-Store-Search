'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Module Name -- dataset_parameters

This program contains the parameters of each dataset. The parameters
(dataset name, url, and expected header) are stored as attributes in
a 'DatasetDescriptor' class. The instances in this module are used as
Constants in the driver file.

This file is used by the driver file:
data_dashboard.py
'''

# Classes
from model.dataset_descriptor import DatasetDescriptor


# Rapid Transit Stations of Vancouver
TRANSIT_STATIONS_DATASET_DESCRIPTOR = DatasetDescriptor(
    dataset_name = 'Transit Stations',
    url = 'https://opendata.vancouver.ca/explore/dataset/rapid-transit-stations/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910',
    expected_headers = {
        'station name' : 'STATION',
        'coordinates' : 'Geom',
        'local area' : 'Geo Local Area',
    }
)

# Storefronts Inventory of Vancouver
STOREFRONTS_DATASET_DESCRIPTOR = DatasetDescriptor(
    dataset_name = 'Storefronts',
    url = 'https://opendata.vancouver.ca/explore/dataset/storefronts-inventory/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B&epsg=26910',
    expected_headers = {
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
)