'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class Storefront -- see docstring below

This file is used by the following:
storefront_factory.py
'''


COORDINATE_COUNT = 2 # Coordinates are represented by 2 values
# Used to concatenate unit, number, and street to form a full address
ADDRESS_SEPARATOR = {
    'unit-to-number' : '-',
    'number-to-street' : ' ',
}


class Storefront:
    '''
    Class Name: Storefront
        Object of this class holds the different category of data acquired from
        a dataset as its instance attributes. The parameters used to instantiate
        a 'Storefront' are te store id, business name, address (unit, number, street),
        retail category, coordinates, and local area.
        
        The following methods are available:
        __init__ (constructor)
        __str__ 
        __eq__
    '''
    def __init__(self, store_id, business_name, address_unit, address_number, address_street,
        retail_category, coordinates, local_area):
        '''
        Method Name: __init__
            Constructor used to isntantiate 'Storefront' objects
        
        Parameters:
            store_id -- int, storefront ID, unique to each storefront
            business_name -- str, name of business at the storefront
            address_unit -- str, unit number of storefront, 'N/A' if not applicable
            address_number -- str, civic address number of storefront
            address_street -- str, street address of storefront
            retail_category -- str, category of business (Service Commercial, Convenience Goods,
                Comparison Goods, Food & Beverage, Entertainment and Leisure) or Vacant
            coordinates -- tuple of (float, float), coordinates of storefront, in
                 EPSG 26910 format, a local projected coordinate system in metres
            local_area -- str, the neighbourhood the storefront is located
        
        Raises:
            TypeError -- raises if the parameter 'store_id' is not an integer
            TypeError -- raises if the parameter 'business_name' is not a string
            TypeError -- raises if the parameter 'address_unit' is not a string
            TypeError -- raises if the parameter 'address_number' is not an integer
            TypeError -- raises if the parameter 'address_street' is not a string
            TypeError -- raises if the parameter 'retail_category' is not a string
            TypeError -- raises if the parameter 'coordinates' is not a tuple
            ValueError -- raises if the parameter 'coordinates' does not contain exaclty 2 values
            TypeError -- raises if the parameter 'local_area' is not a string
        
        Returns:
            None
        '''
        if type(store_id) is not int:
            raise TypeError("TypeError: The parameter 'store_id' must be an integer")

        if type(business_name) is not str:
            raise TypeError("TypeError: The parameter 'business_name' must be an string")

        if type(address_unit) is not str:
            raise TypeError("TypeError: The parameter 'address_unit' must be a string")

        if type(address_number) is not int:
            raise TypeError("TypeError: The parameter 'address_number' must be an integer")

        if type(address_street) is not str:
            raise TypeError("TypeError: The parameter 'address_street' must be an string")

        if type(retail_category) is not str:
            raise TypeError("TypeError: The parameter 'retail_category' must be an string")

        if type(coordinates) is not tuple:
            raise TypeError("TypeError: The parameter 'coordinates' must be a tuple")

        if (len(coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in coordinates)):
            raise ValueError("ValueError: The parameter 'coordinates' must contain exactly 2 floats")

        if type(local_area) is not str:
            raise TypeError("TypeError: The parameter 'local_area' must be a string")

        self.store_id = store_id
        self.business_name = business_name    
        self.address_unit = address_unit
        self.address_number = address_number
        self.address_street = address_street
        self.retail_category = retail_category
        self.coordinates = coordinates
        self.local_area = local_area

        # A full address is generated when a 'Storefront' is instantiated
        self.full_address = str(self.address_number) + ADDRESS_SEPARATOR['number-to-street'] + self.address_street
        if self.address_unit != 'N/A':
            self.full_address = self.address_unit + ADDRESS_SEPARATOR['unit-to-number'] + self.full_address


    def __str__(self):
        '''
        Method Name: __str__
            Defines a string when a 'Storefront' object is converted to a string (ex. when
            the 'str' or 'print' function is called)
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'store_id' is not an integer
            TypeError -- raises if the attribute 'business_name' is not a string
            TypeError -- raises if the attribute 'full_address' is not a string
            TypeError -- raises if the attribute 'retail_category' is not a string
            TypeError -- raises if the attribute 'coordinates' is not a tuple
            ValueError -- raises if the attribute 'coordinates' does not contain exaclty 2 floats
            TypeError -- raises if the attribute 'local_area' is not a string
        
        Returns:
            str, the string used when 'str' or 'print' functions is called
        '''
        if type(self.store_id) is not int:
            raise TypeError("TypeError: The attribute 'store_id' of class 'Storefront' must be an integer")

        if type(self.business_name) is not str:
            raise TypeError("TypeError: The attribute 'business_name' of class 'Storefront' must be an string")

        if type(self.full_address) is not str:
            raise TypeError("TypeError: The attribute 'address' of class 'Storefront' must be an string")

        if type(self.retail_category) is not str:
            raise TypeError("TypeError: The attribute 'retail_category' of class 'Storefront' must be an string")

        if type(self.coordinates) is not tuple:
            raise TypeError("TypeError: The attribute 'coordinates' of class 'Storefront' must be a tuple")

        if (len(self.coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in self.coordinates)):
            raise ValueError("ValueError: The attribute 'coordinates' of class 'Storefront' must contain exactly 2 numeric float")

        if type(self.local_area) is not str:
            raise TypeError("TypeError: The attribute 'local_area' of class 'Storefront' must be a string")

        return (
            f"Store ID: {self.store_id}\n"
            f"Business Name: {self.business_name}\n"
            f"Address: {self.full_address}\n"
            f"Category: {self.retail_category}\n"
            f"Coordinates: {self.coordinates}\n"
            f"Local Area: {self.local_area}\n"
        )

    
    def __eq__(self, other):
        '''
        Method Name: __eq__
            Used to compare two 'Storefront' objects
        
        Parameters:
            other -- Storefront, object representing a storefront
        
        Raises:
            TypeError -- raises if the attribute 'store_id' is not an integer
        
        Returns:
            bool, True if the 'store_id' attributes are the same; False otherwise
        '''
        if (type(self.store_id) is not int) or (type(other.store_id) is not int):
            raise TypeError("TypeError: The attribute 'store_id' of class 'Storefront' must be an integer")
        return self.store_id == other.store_id
                    

