'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class Name -- NearbyStore, see docstring below

This class is used by the following:
nearby_stores_finder.py
'''


DISTANCE_UNIT = 'm'


class NearbyStore:
    '''
    Class Name: NearbyStore
        Object of this class represent a nearby store relative to a transit station.
        The parameters used to instantiate a 'NearbyStore' are a 'Storefront' instance,
        a 'TransitStation' instance representing the origin transit station, distance
        from the 'Storefront' to the origin 'TransitStation', and the retail category of
        the 'Storefront'.

        The following methods are available:
        __init__ (constructor)
        __str__ 
        __eq__
    '''
    def __init__(self, storefront, origin_transit_station, distance, retail_category = 'All'):
        '''
        Method Name: __init__
            Constructor used to instantiate NearbyStore' objects
        
        Parameters:
            storefront -- Storefront, an instance of class 'Storefront'
            origin_station -- TransitStation, the station of origin
            distance -- float, the distance between the origin_station and the storefront
            retail_category -- str, the retail category of the nearby store
        
        Raises:
            TypeError -- raises if the parameter 'distance' is not a float
            TypeError -- raises if the parameter 'retail_category' is not a string
        
        Returns:
            None
        '''
        if type(distance) is not float:
            raise TypeError("TypeError: The attribute 'distance' of class 'NearbysStore' must be a float")
        
        if type(retail_category) is not str:
            raise TypeError("TypeError: The attribute 'retail_category' of class 'NearbysStore' must be a string")

        self.storefront = storefront
        self.origin_station = origin_transit_station
        self.distance = distance
        self.retail_category = retail_category


    def __str__(self):
        '''
        Method Name: __str__
            Defines a string when a 'NearbyStore' object is converted to a string (ex. when
            the 'str' or 'print' function is called)
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'business_name' of class 'Storefront' is not a string
            TypeError -- raises if the attribute 'origin_station' of class 'TransitStation' is not a string
            TypeError -- raises if the attribute 'distance' of class 'NearbyStore' is not a float
            TypeError -- raises if the attribute 'retail_category' of class 'Storefront' is not a string

        Returns:
            str, the string used when 'str' or 'print' functions is called
        '''
        if type(self.storefront.business_name) is not str:
            raise TypeError("TypeError: The attribute 'business_name' of class 'Storefront' must be a string")
        
        if type(self.origin_station) is not str:
            raise TypeError("TypeError: The attribute 'origin_station' of class 'NearbysStore' must be a string")

        if type(self.distance) is not float:
            raise TypeError("TypeError: The attribute 'distance' of class 'NearbysStore' must be a float")
        
        if type(self.retail_category) is not str:
            raise TypeError("TypeError: The attribute 'retail_category' of class 'NearbysStore' must be a string")

        return (
            f"Nearby Store: {self.storefront.business_name}\n"
            f"origin_station: {self.origin_station.station_name}\n"
            f"Distance: {self.distance:.4f} {DISTANCE_UNIT}\n"
            f"Retail Type: {self.storefront.retail_category}\n"
        )

    
    def __eq__(self, other):
        '''
        Method Name: __eq__
           Used to compare two 'NearbyStore' objects
        
        Parameters:
            other -- NearbyStore, object representing a nearby store
        
        Raises:
            Nothing
        
        Returns:
            bool, True if the 'storefront' and 'origin_station' attributes are the same; False otherwise
        '''
        return (
                (self.storefront == other.storefront) and
                (self.origin_station == other.origin_station)
        )