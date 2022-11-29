'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class Name -- GraphicalUserInterface, see docstring below

These functions are used by the driver file:
data_dashboard.py
'''

# Module
from tkinter import *
from tkinter import ttk
from nearby_stores_finder import find_nearby_stores
import user_interface.dataset_table_printer as dataset_table_printer


DEFAULT_GRID_CONFIG = {
    'sticky' : NSEW,
    'ipadx' : 2,
    'ipady' : 2,
    'padx' : 2,
    'pady' : 2,
}
DEFAULT_PACK_CONFIG = {
    'fill' : BOTH,
    'ipadx' : 5,
    'ipadx' : 5,
    'padx' : 5,
    'pady' : 5,
}
FRAME_TITLE = {
    'width' : 0,
    'height' : 24,
    'relief' : SOLID
}
LABELFRAME_MESSAGE_DISPLAY = {
    'text' : 'Status/Messages',
    'width' : 480,
    'height' : 40,
    'relief' : SOLID,
}
LABELFRAME_INSTRUCTIONS = {
    'text' : 'Instructions',
    'width' : 480,
    'height' : 80,
    'relief' : SOLID
}
LABELFRAME_STATION_CONTROL = {
    'text' : 'Transit Stations',
    'width' : 200,
    'height' : 80,
    'relief' : SOLID
}
LABELFRAME_CATEGORY_CONTROL = {
    'text' : 'Store Categories',
    'width' : 200,
    'height' : 80,
    'relief' : SOLID
}
LABELFRAME_SEARCH_RADIUS_CONTROL = {
    'text' : 'Search Radius',
    'width' : 360,
    'height' : 40,
    'relief' : SOLID
}
LABELFRAME_DISPLAY_COUNT_CONTROL = {
    'text' : 'Max Item to Display',
    'width' : 360,
    'height' : 40,
    'relief' : SOLID
}
FRAME_SEARCH_BUTTON_CONTROL = {
    'width' : 400,
    'height' : 40,
    'relief' : FLAT
}
LABELFRAME_OUTPUT_DISPLAY = {
    'text' : 'Output',
    'width' : 640,
    'height' : 460,
    'relief' : SOLID
}
LABEL_TITLE = {
    'text' : "City of Vancouver - Store Finder Dashboard\nCS5001 - Final Project",
    'font': ('Arial', 16, "bold")
}
LABEL_AUTHOR = {
    'text' : "HUI, Macarious Kin Fung",
    'font' : ('Arial', 12)
}
LABEL_INSTRUCTIONS = {
    'text': "This program searches for nearby stores around a Transit Station in the City of Vancouver:\n\n"
    "1. Select a Transit Station.\n"
    "2. Select a store category to filter.\n"
    "3. Specify a search radius in metres.\n"
    "4. Specify the maximum number of stores to display.\n",
    'wraplength': 400,
}
LABEL_LOADING_MESSAGE_START = {
    'text' : 'The program is currently retrieving and processing data.\nPlease wait...',
    'wraplength' : 400,
    'foreground' : 'red',
}
LABEL_LOADING_MESSAGE_WAIT = {
    'text' : 'The program has finished retrieving and processing the data.\nPlease continue...',
    'foreground' : 'sea green',
}
COMBOBOX_STATION_CONTROL = {
    'state' : 'readonly',
}
COMBOBOX_CATEGORY_CONTROL = {
    'state' : 'readonly',
}
SCALE_SEARCH_RADIUS = {
    'orient' : 'horizontal',
    'from_' : 0,
    'to' : 50000,
    'state' : 'disabled',
    'length' : 300,
}
LABEL_SEARCH_RADIUS = {
    'text' : 'Search All',
    'font' : ('Arial', 10),
    'width' : 10,
}
SCALE_DISPLAY_COUNT = {
    'orient' : 'horizontal',
    'from_' : 10,
    'to' : 100,
    'state' : 'disabled',
    'length' : 300,
}
LABEL_DISPLAY_COUNT = {
    'text' : 10,
    'font' : ('Arial', 10),
    'width' : 10,
}
BUTTON_SEARCH = {
    'text' : 'SEARCH',
    'state' : 'disabled',
}
SCROLLBAR_OUTPUT_DISPLAY = {
        'orient' : VERTICAL
}
TREEVIEW_OUTPUT = {
    'height' : 20
}
HEADER_LIST_NEARBY_STORE = [
    'Store Name',
    'Distance',
    'Address',
    'Retail Category',
]
DISTANCE_UNIT = 'm'
ADDITIONAL_STORE_CATEGORY = 'All'
UNUSED_STORE_CATEGORY = [
        'Vacant',
        'Vacant UC',
        'Unknown'
]



class GraphicalUserInterface:
    '''
    Class Name: GraphicalUserInterface
        This class represents the graphical user interface which interacts with
        a user to prompt for input and display output to the user graphically.

        The following methods are available:
        __init__ (Constructor)
        __str__
        __eq__
        display_loading_message
        display_nearby_stores
        poplulate_interface_menu
        start_user_interface
        __configure_style
        __generate_list_station_names
        __generate_list_store_categories
        __set_grid_configuration
        __update_label_search_radius
        __update_label_display_count
    '''
    def __init__(self, user_input):
        '''
        Method Name: __init__
            Constructor for 'GraphicalUserInterface'
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        self.name = 'Graphical User Interface'
        self.user_input = user_input

        self.__list_transit_stations = [] # Placeholder empty list, for menu display
        self.__list_storefronts = [] # Placeholder empty list, for menu display
        self.__list_station_names = [] # Placeholder empty list, for menu display
        self.__list_store_categories = [] # Placeholder empty list, for menu display
        self.__list_nearby_stores = []  # Placeholder empty list, for menu display
        # Create tk object - root level
        self.master = Tk()
        self.master.title("Store Finder Dashboard")

        self.__set_grid_configurations()
        self.__configure_style()

        # Build frames and labelled frames -- level 1
        self.frame_title = ttk.Frame(self.master, **FRAME_TITLE)
        self.labelframe_message_display = ttk.Labelframe(self.master, **LABELFRAME_MESSAGE_DISPLAY)
        self.labelframe_instructions = ttk.Labelframe(self.master, **LABELFRAME_INSTRUCTIONS)
        self.labelframe_station_control = ttk.Labelframe(self.master, **LABELFRAME_STATION_CONTROL)
        self.labelframe_category_control = ttk.Labelframe(self.master, **LABELFRAME_CATEGORY_CONTROL)
        self.labelframe_search_radius_control = ttk.Labelframe(self.master, **LABELFRAME_SEARCH_RADIUS_CONTROL)
        self.labelframe_display_count_control = ttk.Labelframe(self.master, **LABELFRAME_DISPLAY_COUNT_CONTROL)
        self.frame_search_button_control = ttk.Frame(self.master, **FRAME_SEARCH_BUTTON_CONTROL)
        self.labelframe_output_display = ttk.Labelframe(self.master, **LABELFRAME_OUTPUT_DISPLAY)

        # Place widgets, grid -- level 1
        self.frame_title.grid(column = 0, row = 0, columnspan = 6, **DEFAULT_GRID_CONFIG)
        self.labelframe_message_display.grid(column = 0, row = 1, columnspan = 4, **DEFAULT_GRID_CONFIG)
        self.labelframe_instructions.grid(column = 0, row = 2, columnspan = 4, **DEFAULT_GRID_CONFIG)
        self.labelframe_station_control.grid(column = 0, row = 3, columnspan = 2, **DEFAULT_GRID_CONFIG)
        self.labelframe_category_control.grid(column = 2, row = 3, columnspan = 2, **DEFAULT_GRID_CONFIG)
        self.labelframe_search_radius_control.grid(column = 0, row = 4, columnspan = 4, **DEFAULT_GRID_CONFIG)
        self.labelframe_display_count_control.grid(column = 0, row = 5, columnspan = 4, **DEFAULT_GRID_CONFIG)
        self.frame_search_button_control.grid(column = 1, row = 6, columnspan = 2, **DEFAULT_GRID_CONFIG)
        self.labelframe_output_display.grid(column = 4, row = 1, columnspan = 2, rowspan = 6, **DEFAULT_GRID_CONFIG)

        # Place label in frame_title, and pack them -- level 2
        self.label_title = ttk.Label(self.frame_title, **LABEL_TITLE)
        self.label_author = ttk.Label(self.frame_title, **LABEL_AUTHOR)
        self.label_title.pack(**DEFAULT_PACK_CONFIG)
        self.label_author.pack(**DEFAULT_PACK_CONFIG)

        # Place message label in labelframe_message_display -- level 2
        self.label_message_display = ttk.Label(self.labelframe_message_display, **LABEL_LOADING_MESSAGE_START, style = 'message.TLabel')
        self.label_message_display.pack(**DEFAULT_PACK_CONFIG)

        # Place label in labelframe_instructions -- level 2
        self.label_instructions = ttk.Label(self.labelframe_instructions, **LABEL_INSTRUCTIONS, style = 'message.TLabel')
        self.label_instructions.pack(**DEFAULT_PACK_CONFIG)

        # Place combobox in labelframe_station_control -- level 2
        self.transit_station_variable = StringVar()
        self.combobox_station_control = ttk.Combobox(self.labelframe_station_control, textvariable = self.transit_station_variable, **COMBOBOX_STATION_CONTROL)
        self.combobox_station_control.pack(**DEFAULT_PACK_CONFIG)

        # Place combobox in labelframe_category_control -- level 2
        self.store_category_variable = StringVar()
        self.combobox_category_control = ttk.Combobox(self.labelframe_category_control, textvariable = self.store_category_variable, **COMBOBOX_CATEGORY_CONTROL)
        self.combobox_category_control.pack(**DEFAULT_PACK_CONFIG)

        # Place label and slider in labelframe_search_radius_control -- level 2
        self.search_radius_variable = DoubleVar()
        self.search_radius_variable.set(0.0)
        self.scale_search_radius = ttk.Scale(self.labelframe_search_radius_control, variable = self.search_radius_variable, **SCALE_SEARCH_RADIUS, command = self.__update_label_search_radius)
        self.scale_search_radius.pack(**DEFAULT_PACK_CONFIG, side = LEFT)
        self.label_search_radius = ttk.Label(self.labelframe_search_radius_control, **LABEL_SEARCH_RADIUS)
        self.label_search_radius.pack(**DEFAULT_PACK_CONFIG, side = LEFT)

        # Place label and slider in labelframe_display_count_control -- level 2
        self.display_count_variable = IntVar()
        self.display_count_variable.set(10)
        self.scale_display_count = ttk.Scale(self.labelframe_display_count_control, variable = self.display_count_variable, **SCALE_DISPLAY_COUNT, command = self.__update_label_display_count)
        self.scale_display_count.pack(**DEFAULT_PACK_CONFIG, side = LEFT)
        self.label_display_count = ttk.Label(self.labelframe_display_count_control, **LABEL_DISPLAY_COUNT)
        self.label_display_count.pack(**DEFAULT_PACK_CONFIG, side = LEFT)

        # Place button in frame_search_button_control -- level 2
        self.button_search = ttk.Button(self.frame_search_button_control, **BUTTON_SEARCH, style='search.TButton', command=self.display_nearby_store)
        self.button_search.pack(**DEFAULT_PACK_CONFIG)

        # After widgets are created, and window is resized accordingly
        # Set minimum window size to current width and height
        self.master.update()
        self.master.minsize(self.master.winfo_width(), self.master.winfo_height())


    def __str__(self):
        '''
        Method Name: __str__
            Defines a string when a 'GraphicalUserInterface' object is converted to a string
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
            Used to compare two 'GraphicalUserInterface' objects
        
        Parameters:
            other -- GraphicalUserInterface, object representing a Graphical user interface
        
        Raises:
            TypeError -- raises if the attributes 'name' is not a string
        
        Returns:
            bool, True if the attributes 'name' are the same, False otherwise
        '''
        if (type(self.name) is not str) or (type(other.name) is not str):
            raise TypeError("TypeError: The attribute 'name' must be a string")

        return (self.name == other.name)


    def display_loading_message(self):
        print('The program is currently retrieving and processing data. Please wait...')


    def display_nearby_store(self):
        for station in self.__list_transit_stations:
            if station.station_name == self.transit_station_variable.get():
                self.user_input.transit_station = station
        self.user_input.store_category = self.store_category_variable.get()
        self.user_input.search_radius = self.search_radius_variable.get()
        self.user_input.max_display_count = self.display_count_variable.get()
        self.__list_nearby_stores = find_nearby_stores(self.user_input, self.__list_storefronts)

        self.labelframe_output_display.destroy()
        self.labelframe_output_display = ttk.Labelframe(self.master, **LABELFRAME_OUTPUT_DISPLAY)
        self.labelframe_output_display.grid(column = 4, row = 1, columnspan = 2, rowspan = 6, **DEFAULT_GRID_CONFIG)

        treeview_output = ttk.Treeview(self.labelframe_output_display, **TREEVIEW_OUTPUT, style = 'output.Treeview')
        scrollbar_output_display = ttk.Scrollbar(self.labelframe_output_display, **SCROLLBAR_OUTPUT_DISPLAY, command = treeview_output.yview)

        treeview_output.grid(row = 0, column = 0, **DEFAULT_GRID_CONFIG)
        scrollbar_output_display.grid(row = 0, column = 1, **DEFAULT_GRID_CONFIG)

        treeview_output.config(columns = HEADER_LIST_NEARBY_STORE)
        treeview_output.config(yscrollcommand = scrollbar_output_display.set)

        for header in HEADER_LIST_NEARBY_STORE:
            treeview_output.heading(header, text = header)

        treeview_output.column('#0', width = 45, anchor = E)
        treeview_output.column('Store Name', width = 200, anchor = E)
        treeview_output.column('Distance', width = 75, anchor = E)
        treeview_output.column('Address', width = 125, anchor = E)
        treeview_output.column('Retail Category', width=175, anchor=E)

        for i in range(self.user_input.max_display_count):
            treeview_output.insert('', i, i, text = i + 1)
            treeview_output.set(i, 'Store Name', self.__list_nearby_stores[i].storefront.business_name)
            treeview_output.set(i, 'Distance', '{:.1f}'.format(self.__list_nearby_stores[i].distance) + ' ' + DISTANCE_UNIT)
            treeview_output.set(i, 'Address', self.__list_nearby_stores[i].storefront.full_address)
            treeview_output.set(i, 'Retail Category', self.__list_nearby_stores[i].storefront.retail_category)


    def populate_menus(self, list_transit_stations, list_storefronts):
        '''
        Method Name: opulate_menus
            Assign information from a list of 'TransitStation' objects and a list of 'Storefront'
            objects to attributes of the 'GraphicalUserInterface' class
        
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

        self.__generate_list_station_names()
        self.__generate_list_store_categories()

        self.combobox_station_control.config(values = self.__list_station_names)
        self.combobox_station_control.current(0)

        self.combobox_category_control.config(values = self.__list_store_categories)
        self.combobox_category_control.current(0)


    def start_user_interaction(self):
        '''
        Method Name: start_user_interaction
            Commences interaction between graphical and user. Displays menus and prompts
            users for input. The inputs in the graphical are stored as attributes in the
            'graphicalUserInterface' object.
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            Nothing
        '''
        self.label_message_display.config(**LABEL_LOADING_MESSAGE_WAIT)
        self.scale_search_radius.config(state = NORMAL)
        self.scale_display_count.config(state = NORMAL)
        self.button_search.config(state = NORMAL)
        self.master.mainloop()


    def __configure_style(self):
        self.style = ttk.Style()
        self.style.configure('search.TButton', font = ('Arial', 16))
        self.style.configure('message.TLabel', font = ('Arial', 10))
        self.style.configure('output.Treeview', font =('Arial', 8))


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

        self.__list_station_names = sorted(list_station_name)


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
        self.__list_store_categories = sorted(list_store_categories)


    def search_nearby_stores(self):
        self.__list_nearby_stores = find_nearby_stores(self.user_input, self.__list_storefronts)


    def __set_grid_configurations(self):
        # Only row 2 can expand
        self.master.rowconfigure(0, weight = 0)
        self.master.rowconfigure(1, weight = 0)
        self.master.rowconfigure(2, weight = 0)
        self.master.rowconfigure(3, weight = 0)
        self.master.rowconfigure(4, weight = 0)
        self.master.rowconfigure(5, weight = 1)

        # Only column 4 and column 5 can expand
        self.master.columnconfigure(0, weight = 0)
        self.master.columnconfigure(1, weight = 0)
        self.master.columnconfigure(2, weight = 0)
        self.master.columnconfigure(3, weight = 0)
        self.master.columnconfigure(4, weight = 1)
        self.master.columnconfigure(5, weight = 1)


    def __update_label_search_radius(self, event):
        label_text = 'Search All'
        search_radius = self.search_radius_variable.get() / 1000
        if search_radius != 0:
            label_text = '{:.1f}'.format(search_radius) + ' km'
        self.label_search_radius.config(text = label_text)


    def __update_label_display_count(self, event):
        label_text = self.display_count_variable.get()
        self.label_display_count.config(text = label_text)
