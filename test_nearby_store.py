'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_nearby_store

This file is a unit test for:
nearby_store.py
'''

import unittest
from analysis.nearby_store import NearbyStore
from model.storefront import Storefront
from model.transit_station import TransitStation


class TestNearbyStore(unittest.TestCase):
    '''
    Class: TestNearbyStore
    This class consists of a list of unit tests to test each of the methods
    within the 'NearbyStore' class
    '''
    def setUp(self):
        # Instantiate a basic 'Storefront'
        self.basic_store_id = 2346
        self.basic_business_name = 'Miku Restaurant Vancouver Ltd'
        self.basic_address_unit = '70'
        self.basic_address_number = 200
        self.basic_address_street = 'GRANVILLE ST'
        self.basic_retail_category = 'Food & Beverage'
        self.basic_coordinates = (491828.5353999988, 5459317.5562)
        self.basic_local_area = 'Downtown'
        self.basic_storefront = Storefront(
            self.basic_store_id,
            self.basic_business_name,
            self.basic_address_unit,
            self.basic_address_number,
            self.basic_address_street,
            self.basic_retail_category,
            self.basic_coordinates,
            self.basic_local_area
            )

        # Instantiate a basic 'TransitStation'
        self.basic_station_name = 'WATERFRONT'
        self.basic_coordinates = (491757.59371811966, 5459218.857871494)
        self.basic_local_area = 'Downtown'
        self.basic_transit_station = TransitStation(self.basic_station_name, self.basic_coordinates, self.basic_local_area)

        # Instantiate a basic 'NearbyStore'
        self.basic_distance = 121.54868274792
        self.basic_retail_category = 'All'
        self.basic_object = NearbyStore(
            storefront = self.basic_storefront,
            origin_transit_station = self.basic_transit_station,
            distance = self.basic_distance,
            retail_category = self.basic_retail_category
        )


    def test_init_basic(self):
        test_object = NearbyStore(
            storefront = self.basic_storefront,
            origin_transit_station = self.basic_transit_station,
            distance = 121.54868274792,
            retail_category = 'All'
        )
        self.assertEqual(test_object.storefront, self.basic_storefront)
        self.assertEqual(test_object.origin_station, self.basic_transit_station)
        self.assertEqual(test_object.distance, 121.54868274792)
        self.assertEqual(test_object.retail_category, 'All')

        # Test case without specifying retail_category (use default value instead)
        test_object = NearbyStore(
            storefront = self.basic_storefront,
            origin_transit_station = self.basic_transit_station,
            distance = 121.54868274792,
        )
        self.assertEqual(test_object.storefront, self.basic_storefront)
        self.assertEqual(test_object.origin_station, self.basic_transit_station)
        self.assertEqual(test_object.distance, 121.54868274792)
        self.assertEqual(test_object.retail_category, 'All')


    def test_init_TypeError(self):
        with self.assertRaises(TypeError):
            test_distance = 'One hundred one and fifty-four hundredths'
            NearbyStore(
                self.basic_storefront,
                self.basic_transit_station,
                test_distance,
                self.basic_retail_category
            )

        with self.assertRaises(TypeError):
            test_retail_category = 9000
            NearbyStore(
                self.basic_storefront,
                self.basic_transit_station,
                self.basic_distance,
                test_retail_category
            )

    
    def test_str_basic(self):
        self.assertEqual(str(self.basic_object), "Nearby Store: Miku Restaurant Vancouver Ltd\nOrigin Station: WATERFRONT\nDistance: 121.5487 m\nRetail Type: All\n")


    def test_str_TypeError(self):
        with self.assertRaises(TypeError):
            self.basic_object.storefront.business_name = 1000
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.origin_station.station_name = 1000
            str(self.basic_object)
            
        with self.assertRaises(TypeError):
            self.basic_object.distance = 'One hundred one and fifty-four hundredths'
            str(self.basic_object)
            
        with self.assertRaises(TypeError):
            self.basic_object.retail_category = 9000
            str(self.basic_object)


    def test_eq_True(self):
        # Instantiate an other 'Storefront'
        other_store_id = 2346
        other_business_name = 'Miku Restaurant Vancouver Ltd'
        other_address_unit = '70'
        other_address_number = 200
        other_address_street = 'GRANVILLE ST'
        other_retail_category = 'Food & Beverage'
        other_coordinates = (491828.5353999988, 5459317.5562)
        other_local_area = 'Downtown'
        other_storefront = Storefront(
            other_store_id,
            other_business_name,
            other_address_unit,
            other_address_number,
            other_address_street,
            other_retail_category,
            other_coordinates,
            other_local_area
            )

        # Instantiate an other 'TransitStation'
        other_station_name = 'WATERFRONT'
        other_coordinates = (491757.59371811966, 5459218.857871494)
        other_local_area = 'Downtown'
        other_transit_station = TransitStation(other_station_name, other_coordinates, other_local_area)

        other_distance = 121.54868274792
        other_retail_category = 'All'
        other_object = NearbyStore(
            storefront = other_storefront,
            origin_transit_station = other_transit_station,
            distance = other_distance,
            retail_category = other_retail_category
        )
        self.assertTrue(self.basic_object == other_object)


    def test_eq_False(self):
        # Instantiate an other 'Storefront'
        other_store_id = 2757
        other_business_name = 'Nordstrom'
        other_address_unit = 'N/A'
        other_address_number = 799
        other_address_street = 'ROBSON ST'
        other_retail_category = 'Comparison Goods'
        other_coordinates = (491308.8991999985, 5458839.098400002)
        other_local_area = 'Downtown'
        other_storefront = Storefront(
            other_store_id,
            other_business_name,
            other_address_unit,
            other_address_number,
            other_address_street,
            other_retail_category,
            other_coordinates,
            other_local_area
            )

        # Instantiate an other 'TransitStation'
        other_station_name = 'MARINE DRIVE'
        other_coordinates = (491473.12822691567, 5450757.244252066)
        other_local_area = 'Marpole'
        other_transit_station = TransitStation(other_station_name, other_coordinates, other_local_area)

        other_distance = 18083.5226010568
        other_retail_category = 'All'
        other_object = NearbyStore(
            storefront = other_storefront,
            origin_transit_station = other_transit_station,
            distance = other_distance,
            retail_category = other_retail_category
        )
        self.assertFalse(self.basic_object == other_object)


    def test_eq_TypeError(self):
        with self.assertRaises(TypeError):
            other_object = 2000
            self.basic_object == other_object

        # Instantiate an other 'Storefront'
        other_store_id = 2757
        other_business_name = 'Nordstrom'
        other_address_unit = 'N/A'
        other_address_number = 799
        other_address_street = 'ROBSON ST'
        other_retail_category = 'Comparison Goods'
        other_coordinates = (491308.8991999985, 5458839.098400002)
        other_local_area = 'Downtown'
        other_storefront = Storefront(
            other_store_id,
            other_business_name,
            other_address_unit,
            other_address_number,
            other_address_street,
            other_retail_category,
            other_coordinates,
            other_local_area
            )

        # Instantiate an other 'TransitStation'
        other_station_name = 'MARINE DRIVE'
        other_coordinates = (491473.12822691567, 5450757.244252066)
        other_local_area = 'Marpole'
        other_transit_station = TransitStation(other_station_name, other_coordinates, other_local_area)

        other_distance = 18083.5226010568
        other_retail_category = 'All'
        other_object = NearbyStore(
            storefront = other_storefront,
            origin_transit_station = other_transit_station,
            distance = other_distance,
            retail_category = other_retail_category
        )

        with self.assertRaises(TypeError):
            self.basic_object.storefront.business_name = 1000
            other_object.storefront.business_name = 'Nordstrom'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.storefront.business_name = 'Miku Restaurant Vancouver Ltd'
            other_object.storefront.business_name = 2000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.storefront.business_name = 3000
            other_object.storefront.business_name = 4000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.origin_station.station_name = 5000
            other_object.origin_station.station_name = 'MARINE DRIVE'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.origin_station.station_name = 'WATERFRONT'
            other_object.origin_station.station_name = 6000
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.origin_station.station_name = 7000
            other_object.origin_station.station_name = 8000
            self.basic_object == other_object


# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
