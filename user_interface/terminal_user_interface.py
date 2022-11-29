'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class Name -- TerminalUserInterface, see docstring below

These functions are used by the driver file:
data_dashboard.py
'''

# Module
import user_interface.dataset_table_printer as dataset_table_printer


# Constants used for menu display
DEFAULT_MAX_DISPLAY_COUNT = 10
DEFAULT_SEARCH_RADIUS = 0.0
DEFAULT_STORE_CATEGORY = 'All'
HEADER_LINE_SYMBOL = '-'
MENU_CHARACETER = '-'
MENU_EXTRA_LENGTH = 5
MENU_MIN_LENGTH = 30
MENU_START_INDEX = 1
MIN_DISPLAY_COUNT = 1
MAX_DISPLAY_COUNT = 100
MIN_SEARCH_RADIUS = 0 # The value 0 used to represents infinite search radius
UNUSED_STORE_CATEGORY = ['Vacant', 'Vacant UC', 'Unknown']
ADDITIONAL_STORE_CATEGORY = 'All'


class TerminalUserInterface:
    '''
    Class Name: TerminalUserInterface
        This class represents the terminal user interface which interacts with
        a user to prompt for input and display output to the user in the
        terminal.

        The following methods are available:
        __init__ (Constructor)
        __str__
        __eq__
        display_input_summary
        display_loading_message
        display_nearby_stores
        poplulate_interface_menu
        start_user_interface 
        __display_header
        __display_instructions
        __display_list
        __display_menu_store_categories
        __display_menu_transit_stations
        __generate_list_station_names
        __generate_list_store_categories
        __prompt_max_display_count
        __prompt_search_radius
        __prompt_store_category
        __prompt_user_integer_input
    '''
    def __init__(self, user_input):
        '''
        Method Name: __init__
            Constructor for 'TerminalUserInterface'
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        self.name = 'Terminal User Interface'
        self.user_input = user_input
        self.__list_transit_stations = [] # Placeholder empty list, for menu display
        self.__list_storefronts = [] # Placeholder empty list, for menu display
        self.__list_station_names = [] # Placeholder empty list, for menu display
        self.__list_store_categories = [] # Placeholder empty list, for menu display

        
    def __str__(self):
        '''
        Method Name: __str__
            Defines a string when a 'TerminalUserInterface' object is converted to a string
            (ex. when calling the 'str' and 'print' function)
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'name' is not a string
        
        Returns:
            str, the string used when 'str' or 'print' function is called
        '''
        if type(self.name) is not str:
            raise TypeError("TypeError: The attribute 'name' must be a string")
        return (
                f"{self.name}"
            )
    

    def __eq__(self, other):
        '''
        Method Name: __eq__
            Used to compare two 'TerminalUserInterface' objects
        
        Parameters:
            other -- TerminalUserInterface, object representing a terminal user interface
        
        Raises:
            TypeError -- raises if the attributes 'name' is not a string
        
        Returns:
            bool, True if the attributes 'name' are the same, False otherwise
        '''
        if (type(self.name) is not str) or (type(other.name) is not str):
            raise TypeError("TypeError: The attribute 'name' must be a string")
        
        return (self.name == other.name)


    def display_input_summary(self):
        '''
        Function Name: display_input_summary
            Displays a summary of the user's input
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        print(self.user_input)


    def display_loading_message(self):
        '''
        Method Name: display_loading_message
            Display a loading message in the terminal
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        print('The program is currently retrieving and processing data. Please wait...')
        

    def display_nearby_stores(self, list_nearby_stores):
        '''
        Method Name: display_nearby_stores
            Display a list of nearby stores
        
        Parameters:
            list_nearby_stores -- list of NearbyStore, a list of 'NearbyStore' objects
        
        Raises:
            TypeError -- raises if the parameter 'list of NearbyStores' is not a list
            TypeError -- raises if the value of key 'max display count' must be an integer
        
        Returns:
            None
        '''
        if type(list_nearby_stores) is not list:
            raise TypeError("TypeError: The parameter 'list_nearby_stores' must be a list")
        
        if type(self.user_input.max_display_count) is not int:
            raise TypeError("TypeError The value of key 'max display count' must be an integer")
        
        dataset_table_printer.print_nearby_store(list_nearby_stores, self.user_input.max_display_count)


    def populate_menus(self, list_transit_stations, list_storefronts):
        '''
        Method Name: opulate_menus
            Assign information from a list of 'TransitStation' objects and a list of 'Storefront'
            objects to attributes of the 'TerminalUserInterface' class
        
        Parameters:
            list_transit_stations -- TransitStation, a list of 'TransitStation' objects
            list_storefronts -- Storefront, a list of 'Storefront' objects
        
        Raises:
            TypeError -- raises if the parameter 'list_transit_stations' is not a list
            ValueError -- raises if the parameter 'list_transit_stations' is an empty list
            TypeError -- raises if the parameter 'list_storefronts' is not a list
            ValueError -- raises if the parameter 'list_storefronts' is an empty list
        
        Returns:
        '''
        if type(list_transit_stations) is not list:
            raise TypeError("TypeError: The parameter 'list_transit_stations' must be a list")
        
        if len(list_transit_stations) == 0:
            raise ValueError("ValueError: The parameter 'list_transit_stations' cannot be empty")
        
        if type(list_storefronts) is not list:
            raise TypeError("TypeError: The parameter 'list_storefronts' must be a list")
        
        if len(list_storefronts) == 0:
            raise ValueError("ValueError: The parameter 'list_storefronts' cannot be empty")
        
        self.__list_transit_stations = list_transit_stations
        self.__list_storefronts = list_storefronts
                

    def start_user_interaction(self):
        '''
        Method Name: start_user_interaction
            Commences interaction between terminal and user. Displays menus and prompts
            users for input. The inputs in the terminal are stored as attributes in the
            'TerminalUserInterface' object.
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            Nothing
        '''
        self.__display_instructions()
        self.__display_menu_transit_stations()
        # Menu shows input numbered from 1 to n (instead of 0 to n-1) so the
        # index is 1 less than the user input
        self.user_input.transit_station = self.__list_transit_stations[self.prompt_transit_station() - 1]
        self.__display_menu_store_categories()
        # Menu shows input numbered from 1 to n (instead of 0 to n-1) so the
        # index is 1 less than the user input
        self.user_input.store_category = self.__list_store_categories[self.__prompt_store_category() - 1]
        self.user_input.search_radius = self.__prompt_search_radius()
        self.user_input.max_display_count = self.__prompt_max_display_count()
        print()
    

    def __display_header(self, header_text):
        '''
        Method Name: __display_header
            Display a header in the terminal
        
        Parameters:
            header_text -- str, the text to be displayed in the header
        
        Raises:
            TypeError -- raises if the parameter 'header_text' is not a string
        
        Returns:
            None
        '''
        if type(header_text) is not str:
            raise TypeError("TypeError: The parameter 'header_text' must be a string")
        
        print(HEADER_LINE_SYMBOL * len(header_text))
        print(header_text)
        print(HEADER_LINE_SYMBOL * len(header_text))


    def __display_instructions(self):
        '''
        Method Name: __display_header
            Display a list of instructions in the terminal
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        self.__display_header("Instructions")
        print("This program searches for nearby stores given a Transit Station in the City of Vancouver:\n"
            "1. Select a Transit Station.\n"
            "2. Select a store category to filter.\n"
            "3. Specify a search radius in metres.\n"
            "4. Specify the maximum number of stores to display.\n"
            )
        

    def __display_list(self, list_text):
        '''
        Method Name: __display_list
            Display a list in the termianl
        Parameters:
            list_text -- list of str, list of text to display
        
        Raises:
            TypeError -- raises if parameter 'list_text' is not a list
            ValueError -- raises if parameter 'list_text' is an empty list
        
        Returns:
            None
        '''
        if type(list_text) is not list:
            raise TypeError("TypeError: The parameter 'list_text' must be a list")
        if len(list_text) == 0:
            raise ValueError("ValueError: The parameter 'list_text' is empty")

        # Ensure menu width is greater than all text entries
        max_text_length = MENU_MIN_LENGTH - MENU_EXTRA_LENGTH
        for entry in list_text:
            if len(entry) > max_text_length:
                max_text_length = len(entry)

        for i in range(len(list_text)):
            print(f"{(list_text[i] + '').ljust(max_text_length + MENU_EXTRA_LENGTH, '-')} {i + MENU_START_INDEX}")
        print()
                
 
    def __display_menu_store_categories(self):
        '''
        Method Name: __display_menu_store_categories
            Display a menu of store categories
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.__display_header('List of Store Categories')
        self.__generate_list_store_categories()
        self.__display_list(self.__list_store_categories)

        
    def __display_menu_transit_stations(self):
        '''
        Method Name: __display_menu_transit_stations
            Display a menu of transit_stations
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        self.__display_header('List of Transit Stations')
        self.__generate_list_station_names()
        self.__display_list(self.__list_station_names)
    

    def __generate_list_station_names(self):
        '''
        Method Name: __generate_list_station_names
            Generate a list of transit station names from a list of 'TransitStation' objects
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if attribute 'list_transit_stations' is not a list
            ValueError -- raises if attribute 'list_transit_stations' is an empty list
        
        Returns:
            None
        '''
        if type(self.__list_transit_stations) is not list:
            raise TypeError("TypeError: The attribute 'list_transit_stations' must be a list")
        
        if len(self.__list_transit_stations) == 0:
            raise ValueError("ValueError: The attribute 'list_transit_stations' cannot be empty")

        list_station_name = []
        for station in self.__list_transit_stations:
            list_station_name.append(station.station_name)
        
        self.__list_station_names = list_station_name
    

    def __generate_list_store_categories(self):
        '''
        Method Name: __generate_list_store_categories
            Generate a list of store categories form a list of 'Storefront' objects
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if attribute 'list_storefront' is not a list
            ValueError -- raises if attribute 'list_storefront' is an empty list
        
        Returns:
        '''
        if type(self.__list_storefronts) is not list:
            raise TypeError("TypeError: The attribute 'list_storefronts' must be a list")
        
        if len(self.__list_storefronts) == 0:
            raise ValueError("ValueError: The attribute 'list_storefronts' cannot be empty")

        list_store_categories = []
        for store in self.__list_storefronts:
            if (store.retail_category not in list_store_categories) and (store.retail_category not in UNUSED_STORE_CATEGORY):
                list_store_categories.append(store.retail_category)

        list_store_categories.append(ADDITIONAL_STORE_CATEGORY)
        self.__list_store_categories = list_store_categories
 
        
    def __prompt_max_display_count(self):
        '''
        Method Name: __prompt_max_display_count
           Prompt user for a maximum number of entries to display in the results
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            int, user input
        '''
        return self.__prompt_user_integer_input(f"the maximum number of stores to display (max: {MAX_DISPLAY_COUNT})", MIN_DISPLAY_COUNT, MAX_DISPLAY_COUNT)


    def __prompt_search_radius(self):
        '''
        Method Name: __prompt_max_display_count
           Prompt user for a maximum number of entries to display in the results
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            float, user input
        '''
        user_input = 0
        is_valid_input = False
        while not is_valid_input:
            user_input = input("Please enter a search radius in metres (or enter 0 to search all): ")

            try:
                user_input = float(user_input)
            except ValueError:
                print("Input must be a number")
            else:
                if user_input < 0:
                    print("Input must be a positive number (or enter 0 to search all)")
                else:
                    is_valid_input = True
        
        return user_input
                    

    def __prompt_store_category(self):
        '''
        Method Name: __prompt_store_category
           Prompt for an integer corresponding to a store category
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if attribute 'list_store_categories' is not a list
            ValueError -- raises if attribute 'list_store_categories' is an empty list
     
        Returns:
            int, user input
        '''
        if type(self.__list_store_categories) is not list:
            raise TypeError("TypeError: The attribute 'list_store_categories' must be a list")
        
        if len(self.__list_store_categories) == 0:
            raise ValueError("ValueError: The attribute 'list_store_categories' cannot be empty")

        object_prompt = 'an integer corresponding to the store category'
        return self.__prompt_user_integer_input(object_prompt, MENU_START_INDEX, len(self.__list_store_categories))

    
    def prompt_transit_station(self):
        '''
        Method Name: prompt_transit_station
           Prompt for an integer corresponding to a transit station
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if attribute 'list_station_names' is not a list
            ValueError -- raises if attribute 'list_station_names' is an empty list
        
        Returns:
            int, user input
        '''
        if type(self.__list_station_names) is not list:
            raise TypeError("TypeError: The attribute 'list_station_names' must be a list")
        
        if len(self.__list_station_names) == 0:
            raise ValueError("ValueError: The attribute 'list_station_names' cannot be empty")

        object_prompt = 'an integer corresponding to the transit station'
        return self.__prompt_user_integer_input(object_prompt, MENU_START_INDEX, len(self.__list_station_names))

   
     
    def __prompt_user_integer_input(self, prompt_subject, min_input, max_input):
        '''
        Method Name: __prompt_user_integer_input
            Prompt user for an integer input within a specified minimum an maxmimum value
        
        Parameters:
            prompt_subject -- str, the subject of the input asked to the user
            min_input -- int, minimum value of input
            max_input -- int, maximum value of input
        
        Raises:
            TypeError -- raises if the parameter 'prompt_subject' is not a string
            TypeError -- raises if the parameter 'min_input' is not an integer
            TypeError -- raises if the parameter 'max_input' is not an integer
        
        Returns:
            int, user input
        '''
        if type(prompt_subject) is not str:
            raise TypeError("TypeError: The parameter 'prompt_subject' must be a string")
        
        if type(min_input) is not int:
            raise TypeError("TypeError: The parameter 'min_input' must be an integer")
        
        if type(max_input) is not int:
            raise TypeError("TypeError: The parameter 'max_input' must be an integer")
        
        user_input = 0
        is_valid_input = False
        while not is_valid_input:
            user_input = input(f"Please enter {prompt_subject}: ")

            try:
                user_input = int(user_input)
            except ValueError:
                print(f"Input must be a positive integer")
            else:
                if (user_input < min_input) or (user_input > max_input):
                    print(f"Input must be an integer between {min_input} to {max_input}")
                else:
                    is_valid_input = True
        
        return user_input