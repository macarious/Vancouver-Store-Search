'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Test Suite - test_storefront

This file is a unit test for:
storefront.py
'''

import unittest
from storefront import Storefront


class TestStorefront(unittest.TestCase):
    '''
    Class: TestStorefront
    This class consists of a list of unit tests to test each of the methods
    within the 'Storefront' class
    '''
    def setUp(self):
        self.basic_store_id = 2346
        self.basic_business_name = 'Miku Restaurant Vancouver Ltd'
        self.basic_address_unit = '70'
        self.basic_address_number = 200
        self.basic_address_street = 'GRANVILLE ST'
        self.basic_retail_category = 'Food & Beverage'
        self.basic_coordinates = (491828.5353999988, 5459317.5562)
        self.basic_local_area = 'Downtown'
        self.basic_object = Storefront(
            self.basic_store_id,
            self.basic_business_name,
            self.basic_address_unit,
            self.basic_address_number,
            self.basic_address_street,
            self.basic_retail_category,
            self.basic_coordinates,
            self.basic_local_area
            )


    def test_init_basic(self):
        self.assertEqual(self.basic_object.store_id, 2346)
        self.assertEqual(self.basic_object.business_name, 'Miku Restaurant Vancouver Ltd')
        self.assertEqual(self.basic_object.address_unit, '70')
        self.assertEqual(self.basic_object.address_number, 200)
        self.assertEqual(self.basic_object.address_street, 'GRANVILLE ST')
        self.assertEqual(self.basic_object.retail_category, 'Food & Beverage')
        self.assertEqual(self.basic_object.coordinates, (491828.5353999988, 5459317.5562))
        self.assertEqual(self.basic_object.local_area, 'Downtown')
        self.assertEqual(self.basic_object.full_address, '70-200 GRANVILLE ST')

        # Check case when address_unit == 'N/A'
        test_address_unit = 'N/A'
        self.basic_object = Storefront(
            self.basic_store_id,
            self.basic_business_name,
            test_address_unit,
            self.basic_address_number,
            self.basic_address_street,
            self.basic_retail_category,
            self.basic_coordinates,
            self.basic_local_area
            )
        self.assertEqual(self.basic_object.full_address, '200 GRANVILLE ST')



    def test_init_TypeError(self):
        with self.assertRaises(TypeError):
            test_store_id = 'two thousand three hundred forty-six'
            self.basic_object = Storefront(
                test_store_id,
                self.basic_business_name,
                self.basic_address_unit,
                self.basic_address_number,
                self.basic_address_street,
                self.basic_retail_category,
                self.basic_coordinates,
                self.basic_local_area
                )

        with self.assertRaises(TypeError):
            test_basic_business_name = 2000
            self.basic_object = Storefront(
                self.basic_store_id,
                test_basic_business_name,
                self.basic_address_unit,
                self.basic_address_number,
                self.basic_address_street,
                self.basic_retail_category,
                self.basic_coordinates,
                self.basic_local_area
                )
            
        with self.assertRaises(TypeError):
            test_address_unit = 70
            self.basic_object = Storefront(
                self.basic_store_id,
                self.basic_business_name,
                test_address_unit,
                self.basic_address_number,
                self.basic_address_street,
                self.basic_retail_category,
                self.basic_coordinates,
                self.basic_local_area
                )
            
        with self.assertRaises(TypeError):
            test_address_number = 'Two Hundred'
            self.basic_object = Storefront(
                self.basic_store_id,
                self.basic_business_name,
                self.basic_address_unit,
                test_address_number,
                self.basic_address_street,
                self.basic_retail_category,
                self.basic_coordinates,
                self.basic_local_area
                )
            
        with self.assertRaises(TypeError):
            test_address_street = 2000
            self.basic_object = Storefront(
                self.basic_store_id,
                self.basic_business_name,
                self.basic_address_unit,
                self.basic_address_number,
                test_address_street,
                self.basic_retail_category,
                self.basic_coordinates,
                self.basic_local_area
                )
            
        with self.assertRaises(TypeError):
            test_retail_category = 2000
            self.basic_object = Storefront(
                self.basic_store_id,
                self.basic_business_name,
                self.basic_address_unit,
                self.basic_address_number,
                self.basic_address_street,
                test_retail_category,
                self.basic_coordinates,
                self.basic_local_area
                )
            
        with self.assertRaises(TypeError):
            test_coordinates = [491828.5353999988, 5459317.5562]
            self.basic_object = Storefront(
                self.basic_store_id,
                self.basic_business_name,
                self.basic_address_unit,
                self.basic_address_number,
                self.basic_address_street,
                self.basic_retail_category,
                test_coordinates,
                self.basic_local_area
                )
            
        with self.assertRaises(TypeError):
            test_local_area = 2000
            self.basic_object = Storefront(
                self.basic_store_id,
                self.basic_business_name,
                self.basic_address_unit,
                self.basic_address_number,
                self.basic_address_street,
                self.basic_retail_category,
                self.basic_coordinates,
                test_local_area
                )


    def test_init_ValueError(self):
        with self.assertRaises(ValueError):
            test_coordinates = ()
            self.basic_object = Storefront(
                self.basic_store_id,
                self.basic_business_name,
                self.basic_address_unit,
                self.basic_address_number,
                self.basic_address_street,
                self.basic_retail_category,
                test_coordinates,
                self.basic_local_area
                )

        with self.assertRaises(ValueError):
            test_coordinates = (1.0, 2.0, 3.0)
            self.basic_object = Storefront(
                self.basic_store_id,
                self.basic_business_name,
                self.basic_address_unit,
                self.basic_address_number,
                self.basic_address_street,
                self.basic_retail_category,
                test_coordinates,
                self.basic_local_area
                )

        with self.assertRaises(ValueError):
            test_coordinates = (1.0, 'Two')
            self.basic_object = Storefront(
                self.basic_store_id,
                self.basic_business_name,
                self.basic_address_unit,
                self.basic_address_number,
                self.basic_address_street,
                self.basic_retail_category,
                test_coordinates,
                self.basic_local_area
                )

        with self.assertRaises(ValueError):
            test_coordinates = ('One', 'Two')
            self.basic_object = Storefront(
                self.basic_store_id,
                self.basic_business_name,
                self.basic_address_unit,
                self.basic_address_number,
                self.basic_address_street,
                self.basic_retail_category,
                test_coordinates,
                self.basic_local_area
                )

    
    def test_str_basic(self):
        expected_text = (
            "Store ID: 2346\n"
            "Business Name: Miku Restaurant Vancouver Ltd\n"
            "Address: 70-200 GRANVILLE ST\n"
            "Category: Food & Beverage\n"
            "Coordinates: (491828.5353999988, 5459317.5562)\n"
            "Local Area: Downtown\n"
        )
        self.assertEqual(str(self.basic_object), expected_text)


    def test_str_TypeError(self):
        with self.assertRaises(TypeError):
            self.basic_object.store_id = 'two thousand three hundred forty-six'
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.business_name = 2000
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.full_address = 2000
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.retail_category = 2000
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.coordinates = [491828.5353999988, 5459317.5562]
            str(self.basic_object)

        with self.assertRaises(TypeError):
            self.basic_object.local_area = 2000
            str(self.basic_object)

    
    def test_str_ValueError(self):
        with self.assertRaises(ValueError):
            self.basic_object.coordinates = ()
            str(self.basic_object)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = (1.0, 2.0, 3.0)
            str(self.basic_object)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = (1.0, 'Two')
            str(self.basic_object)

        with self.assertRaises(ValueError):
            self.basic_object.coordinates = ('One', 'Two')
            str(self.basic_object)


    def test_eq_True(self):
        other_store_id = 2346
        other_business_name = 'Miku Restaurant Vancouver Ltd'
        other_address_unit = '70'
        other_address_number = 200
        other_address_street = 'GRANVILLE ST'
        other_retail_category = 'Food & Beverage'
        other_coordinates = (491828.5353999988, 5459317.5562)
        other_local_area = 'Downtown'
        other_object = Storefront(
            other_store_id,
            other_business_name,
            other_address_unit,
            other_address_number,
            other_address_street,
            other_retail_category,
            other_coordinates,
            other_local_area
            )
        self.assertTrue(self.basic_object == other_object)


    def test_eq_False(self):
        other_store_id = 5422
        other_business_name = 'CoCo Fresh Tea & Juice'
        other_address_unit = 'N/A'
        other_address_number = 491
        other_address_street = 'SW MARINE DRIVE'
        other_retail_category = 'Food & Beverage'
        other_coordinates = (491514.51389999833, 5450961.4485)
        other_local_area = 'Marpole'
        other_object = Storefront(
            other_store_id,
            other_business_name,
            other_address_unit,
            other_address_number,
            other_address_street,
            other_retail_category,
            other_coordinates,
            other_local_area
            )
        self.assertFalse(self.basic_object == other_object)


    def test_eq_TypeError(self):
        other_store_id = 5422
        other_business_name = 'CoCo Fresh Tea & Juice'
        other_address_unit = 'N/A'
        other_address_number = 491
        other_address_street = 'SW MARINE DRIVE'
        other_retail_category = 'Food & Beverage'
        other_coordinates = (491514.51389999833, 5450961.4485)
        other_local_area = 'Marpole'
        other_object = Storefront(
            other_store_id,
            other_business_name,
            other_address_unit,
            other_address_number,
            other_address_street,
            other_retail_category,
            other_coordinates,
            other_local_area
            )

        with self.assertRaises(TypeError):
            self.basic_object.store_id = 'two thousand three hundred forty-six'
            other_object.store_id = 5422
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.store_id = 2346
            other_object.store_id = 'five thousand four hundred twenty-two'
            self.basic_object == other_object

        with self.assertRaises(TypeError):
            self.basic_object.store_id = 'two thousand three hundred forty-six'
            other_object.store_id = 'five thousand four hundred twenty-two'
            self.basic_object == other_object


# Run test in main
def main():

    unittest.main(verbosity = 3)

if __name__ == '__main__':
    main()
