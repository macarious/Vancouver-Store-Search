'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class UserInput -- see docstring below

This file is used by the following:
graphical_user_input.py
'''


DEFAULT_MAX_DISPLAY_COUNT = 50
DEFAULT_SEARCH_RADIUS = 0.0
DEFAULT_STORE_CATEGORY = 'All'


class UserInput:
    '''
    Class Name: UserInputInventory
        Object of this class represents the all the user input. Instances
        of a 'UserInput' object includes: a transit station, a store category,
        a search radius, and the number of stores to display.

        The following methods are available:
            __init__ (constructor)
            __str__
            __eq__
    '''
    def __init__(self):
        '''
        Method Name: __init__
            Constructor for 'UserInput'
        
        Parameters:
            transit_station -- TransitStation, transit station selected by user
            store_category -- str, store category selected by user
            search radius -- float, search radius input by user, in metres
            display_count -- int, number of stores user want to display
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        self.name = 'User Input'
        self.transit_station = None
        self.store_category = DEFAULT_STORE_CATEGORY
        self.search_radius = DEFAULT_SEARCH_RADIUS
        self.max_display_count = DEFAULT_MAX_DISPLAY_COUNT


    def __str__(self):
        '''
        Function Name: __str__
            Defines a string when a 'UserInput' object is converted to a string
            (ex. when calling the 'str' and 'print' function)
        
        Parameters:
            Nothing
        
        Raises:
            ValueError -- raises if no transit station has been selected
            TypeError -- raises if the attribute 'name' is not a string
            TypeError -- raises if the attribute 'station_name' of class 'TransitStation' is not a string
            TypeError -- raises if the attribute 'store_category' is not a string
            TypeError -- raises if the attribute 'search_radius' is not a float
            TypeError -- raises if the attribute 'max_display_count' is not an integer
        
        Returns:
            str, the string used when 'str' or 'print' function is called
        '''
        if self.transit_station is None:
            raise ValueError("ValueError: No transit station has been selected")

        if type(self.name) is not str:
            raise TypeError("TypeError: The attribute 'name' must be a string")

        if type(self.transit_station.station_name) is not str:
            raise TypeError("TypeError: The attribute 'station_name' of class 'TransitStation' must be a string")

        if type(self.store_category) is not str:
            raise TypeError("TypeError: The attribute 'store_category' must be a string")

        if type(self.search_radius) is not float:
            raise TypeError("TypeError: The attribute 'search_radius' must be a float")

        if type(self.max_display_count) is not int:
            raise TypeError("TypeError: The attribute 'max_display_count' must be an integer")

        search_radius_text = '{:.1f}'.format(self.search_radius)
        if self.search_radius == 0:
            search_radius_text = 'infinite'

        return (
            f"{self.name}\n"
            f"Transit Station: {self.transit_station.station_name}\n"
            f"Store Category: {self.store_category}\n"
            f"Search Radius: {search_radius_text}\n"
            f"Max Display: {self.max_display_count}\n"
        )


    def __eq__(self, other):
        '''
        Method Name: __eq__
            Used to compare two 'UserInput' objects
        
        Parameters:
            other -- UserInput, object containing user input
        
        Raises:
            TypeError -- raises if the parameter 'other' is not a UserInput object
            TypeError -- raises if the attribute 'name' is not a string
            TypeError -- raises if the attribute 'station_name' of class 'TransitStation' is not a string
            TypeError -- raises if the attribute 'store_category' is not a string
            TypeError -- raises if the attribute 'search_radius' is not a float
            TypeError -- raises if the attribute 'max_display_count' is not an integer
        
        Returns:
            bool, True if all attributes are the same, False otherwise
        '''
        if type(other) is not UserInput:
            raise TypeError("TypeError: The parameter 'other' must be a 'UserInput' object")

        if (type(self.name) is not str) or (type(other.name) is not str):
            raise TypeError("TypeError: The attribute 'name' must be a string")

        if (type(self.transit_station.station_name) is not str) or (type(other.transit_station.station_name) is not str):
            raise TypeError("TypeError: The attribute 'station_name' of class 'TransitStation' must be a string")

        if (type(self.store_category) is not str) or (type(other.store_category) is not str):
            raise TypeError("TypeError: The attribute 'store_category' must be a string")

        if (type(self.search_radius) is not float or (type(other.search_radius) is not float)):
            raise TypeError("TypeError: The attribute 'search_radius' must be a float")

        if (type(self.max_display_count) is not int) or (type(other.max_display_count) is not int):
            raise TypeError("TypeError: The attribute 'max_display_count' must be an integer")

        return (
            (self.name == other.name) and
            (self.transit_station == other.transit_station) and
            (self.store_category == other.store_category) and
            (self.search_radius == other.search_radius) and
            (self.max_display_count == other.max_display_count)
        )
