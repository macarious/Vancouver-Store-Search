'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class Name -- TransitStation, see docstring below

This file is used by the following:
transit_station_factory
'''


COORDINATE_COUNT = 2 # Coordinates are represented by 2 values


class TransitStation:
    '''
    Class Name: TransitStation
        Object of this class holds the different category of data acquired
        from a dataset as its instance attributes. The parameters used to instantiate
        a 'TransitStation' are the transit station name, the coordinates, and the
        local area. This class can also calculate the distance from a given pair of
        coordinates to the 'TransitStation'.

        The following methods are available:
        __init__ (constructor)
        __str__ 
        __eq__
        calculate_distance_to
    '''
    def __init__(self, name, coordinates, local_area):
        '''
        Method Name: __init__
            Constructor for 'TransitStation'
        
        Parameters:
            name -- str, transit station name
            coordinates -- tuple of (float, float), coordinates of transit station, in
                EPSG 26910 format, a local projected coordinate system in metres
            local_area -- str, the neighbourhood the station is located
        
        Raises:
            TypeError -- raises if the parameter 'name' is not a string
            TypeError -- raises if the parameter 'coordinates' is not a tuple
            ValueError -- raises if the parameter 'coordinates' does not contain exaclty 2 float
            TypeError -- raises if the parameter 'local_area' is not a string
        
        Returns:
            None
        '''
        if type(name) is not str:
            raise TypeError("TypeError: The parameter 'name' must be a string")

        if type(coordinates) is not tuple:
            raise TypeError("TypeError: The parameter 'coordinates' must be a tuple")

        if (len(coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in coordinates)):
            raise ValueError("ValueError: The parameter 'coordinates' must contain exactly 2 floats")

        if type(local_area) is not str:
            raise TypeError("TypeError: The parameter 'local_area' must be a string")

        self.station_name = name
        self.coordinates = coordinates
        self.local_area = local_area
        self.nearby_stores = [] # Used in analysis

    
    def __str__(self):
        '''
        Method Name: __str__
            Defines a string when a 'TransitStation' object is converted to a string (ex. when
            the 'str' or 'print' function is called)
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'station_name' is not a string
            TypeError -- raises if the attribute 'coordinates' is not a tuple
            ValueError -- raises if the attribute 'coordinates' does not contain exactly 2 floats
            TypeError -- raises if the attribute 'local_area'  is not a string
        
        Returns:
            str, the string used when 'str' or 'print' functions is called
        '''
        if type(self.station_name) is not str:
            raise TypeError("TypeError: The attribute 'name' of class 'TransitStation' must be a string")

        if type(self.coordinates) is not tuple:
            raise TypeError("TypeError: The attribute 'coordinates' of class 'TransitStation' must be a tuple")

        if (len(self.coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in self.coordinates)):
            raise ValueError("ValueError: The attribute 'coordinates' of class 'TransitStation' must contain exactly 2 floats")

        if type(self.local_area) is not str:
            raise TypeError("TypeError: The attribute 'local_area' of class 'TransitStation' must be a string")

        return (
            f"Name: {self.station_name}\n"
            f"Coordinates: {self.coordinates}\n"
            f"Local Area: {self.local_area}\n"
        )

    
    def __eq__(self, other):
        '''
        Method Name: __eq__
           Used to compare two 'TransitStation' objects
        
        Parameters:
            other -- TransitStation, object representing a transit station
        
        Raises:
            TypeError -- raises if the attribute 'station_name' is not a string
        
        Returns:
            bool, True if the 'station_name' attributes are the same; False otherwise
        '''
        if (type(self.station_name) is not str) or (type(other.station_name) is not str):
            raise TypeError("TypeError: The attribute 'name' of class 'TransitStation' must be a string")

        return self.station_name == other.station_name


    def calculate_distance_to(self, destination_coordinates):
        '''
        Method Name: calculate_distance_to
            Calculates the distance from a given coordinates to a 'TransitStation'
        
        Parameters:
            destination_coordinates -- tuple of (float, float), coordinates of destination,
                in EPSG 26910 format, a local projected coordinate system in metres
        
        Raises:
            TypeError -- raises if the attribute 'coordinates' of class 'TransitStation' is not a tuple
            TypeError -- raises if the parameter 'destination_coordinates' is not a tuple
            ValueError -- raises if the attribute 'coordinates' of class 'TransitStation' does not contain exaclty 2 values
            ValueError -- raises if the parameter 'destination_coordinates' does not contain exaclty 2 values
            TypeError -- raises if the attribute 'coordinates' of class 'TransitStation' does not contain all floats
            TypeError -- raises if the parameter 'destination_coordinates' does not contain all floats
        
        Returns:
            float, a distance between distination and transit station, in metres
        '''
        if type(self.coordinates) is not tuple or type(destination_coordinates) is not tuple:
            raise TypeError("TypeError: The attribute 'coordinates' of class 'TransitStation' must be a tuple")

        if (
            (len(self.coordinates) != COORDINATE_COUNT) or
            (len(destination_coordinates) != COORDINATE_COUNT) or
            (not all(type(value) is float for value in self.coordinates)) or
            (not all(type(value) in (int, float) for value in destination_coordinates))
            ):
            raise ValueError("ValueError: The attribute 'coordinates' of class 'TransitStation' must contain exactly 2 floats")

        if (not all(type(value) is float for value in self.coordinates)) or (not all(type(value) in (int, float) for value in destination_coordinates)):
            raise TypeError("TypeError: The attribute 'coordinates' of class 'TransitStation' must contain exactly 2 floats")

       # Formula to calculate distance between two points:
       # Distance = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
        return ((self.coordinates[0] - destination_coordinates[0]) ** 2 + (self.coordinates[1] - destination_coordinates[1]) ** 2) ** 0.5