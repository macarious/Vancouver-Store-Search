'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_visualization_view

This file is a unit test for:
visualization_view.py
'''

import unittest
from analysis.nearby_store import NearbyStore
from model.local_area_boundary import LocalAreaBoundary
from model.storefront import Storefront
from model.transit_station import TransitStation
from tkinter import *
from tkinter import ttk
from user_interface.graphical_user_interface import GraphicalUserInterface
from user_interface.user_input import UserInput
from user_interface.visualization_view import VisualizationView


class TestVisualizationView(unittest.TestCase):
    '''
    Class: TestVisualizationView
    This class consists of a list of unit tests to test the methods from
    the 'VisualizationView' class. GUI related methods are not tested.
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

        self.basic_list_storefronts = [
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

        # Instantiate 2 basic 'UserInput'
        self.basic_user_input_1 = UserInput()
        self.basic_user_input_1.transit_station = self.basic_transit_station
        self.basic_user_input_1.store_category = 'Comparison Goods'
        self.basic_user_input_1.search_radius = 1000.0
        self.basic_user_input_1.max_display_count = 100

        self.basic_user_input_2 = UserInput()
        self.basic_user_input_2.transit_station = self.basic_transit_station
        self.basic_user_input_2.store_category = 'All'
        self.basic_user_input_2.search_radius = 500.0
        self.basic_user_input_2.max_display_count = 50

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

        self.basic_list_nearby_stores = [
            self.basic_nearby_store_1,
            self.basic_nearby_store_2,
            self.basic_nearby_store_3,
            self.basic_nearby_store_4,
            self.basic_nearby_store_5,
            self.basic_nearby_store_6,
        ]

        # Instantiate multiple 'LocalAreaBoundary'
        self.basic_local_area_boundary_1 = LocalAreaBoundary(
            abbreviation = 'OAK',
            name = 'Oakridge',
            list_boundary_coordinates = [(492310.70745902986, 5453376.091043321), (492269.0509910676, 5451793.061679327), (489794.0144154225, 5451845.011054722), (489837.64126147685, 5453508.59546255), (490678.46469729935, 5453466.396391663), (492310.70745902986, 5453376.091043321)],
            centroid_coordinates = (5452631.7289951695, 491042.52665588236)
        )
        self.basic_local_area_boundary_2 = LocalAreaBoundary(
            abbreviation = 'GW',
            name = 'Grandview-Woodland',
            list_boundary_coordinates = [(494399.4616453806, 5459725.039424128), (495071.2898342053, 5459708.280744998), (495446.2721377341, 5459644.768848708), (495460.81964618707, 5459793.6101129325), (495892.65275480703, 5460083.7676818995), (495882.8355803871, 5456602.905781702), (494363.54977730464, 5456622.063910625), (494367.75457073154, 5456933.75961796), (494399.4616453806, 5459725.039424128)],
            centroid_coordinates = (5458189.142341714,495146.3975207777)
        )

        self.basic_list_local_area_boundaries = [
            self.basic_local_area_boundary_1,
            self.basic_local_area_boundary_2
        ]

        # Instantiate a basic 'GraphicalUserInterface'
        self.basic_gui = GraphicalUserInterface()
        self.basic_gui.user_input = self.basic_user_input_1
        self.basic_gui.list_nearby_stores = self.basic_list_nearby_stores
        self.basic_gui.list_local_area_boundaries = self.basic_list_local_area_boundaries
        self.basic_gui.canvas_output_display = Canvas()
        self.basic_gui.labelframe_output_legend = ttk.LabelFrame()

        # Instantiate a basic 'VisualizationView'
        self.basic_visualization_view = VisualizationView(self.basic_gui)


    def test_init_basic(self):
        expected_user_input = self.basic_user_input_1
        expected_list_local_area_boundaries = self.basic_list_local_area_boundaries
        expected_list_nearby_stores = self.basic_list_nearby_stores
        self.assertEqual(self.basic_visualization_view.user_input, expected_user_input)
        self.assertEqual(self.basic_visualization_view.list_local_area_boundaries, expected_list_local_area_boundaries)
        self.assertEqual(self.basic_visualization_view.list_nearby_stores, expected_list_nearby_stores)
        self.assertEqual(self.basic_visualization_view.map_min_x, 0.0)
        self.assertEqual(self.basic_visualization_view.map_max_x, 0.0)
        self.assertEqual(self.basic_visualization_view.map_min_y, 0.0)
        self.assertEqual(self.basic_visualization_view.map_max_y, 0.0)
        self.assertEqual(self.basic_visualization_view.scale, 1.0)


    def test_init_TypeError_1(self):
        self.basic_gui.list_local_area_boundaries = 2000
        with self.assertRaises(TypeError):
            VisualizationView()

        self.basic_gui.list_local_area_boundaries = []
        with self.assertRaises(TypeError):
            VisualizationView()


    def test_init_TypeError_2(self):
        self.basic_gui.list_nearby_stores = 2000
        with self.assertRaises(TypeError):
            VisualizationView()

        self.basic_gui.list_nearby_stores = []
        with self.assertRaises(TypeError):
            VisualizationView()


    def test_str_basic(self):
        expected_output = (
            f"Visualization View\n"
            f"Input -- Station: WATERFRONT\n"
            f"Input -- Store Category: Comparison Goods\n"
            f"Input -- Search Radius: 1000.0\n"
        )
        self.assertEqual(str(self.basic_visualization_view), expected_output)


    def test_eq_True(self):
        other_object = VisualizationView(self.basic_gui)
        self.assertTrue(self.basic_visualization_view == other_object)


    def test_eq_False(self):
        self.basic_gui.user_input = self.basic_user_input_2
        other_object = VisualizationView(self.basic_gui)
        self.assertFalse(self.basic_visualization_view == other_object)


    def test_eq_TypeError(self):
        test_other_visualization_view = 2000
        with self.assertRaises(TypeError):
            self.basic_visualization_view == test_other_visualization_view
        

    def test_calculate_canvas_scale_basic(self):
        test_output = self.basic_visualization_view._calculate_canvas_scale()
        expected_output = 0.000108555290
        self.assertAlmostEqual(test_output, expected_output)

        # Check if the following attributes are updated properly
        test_map_min_x = self.basic_visualization_view.map_min_x
        expected_map_min_x = 489794.0144154225
        self.assertAlmostEqual(test_map_min_x, expected_map_min_x)

        test_map_max_x = self.basic_visualization_view.map_max_x
        expected_map_max_x = 495892.65275480703
        self.assertAlmostEqual(test_map_max_x, expected_map_max_x)

        test_map_min_y = self.basic_visualization_view.map_min_y
        expected_map_min_y = 5451793.061679327
        self.assertAlmostEqual(test_map_min_y, expected_map_min_y)

        test_map_max_y = self.basic_visualization_view.map_max_y
        expected_map_max_y = 5460083.7676818995
        self.assertAlmostEqual(test_map_max_y, expected_map_max_y)


    def test_calculate_canvas_scale_TypeError(self):
        self.basic_visualization_view.list_local_area_boundaries = 2000
        with self.assertRaises(TypeError):
            self.basic_visualization_view._calculate_canvas_scale()


    def test_calculate_canvas_scale_ValueError(self):
        self.basic_visualization_view.list_local_area_boundaries = []
        with self.assertRaises(ValueError):
            self.basic_visualization_view._calculate_canvas_scale()


    def test_calculate_scaled_centroid_all_local_area_boundary_basic(self):
        self.basic_visualization_view.map_min_x = 489794.0144154225
        self.basic_visualization_view.map_max_x = 495892.65275480703
        self.basic_visualization_view.map_min_y = 5451793.061679327
        self.basic_visualization_view.map_max_y = 5460083.7676818995
        test_output = self.basic_visualization_view._calculate_scaled_centroid_all_local_area_boundary()
        expected_output = (492843.3335851148, 5455938.414680613)
        self.assertEqual(test_output, expected_output)

        self.basic_visualization_view.map_min_x = -0.0005
        self.basic_visualization_view.map_max_x = +0.0005
        self.basic_visualization_view.map_min_y = -2000.0
        self.basic_visualization_view.map_max_y = 0.0
        test_output = self.basic_visualization_view._calculate_scaled_centroid_all_local_area_boundary()
        expected_output = (0.0, -1000.0)
        self.assertEqual(test_output, expected_output)


    def test_calculate_scaled_centroid_all_local_area_boundaries_TypeError_1(self):
        self.basic_visualization_view.map_min_x = 'One hundred'
        with self.assertRaises(TypeError):
            self.basic_visualization_view._calculate_scaled_centroid_all_local_area_boundary()


    def test_calculate_scaled_centroid_all_local_area_boundaries_TypeError_2(self):
        self.basic_visualization_view.map_max_x = [1000.0]
        with self.assertRaises(TypeError):
            self.basic_visualization_view._calculate_scaled_centroid_all_local_area_boundary()


    def test_calculate_scaled_centroid_all_local_area_boundaries_TypeError_3(self):
        self.basic_visualization_view.map_min_y = False
        with self.assertRaises(TypeError):
            self.basic_visualization_view._calculate_scaled_centroid_all_local_area_boundary()


    def test_calculate_scaled_centroid_all_local_area_boundaries_TypeError_4(self):
        self.basic_visualization_view.map_max_y = {'x-value' : -50.0}
        with self.assertRaises(TypeError):
            self.basic_visualization_view._calculate_scaled_centroid_all_local_area_boundary()


    def test_normalize_coordinates_basic(self):
        test_coordinates = (400000.0, 5000000.0)
        self.basic_visualization_view.map_min_x = 489794.0144154225
        self.basic_visualization_view.map_max_x = 495892.65275480703
        self.basic_visualization_view.map_min_x = 5451793.061679327
        self.basic_visualization_view.map_max_x = 5460083.7676818995
        self.basic_visualization_view.scale = 0.000108555290
        test_output = self.basic_visualization_view._normalize_coordinates(test_coordinates)
        expected_output = (-548.3488608277943, -542.27645)
        self.assertEqual(test_output, expected_output)

        test_coordinates = (-500.0, 0.0)
        self.basic_visualization_view.map_min_x = -20.0
        self.basic_visualization_view.map_max_x = 20.0
        self.basic_visualization_view.map_min_x = -10.0
        self.basic_visualization_view.map_max_x = 10.0
        self.basic_visualization_view.scale = 0.5
        test_output = self.basic_visualization_view._normalize_coordinates(test_coordinates)
        expected_output = (-249.5, 0.5)
        self.assertEqual(test_output, expected_output)


    def test_normalize_coordinates_TypeError_1(self):
        test_coordinates = [50.0, 20.0]
        with self.assertRaises(TypeError):
            self.basic_visualization_view._normalize_coordinates(test_coordinates)

        test_coordinates = 'Three and Two'
        with self.assertRaises(TypeError):
            self.basic_visualization_view._normalize_coordinates(test_coordinates)


    def test_normalize_coordinates_TypeError_2(self):
        test_coordinates = (1.000, 2.000)
        self.basic_visualization_view.scale = 'Three and two-tenths'
        with self.assertRaises(TypeError):
            self.basic_visualization_view._normalize_coordinates(test_coordinates)


    def test_normalize_coordinates_ValueError_1(self):
        test_coordinates = ()
        with self.assertRaises(ValueError):
            self.basic_visualization_view._normalize_coordinates(test_coordinates)

        test_coordinates = (1.0, 2.0, 3.0)
        with self.assertRaises(ValueError):
            self.basic_visualization_view._normalize_coordinates(test_coordinates)

        test_coordinates = ('One', 2.0)
        with self.assertRaises(ValueError):
            self.basic_visualization_view._normalize_coordinates(test_coordinates)

        test_coordinates = ('One', 'Two')
        with self.assertRaises(ValueError):
            self.basic_visualization_view._normalize_coordinates(test_coordinates)


    def test_normalize_coordinates_ValueError_2(self):
        test_coordinates = (1.000, 2.000)
        self.basic_visualization_view.scale = -50.0
        with self.assertRaises(ValueError):
            self.basic_visualization_view._normalize_coordinates(test_coordinates)


# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
