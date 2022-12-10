'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class Name -- LocalAreaBoundary, see docstring below

This file is used by the following:
local_area_boundary_factory.py
'''


COORDINATE_COUNT = 2 # Coordinates are represented by 2 values


class LocalAreaBoundary:
    '''
    Class Name: LocalAreaBoundary
        Object of this class holds the different category of data acquired
        from a dataset as its instance attributes. The parameters used to instantiate
        a 'LocalAreaBoundary' are the local area abbreciation (Map ID), the name of
        the neighbourhood, the coordinates which connects the boundary, and the
        coordinate of the centroid of the neighbourhood.

        The following methods are available:
        __init__ (constructor)
        __str__ 
        __eq__
    '''
    def __init__(self, abbreviation, name, list_boundary_coordinates, centroid_coordinates):
        '''
        Method Name: __init__
            Constructor for 'LocalAreaBoundary'
        
        Parameters:
            name -- str, local area boundary name
            coordinates -- tuple of (float, float), coordinates of local area boundary, in
                EPSG 26910 format, a local projected coordinate system in metres
            local_area -- str, the neighbourhood the station is located
        
        Raises:
            TypeError -- raises if the parameter 'abbreviation' is not a string
            TypeError -- raises if the parameter 'name' is not a string
            TypeError -- raises if the parameter 'list_boundary_coordinates' is not a list
            ValueError -- raises if the parameter 'list_boundary_coordintes' do not only contain tuples
            TypeError -- raises if the parameter 'centroid_coordinates' is not a tuple
            ValueError -- raises if the parameter 'centroid_coordinates' does not contain exaclty 2 float
        
        Returns:
            None
        '''
        if type(abbreviation) is not str:
            raise TypeError("TypeError: The parameter 'abbreviation' must be a string")

        if type(name) is not str:
            raise TypeError("TypeError: The parameter 'name' must be a string")

        if type(list_boundary_coordinates) is not list:
            raise TypeError("TypeError: The parameter 'list_boundary_coordinates' must be a list")

        if not all(type(coordinate) is tuple for coordinate in list_boundary_coordinates):
            raise ValueError("ValueError: The parameter 'list_boundary_coordinates' must contain only tuples")

        if type(centroid_coordinates) is not tuple:
            raise TypeError("TypeError: The parameter 'centroid_coordinates' must be a tuple")

        if (len(centroid_coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in centroid_coordinates)):
            raise ValueError("ValueError: The parameter 'centroid_coordinates' must contain exactly 2 floats")

        self.abbreviation = abbreviation
        self.name = name
        self.list_boundary_coordinates = list_boundary_coordinates
        self.centroid_coordinates = centroid_coordinates

    
    def __str__(self):
        '''
        Method Name: __str__
            Defines a string when a 'LocalAreaBoundary' object is converted to a string (ex. when
            the 'str' or 'print' function is called)
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'abbreviation' is not a string
            TypeError -- raises if the attribute 'name' is not a string
            TypeError -- raises if the attribute 'centroid_coordinates' is not a tuple
            ValueError -- raises if the attribute 'centroid_coordinates' does not contain exaclty 2 float
        
        Returns:
            str, the string used when 'str' or 'print' functions is called
        '''
        if type(self.abbreviation) is not str:
            raise TypeError("TypeError: The attribute 'abbreviation' must be a string")

        if type(self.name) is not str:
            raise TypeError("TypeError: The attribute 'name' must be a string")

        if type(self.centroid_coordinates) is not tuple:
            raise TypeError("TypeError: The attribute 'centroid_coordinates' must be a tuple")

        if (len(self.centroid_coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in self.centroid_coordinates)):
            raise ValueError("ValueError: The attribute 'centroid_coordinates' must contain exactly 2 floats")

        return (
            f"Abbreviation: {self.abbreviation}\n"
            f"Name: {self.name}\n"
            f"Coordinates of Centroid: {self.centroid_coordinates}\n"
        )

    
    def __eq__(self, other):
        '''
        Method Name: __eq__
           Used to compare two 'LocalAreaBoundary' objects
        
        Parameters:
            other -- LocalAreaBoundary, object representing a local area boundary
        
        Raises:
            TypeError -- raises if the attribute 'name' is not a string
        
        Returns:
            bool, True if the 'station_name' attributes are the same; False otherwise
        '''
        if (type(self.name) is not str) or (type(other.name) is not str):
            raise TypeError("TypeError: The attribute 'name' of class 'LocalAreaBoundary' must be a string")

        return self.name == other.name