'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_nearby_stores_finder

This file is a unit test for:
nearby_stores_finder.py
'''

import unittest
from analysis.nearby_stores_finder import *
from model.storefront import Storefront
from model.transit_station import TransitStation
from user_interface.user_input import UserInput


class TestNearbyStoresFinder(unittest.TestCase):
    '''
    Class: TestNearbyStoresFinder
    This class consists of a list of unit tests to test the functions
    in the transit_station_factory module
    '''
    def setUp(self):
        # Instantiate multiple 'Storefront'
        self.basic_storefront_1 = Storefront(
            store_id = 2346,
            business_name = 'Miku Restaurant Vancouver Ltd',
            address_unit = '70',
            address_number = 200,
            address_street = 'GRANVILLE ST',
            retail_category = 'Food & Beverage',
            coordinates = (491828.5353999988, 5459317.5562),
            local_area = 'Downtown'
        )

        self.basic_storefront_2 = Storefront(
            store_id = 5422,
            business_name = 'CoCo Fresh Tea & Juice',
            address_unit = 'N/A',
            address_number = 491,
            address_street = 'SW MARINE DRIVE',
            retail_category = 'Food & Beverage',
            coordinates = (491514.51389999833, 5450961.4485),
            local_area = 'Marpole'
        )

        self.basic_storefront_3 = Storefront(
            store_id = 2757,
            business_name = 'Nordstrom',
            address_unit = 'N/A',
            address_number = 799,
            address_street = 'ROBSON ST',
            retail_category = 'Comparison Goods',
            coordinates = (491308.8991999985, 5458839.098400002),
            local_area = 'Downtown'
        )

        self.basic_storefront_4 = Storefront(
            store_id = 2033,
            business_name = 'Golden Rug Outlet',
            address_unit = 'N/A',
            address_number = 3211,
            address_street = 'DUNBAR ST',
            retail_category = 'Comparison Goods',
            coordinates = (486503.42789999687, 5456109.006700002),
            local_area = 'Dunbar-Southlands'
        )

        self.basic_storefront_5 = Storefront(
            store_id = 2036,
            business_name = 'Golden Rug Outlet',
            address_unit = 'N/A',
            address_number = 3271,
            address_street = 'DUNBAR ST',
            retail_category = 'Comparison Goods',
            coordinates = (486503.42789999687, 5456109.006700002),
            local_area = 'Dunbar-Southlands'
        )

        self.basic_storefront_6 = Storefront(
            store_id = 2059,
            business_name = 'Vacant',
            address_unit = 'N/A',
            address_number = 3422,
            address_street = 'DUNBAR ST',
            retail_category = 'Vacant',
            coordinates = (486557.51459999796, 5455959.7917),
            local_area = 'Dunbar-Southlands'
        )

        self.list_storefronts = [
            self.basic_storefront_1,
            self.basic_storefront_2,
            self.basic_storefront_3,
            self.basic_storefront_4,
            self.basic_storefront_5,
            self.basic_storefront_6,
        ]

        # Instantiate a basic 'TransitStation'
        self.basic_transit_station = TransitStation(
            name = 'WATERFRONT',
            coordinates = (491757.59371811966, 5459218.857871494),
            local_area = 'Downtown'
        )

        # Instantiate 2 'UserInput'
        self.basic_user_input_1 = UserInput()
        self.basic_user_input_1.transit_station = self.basic_transit_station
        self.basic_user_input_1.store_category = 'All'
        self.basic_user_input_1.search_radius = 0.0
        self.basic_user_input_1.max_display_count = 50

        self.basic_user_input_2 = UserInput()
        self.basic_user_input_2.transit_station = self.basic_transit_station
        self.basic_user_input_2.store_category = 'Comparison Goods'
        self.basic_user_input_2.search_radius = 1000.0
        self.basic_user_input_2.max_display_count = 100

        # Instantiate multiple 'NearbyStore'
        self.basic_nearby_store_1 = NearbyStore(
            storefront = self.basic_storefront_1,
            origin_transit_station = self.basic_transit_station,
            distance = 121.54868274792,
            retail_category = 'All'
        )

        self.basic_nearby_store_2 = NearbyStore(
            storefront = self.basic_storefront_2,
            origin_transit_station = self.basic_transit_station,
            distance = 8260.9864620649,
            retail_category = 'All'
        )

        self.basic_nearby_store_3 = NearbyStore(
            storefront = self.basic_storefront_3,
            origin_transit_station = self.basic_transit_station,
            distance = 587.82993014972,
            retail_category = 'All'  
        )
        
        self.basic_nearby_store_4 = NearbyStore(
            storefront = self.basic_storefront_4,
            origin_transit_station = self.basic_transit_station,
            distance = 6105.5247729547,
            retail_category = 'All'
        )
   
        self.basic_nearby_store_5 = NearbyStore(
            storefront = self.basic_storefront_5,
            origin_transit_station = self.basic_transit_station,
            distance = 6105.5247729547,
            retail_category = 'All' 
        )

        self.basic_nearby_store_6 = NearbyStore(
            storefront = self.basic_storefront_6,
            origin_transit_station = self.basic_transit_station,
            distance = 6136.9646524079,
            retail_category = 'All' 
        )

        self.list_nearby_stores = [
            self.basic_nearby_store_1,
            self.basic_nearby_store_2,
            self.basic_nearby_store_3,
            self.basic_nearby_store_4,
            self.basic_nearby_store_5,
            self.basic_nearby_store_6,
        ]


    def test_find_nearby_stores_basic_1(self):
        test_output = find_nearby_stores(self.basic_user_input_1, self.list_storefronts)
        expected_output = [
            self.basic_nearby_store_1,
            self.basic_nearby_store_3,
            self.basic_nearby_store_4,
            self.basic_nearby_store_2,
        ]
        self.assertEqual(test_output, expected_output)


    def test_find_nearby_stores_basic_2(self):
        test_output = find_nearby_stores(self.basic_user_input_2, self.list_storefronts)
        expected_output = [
            self.basic_nearby_store_3,
        ]
        self.assertEqual(test_output, expected_output)


    def test_find_nearby_stores_TypeError_1(self):
        self.basic_user_input_1.transit_station.station_name = 2000
        with self.assertRaises(TypeError):
            find_nearby_stores(self.basic_user_input_1, self.list_storefronts)


    def test_find_nearby_stores_TypeError_2(self):
        self.basic_user_input_1.transit_station.coordinates = [491757.59371811966, 5459218.857871494]
        with self.assertRaises(TypeError):
            find_nearby_stores(self.basic_user_input_1, self.list_storefronts)


    def test_find_nearby_stores_TypeError_3(self):
        self.list_storefronts = (
            self.basic_nearby_store_1,
            self.basic_nearby_store_2,
            self.basic_nearby_store_3,
            self.basic_nearby_store_4,
            self.basic_nearby_store_5,
            self.basic_nearby_store_6,
        )
        with self.assertRaises(TypeError):
            find_nearby_stores(self.basic_user_input_1, self.list_storefronts)


    def test_find_nearby_stores_TypeError_4(self):
        self.basic_user_input_1.search_radius = 'Five thousand'
        with self.assertRaises(TypeError):
            find_nearby_stores(self.basic_user_input_1, self.list_storefronts)


    def test_find_nearby_stores_ValueError_1(self):
        self.basic_user_input_1.transit_station.coordinates = ()
        with self.assertRaises(ValueError):
            find_nearby_stores(self.basic_user_input_1, self.list_storefronts)

        self.basic_user_input_1.transit_station.coordinates = (1.0, 2.0, 3.0)
        with self.assertRaises(ValueError):
            find_nearby_stores(self.basic_user_input_1, self.list_storefronts)

        self.basic_user_input_1.transit_station.coordinates = (1.0, 'two')
        with self.assertRaises(ValueError):
            find_nearby_stores(self.basic_user_input_1, self.list_storefronts)

        self.basic_user_input_1.transit_station.coordinates = ('one', 'two')
        with self.assertRaises(ValueError):
            find_nearby_stores(self.basic_user_input_1, self.list_storefronts)


    def test_find_nearby_stores_ValueError_2(self):
        test_list_storefronts = []
        with self.assertRaises(ValueError):
            find_nearby_stores(self.basic_user_input_1, test_list_storefronts)


    def test_filter_stores_by_category_basic(self):
        test_category = 'Comparison Goods'
        test_output = filter_stores_by_category(self.list_storefronts, test_category)
        expected_output = [
            self.basic_storefront_3,
            self.basic_storefront_4,
            self.basic_storefront_5
        ]
        self.assertEqual(test_output, expected_output)

        test_category = 'Food & Beverage'
        test_output = filter_stores_by_category(self.list_storefronts, test_category)
        expected_output = [
            self.basic_storefront_1,
            self.basic_storefront_2
        ]
        self.assertEqual(test_output, expected_output)

        test_category = 'All'
        test_output = filter_stores_by_category(self.list_storefronts, test_category)
        expected_output = [
            self.basic_storefront_1,
            self.basic_storefront_2,
            self.basic_storefront_3,
            self.basic_storefront_4,
            self.basic_storefront_5,
        ]
        self.assertEqual(test_output, expected_output)


    def test_filter_stores_by_category_TypeError(self):
        with self.assertRaises(TypeError):
            test_list_storefronts = (
                self.basic_storefront_1,
                self.basic_storefront_2,
                self.basic_storefront_3,
            )
            filter_stores_by_category(test_list_storefronts, self.basic_user_input_1.store_category)

        with self.assertRaises(TypeError):
            test_store_category = 5000
            filter_stores_by_category(self.list_storefronts, test_store_category)


    def test_filter_stores_by_category_ValueError(self):
        with self.assertRaises(ValueError):
            test_list_storefronts = []
            filter_stores_by_category(test_list_storefronts, self.basic_user_input_1.store_category)


    def test_filter_stores_by_search_radius_basic(self):
        test_search_radius = 5000.0
        test_output = filter_stores_by_search_radius(self.list_nearby_stores.copy(), test_search_radius)
        expected_output = [
            self.basic_nearby_store_1,
            self.basic_nearby_store_3,
        ]
        self.assertEqual(test_output, expected_output)

        test_search_radius = 0.0
        test_output = filter_stores_by_search_radius(self.list_nearby_stores.copy(), test_search_radius)
        expected_output = [
            self.basic_nearby_store_1,
            self.basic_nearby_store_2,
            self.basic_nearby_store_3,
            self.basic_nearby_store_4,
            self.basic_nearby_store_5,
            self.basic_nearby_store_6,
        ]
        self.assertEqual(test_output, expected_output)


    def test_filter_stores_by_search_radius_TypeError(self):
        with self.assertRaises(TypeError):
            test_list_nearby_stores = 2000
            filter_stores_by_search_radius(test_list_nearby_stores, self.basic_user_input_1.search_radius)

        with self.assertRaises(TypeError):
            test_search_radius = 'Five thousand'
            filter_stores_by_search_radius(self.list_nearby_stores, test_search_radius)


    def test_filter_stores_by_search_radius_ValueError(self):
        with self.assertRaises(ValueError):
            test_list_nearby_stores = []
            filter_stores_by_search_radius(test_list_nearby_stores, self.basic_user_input_1.search_radius)


    def test_sort_stores_by_distance_basic(self):
        test_output = sort_stores_by_distance(self.list_nearby_stores)
        expected_output = [
            self.basic_nearby_store_1,
            self.basic_nearby_store_3,
            self.basic_nearby_store_4,
            self.basic_nearby_store_5,
            self.basic_nearby_store_6,
            self.basic_nearby_store_2,
        ]
        self.assertEqual(test_output, expected_output)


    def test_sort_stores_by_distance_TypeError(self):
        with self.assertRaises(TypeError):
            test_list_nearby_stores = 2000
            sort_stores_by_distance(test_list_nearby_stores)


    def test_sort_stores_by_distance_ValueError(self):
        with self.assertRaises(ValueError):
            test_list_nearby_stores = []
            sort_stores_by_distance(test_list_nearby_stores)


    def test_remove_duplicated_stores_basic(self):
        test_output = remove_duplicated_stores(self.list_nearby_stores.copy())
        expected_output = [
            self.basic_nearby_store_1,
            self.basic_nearby_store_2,
            self.basic_nearby_store_3,
            self.basic_nearby_store_4,
            self.basic_nearby_store_6,
        ]
        self.assertEqual(test_output, expected_output)


    def test_remove_duplicated_stores_TypeError(self):
        with self.assertRaises(TypeError):
            test_list_nearby_stores = 2000
            remove_duplicated_stores(test_list_nearby_stores)


    def test_remove_duplicated_stores_ValueError(self):
        with self.assertRaises(ValueError):
            test_list_nearby_stores = []
            remove_duplicated_stores(test_list_nearby_stores)


# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
