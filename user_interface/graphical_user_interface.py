'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class Name -- GraphicalUserInterface, see docstring below

These functions are used by the driver file:
data_dashboard.py
'''
# Modules and Functions
from dataset_parameters import LOCAL_AREA_BOUNDARY_DESCRIPTOR
from dataset_parameters import TRANSIT_STATIONS_DATASET_DESCRIPTOR
from dataset_parameters import STOREFRONTS_DATASET_DESCRIPTOR
from local_area_boundary_factory import create_local_area_boundary_list_from_url
from nearby_stores_finder import find_nearby_stores
from storefront_factory import create_storefront_list_from_url
from transit_station_factory import create_transit_station_list_from_url

# Downloaded Libraries
from tkinter import *
from tkinter import ttk


APPLICATION_NAME = 'Store Finder Dashboard'
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
FRAME_TITLE = {'width': 0, 'height': 24, 'relief': SOLID}
FRAME_TITLE_GRID = {
    'column': 0,
    'row': 0,
    'columnspan' : 6,
    'rowspan' : 1,
}
LABELFRAME_MESSAGE_DISPLAY = {
    'text' : 'Status/Messages',
    'width' : 480,
    'height' : 120,
    'relief' : SOLID,
}
LABELFRAME_MESSAGE_DISPLAY_GRID = {
    'column' : 0,
    'row' : 1,
    'columnspan' : 4,
    'rowspan' : 1,
}
LABELFRAME_INSTRUCTIONS = {
    'text' : 'Instructions',
    'width' : 480,
    'height' : 120,
    'relief' : SOLID
}
LABELFRAME_INSTRUCTIONS_GRID = {
    'column' : 0,
    'row' : 2,
    'columnspan' : 4,
    'rowspan' : 1,
}
LABELFRAME_STATION_CONTROL = {
    'text' : 'Transit Stations',
    'width' : 200,
    'height' : 80,
    'relief' : SOLID
}
LABELFRAME_STATION_CONTROL_GRID = {
    'column' : 0,
    'row' : 3,
    'columnspan' : 2,
    'rowspan' : 1,
}
LABELFRAME_CATEGORY_CONTROL = {
    'text' : 'Store Categories',
    'width' : 200,
    'height' : 80,
    'relief' : SOLID
}
LABELFRAME_CATEGORY_CONTROL_GRID = {
    'column' : 2,
    'row' : 3,
    'columnspan' : 2,
    'rowspan' : 1,
}
LABELFRAME_SEARCH_RADIUS_CONTROL = {
    'text' : 'Search Radius',
    'width' : 360,
    'height' : 40,
    'relief' : SOLID
}
LABELFRAME_SEARCH_RADIUS_GRID = {
    'column': 0,
    'row': 4,
    'columnspan': 4,
    'rowspan': 1,
}
LABELFRAME_DISPLAY_COUNT_CONTROL = {
    'text' : 'Max Item to Display',
    'width' : 360,
    'height' : 40,
    'relief' : SOLID
}
LABELFRAME_DISPLAY_COUNT_GRID = {
    'column': 0,
    'row': 5,
    'columnspan': 4,
    'rowspan': 1,
}
FRAME_SEARCH_BUTTON_CONTROL = {
    'width' : 400,
    'height' : 40,
    'relief' : FLAT
}
FRAME_SEARCH_BUTTON_CONTROL_GRID = {
    'column': 1,
    'row': 6,
    'columnspan': 2,
    'rowspan': 1,
}
LABELFRAME_OUTPUT_DISPLAY = {
    'text' : 'Output',
    'width' : 640,
    'height' : 460,
    'relief' : SOLID
}
LABELFRAME_OUTPUT_DISPLAY_GRID = {
    'column': 4,
    'row': 1,
    'columnspan': 2,
    'rowspan': 6,
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
LABEL_LOADING_MESSAGE_READY = {
    'text' : 'The program has finished retrieving and processing the data.\nPlease continue...',
    'foreground' : 'sea green',
}
LABEL_LOADING_MESSAGE_COMPLETE_NORMAL = {
    'text' : 'The program has finished searching.\nPlease select between Map View or List View',
    'foreground' : 'sea green',
}
LABEL_LOADING_MESSAGE_COMPLETE_NO_RESULTS = {
    'text' : 'The program has finished searching.\nNo results found.\nPlease adjust search radius and/or maximum display items.',
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
NOTEBOOK_OUTPUT_DISPLAY = {
    'width' : 640,
    'height' : 460,
}
FRAME_NOTEBOOK_MAP_VIEW = {
    'width' : 700,
    'height' : 460,
    'relief' : FLAT,
}
FRAME_NOTEBOOK_LIST_VIEW = {
    'width' : 640,
    'height' : 460,
    'relief' : FLAT,
}
TAB_NOTEBOOK_TAB_MAP_VIEW = {
    'text' : 'Map View',
    'sticky' : W,
}
TAB_NOTEBOOK_TAB_LIST_VIEW = {
    'text' : 'List View',
    'sticky' : W,
}
CANVAS_OUTPUT_DISPLAY = {
    'width' : 700,
    'height' : 460,
    'bg' : 'light gray'
}
CANVAS_DRAW_MAP = {
    'outline' : 'navy',
    'fill' : 'LightBlue1',
    'width' : 2,
}
CANVAS_MAP_SCALE = 0.80
TREEVIEW_OUTPUT_DISPLAY = {
    'height' : 20
}
SCROLLBAR_OUTPUT_DISPLAY_DISPLAY = {
    'orient' : VERTICAL
}
TREEVIEW_OUTPUT_DISPLAY_GRID = {
    'row' : 0,
    'column' : 0,
}
SCROLLBAR_OUTPUT_DISPLAY_GRID = {
    'row' : 0,
    'column' : 1,
}
TREEVIEW_OUTPUT_DISPLAY_COLUMN_INDEX = {
    'column' : '#0',
    'width' : 40,
    'anchor' : E,
}
TREEVIEW_OUTPUT_DISPLAY_COLUMN_STORE_NAME = {
    'column' : 'Store Name',
    'width' : 180,
    'anchor' : E,
}
TREEVIEW_OUTPUT_DISPLAY_COLUMN_DISTANCE = {
    'column' : 'Distance',
    'width' : 60,
    'anchor' : E,
}
TREEVIEW_OUTPUT_DISPLAY_COLUMN_ADDRESS = {
    'column' : 'Address',
    'width' : 160,
    'anchor' : E,
}
TREEVIEW_OUTPUT_DISPLAY_COLUMN_RETAIL_CATEGORY = {
    'column' : 'Retail Category',
    'width' : 180,
    'anchor' : E,
}
PRIMARY_FRAME_GRID_ROW_WEIGHT = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 1,
} # key is row index; value is grid weight
PRIMARY_FRAME_GRID_COLUMN_WEIGHT = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 1,
    5 : 1,
}  # key is column index; value is grid weight
HEADER_LIST_NEARBY_STORE = ['Store Name', 'Distance', 'Address', 'Retail Category',]
DISTANCE_UNIT_DISPLAY = 'm'
DISTANCE_UNIT_SCROLLBAR = 'km'
METRE_TO_KILOMETRE_CONVERSTION = 1 / 1000
DISTANCE_UNIT_FORMAT = '{:.1f}'
ADDITIONAL_STORE_CATEGORY = 'All'
UNUSED_STORE_CATEGORY = ['Vacant', 'Vacant UC', 'Unknown']


class GraphicalUserInterface:
    '''
    Class Name: GraphicalUserInterface
        This class represents the graphical user interface which interacts with
        a user to prompt for input and display output to the user graphically.

        The following methods are available:
        __init__ (Constructor)
        __str__
        __eq__
        build_application_window
        create_list_of_objects_from_url
        start_search_button_event
        start_user_interface
        update_label_search_radius_event
        update_label_display_count_event
        __configure_style
        __create_primary_frames
        __display_list_nearby_stores
        __generate_list_station_names
        __generate_list_store_categories
        __populate_frame_title
        __populate_frame_search_button_control
        __populate_labelframe_category_control
        __populate_labelframe_display_count_control
        __populate_labelframe_instructions
        __populate_labelframe_message_display
        __populate_labelframe_output_display
        __populate_labelframe_search_radius_control
        __populate_labelframe_station_control
        __poplulate_menus
        __refresh_labelframe_output_display
        __set_grid_configuration
        __set_minimum_window_size
        __set_user_interface_state_ready
        __update_user_input
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

        self.list_transit_stations = [] # Placeholder empty list, list of 'Transit Station' objects from url
        self.list_storefronts = [] # Placeholder empty list, list of 'Storefront' objects from url
        self.list_station_names = [] # Placeholder empty list, for menu display in GUI
        self.list_store_categories = [] # Placeholder empty list, for menu display in GUI
        self.list_nearby_stores = []  # Placeholder empty list, for output display in GUI
        self.list_local_area_boundaries = []  # Placeholder empty list, for output display in GUI


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

        return f"{self.name}"


    def __eq__(self, other):
        '''
        Method Name: __eq__
            Used to compare two 'GraphicalUserInterface' objects
        
        Parameters:
            other -- GraphicalUserInterface, object representing a Graphical user interface
        
        Raises:
            TypeError -- raises if the parameter 'other' is not a 'GraphicalUserInterface' object
            TypeError -- raises if the attributes 'name' is not a string
        
        Returns:
            bool, True if the attributes 'name' are the same, False otherwise
        '''
        if type(other) is not GraphicalUserInterface:
            raise TypeError("TypeError: The parameter 'other' must be a GraphicalUserInterface object")
        if (type(self.name) is not str) or (type(other.name) is not str):
            raise TypeError("TypeError: The attribute 'name' must be a string")

        return (self.name == other.name)


    def build_application_window(self):

        self.master = Tk()  # Create tk object - root level
        self.master.title(APPLICATION_NAME)

        self.__set_grid_configurations()
        self.__configure_style()
        self.__create_primary_frames()

        # Populate each of the primary frames with appropriate frames and widgets
        self.__populate_frame_title()
        self.__populate_labelframe_message_display()
        self.__populate_labelframe_instructions()
        self.__populate_labelframe_station_control()
        self.__populate_labelframe_category_control()
        self.__populate_labelframe_search_radius_control()
        self.__populate_labelframe_display_count_control()
        self.__populate_frame_search_button_control()
        self.__populate_labelframe_output_display()

        self.__set_minimum_window_size()

        # Download and process data
        self.create_list_of_objects_from_url()
        self.__populate_menus()


    def create_list_of_objects_from_url(self):
        self.list_transit_stations = create_transit_station_list_from_url(TRANSIT_STATIONS_DATASET_DESCRIPTOR)
        self.list_storefronts = create_storefront_list_from_url(STOREFRONTS_DATASET_DESCRIPTOR)
        self.list_local_area_boundaries = create_local_area_boundary_list_from_url(LOCAL_AREA_BOUNDARY_DESCRIPTOR)


    def start_search_button_event(self):
        self.__update_user_input()

        # Analysis is done in the 'nearbystores_finder' module
        self.list_nearby_stores = find_nearby_stores(self.user_input, self.list_storefronts)

        self.__refresh_labelframe_output_display() # Refresh labelframe to clear existing output

        if len(self.list_nearby_stores) == 0:
            self.label_message_display.config(**LABEL_LOADING_MESSAGE_COMPLETE_NO_RESULTS)

        else:
            self.__display_list_nearby_stores()
            self.__display_map_nearby_stores()
            self.label_message_display.config(**LABEL_LOADING_MESSAGE_COMPLETE_NORMAL)


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
        self.__set_user_interface_state_ready()
        self.master.mainloop()


    def update_label_search_radius_event(self, event):
        label_text = LABEL_SEARCH_RADIUS['text']
        search_radius = self.search_radius_variable.get() * METRE_TO_KILOMETRE_CONVERSTION
        if search_radius != 0:
            label_text = DISTANCE_UNIT_FORMAT.format(search_radius) + ' ' + DISTANCE_UNIT_SCROLLBAR
        self.label_search_radius.config(text = label_text)


    def update_label_display_count_event(self, event):
        label_text = self.display_count_variable.get()
        self.label_display_count.config(text = label_text)


    def __configure_style(self):
        self.style = ttk.Style()
        self.style.configure('search.TButton', font = ('Arial', 16))
        self.style.configure('message.TLabel', font = ('Arial', 10))
        self.style.configure('output.Treeview', font = ('Arial', 8))


    def __create_primary_frames(self):
        self.frame_title = ttk.Frame(self.master, **FRAME_TITLE)
        self.labelframe_message_display = ttk.Labelframe(self.master, **LABELFRAME_MESSAGE_DISPLAY)
        self.labelframe_instructions = ttk.Labelframe(self.master, **LABELFRAME_INSTRUCTIONS)
        self.labelframe_station_control = ttk.Labelframe(self.master, **LABELFRAME_STATION_CONTROL)
        self.labelframe_category_control = ttk.Labelframe(self.master, **LABELFRAME_CATEGORY_CONTROL)
        self.labelframe_search_radius_control = ttk.Labelframe(self.master, **LABELFRAME_SEARCH_RADIUS_CONTROL)
        self.labelframe_display_count_control = ttk.Labelframe(self.master, **LABELFRAME_DISPLAY_COUNT_CONTROL)
        self.frame_search_button_control = ttk.Frame(self.master, **FRAME_SEARCH_BUTTON_CONTROL)
        self.labelframe_output_display = ttk.Labelframe(self.master, **LABELFRAME_OUTPUT_DISPLAY)

        self.frame_title.grid(**FRAME_TITLE_GRID, **DEFAULT_GRID_CONFIG)
        self.labelframe_message_display.grid(**LABELFRAME_MESSAGE_DISPLAY_GRID, **DEFAULT_GRID_CONFIG)
        self.labelframe_instructions.grid(**LABELFRAME_INSTRUCTIONS_GRID, **DEFAULT_GRID_CONFIG)
        self.labelframe_station_control.grid(**LABELFRAME_STATION_CONTROL_GRID, **DEFAULT_GRID_CONFIG)
        self.labelframe_category_control.grid(**LABELFRAME_CATEGORY_CONTROL_GRID, **DEFAULT_GRID_CONFIG)
        self.labelframe_search_radius_control.grid(**LABELFRAME_SEARCH_RADIUS_GRID, **DEFAULT_GRID_CONFIG)
        self.labelframe_display_count_control.grid(**LABELFRAME_DISPLAY_COUNT_GRID, **DEFAULT_GRID_CONFIG)
        self.frame_search_button_control.grid(**FRAME_SEARCH_BUTTON_CONTROL_GRID, **DEFAULT_GRID_CONFIG)
        self.labelframe_output_display.grid(**LABELFRAME_OUTPUT_DISPLAY_GRID, **DEFAULT_GRID_CONFIG)


    def __display_list_nearby_stores(self):
        for i in range(self.user_input.max_display_count):
            self.treeview_output_display.insert('', index = i, iid = i, text = i + 1) # Insert new row with index starting at 1 (ex. column ID = 0 -> text = 1)
            self.treeview_output_display.set(i, TREEVIEW_OUTPUT_DISPLAY_COLUMN_STORE_NAME['column'], self.list_nearby_stores[i].storefront.business_name)
            self.treeview_output_display.set(i, TREEVIEW_OUTPUT_DISPLAY_COLUMN_DISTANCE['column'], DISTANCE_UNIT_FORMAT.format(self.list_nearby_stores[i].distance) + ' ' + DISTANCE_UNIT_DISPLAY)
            self.treeview_output_display.set(i, TREEVIEW_OUTPUT_DISPLAY_COLUMN_ADDRESS['column'], self.list_nearby_stores[i].storefront.full_address)
            self.treeview_output_display.set(i, TREEVIEW_OUTPUT_DISPLAY_COLUMN_RETAIL_CATEGORY['column'], self.list_nearby_stores[i].storefront.retail_category)


    def __display_map_nearby_stores(self):
        for local_area_boundary in self.list_local_area_boundaries:
            self.__draw_local_area_boundary(local_area_boundary.list_boundary_coordinates)


    def __draw_local_area_boundary(self, list_boundary_coordinates):
        list_polygon_coordinates = []
        for coordinates in list_boundary_coordinates:
            coordinates = self.__normalize_local_boundary_coordinates(coordinates)
            list_polygon_coordinates.append(coordinates[0])
            list_polygon_coordinates.append(coordinates[1])
        self.canvas_output_display.create_polygon(list_polygon_coordinates, **CANVAS_DRAW_MAP)
        self.canvas_output_display.pack(**DEFAULT_PACK_CONFIG)


    def __find_scaled_centroid_all_local_area_boundary(self):
        list_all_x_coordinates = []
        list_all_y_coordinates = []
        for local_area_boundary in self.list_local_area_boundaries:
            list_x_coordinates, list_y_coordinates = zip(*local_area_boundary.list_boundary_coordinates)
            list_all_x_coordinates.extend(list_x_coordinates)
            list_all_y_coordinates.extend(list_y_coordinates)

        map_min_x = min(list_all_x_coordinates)
        map_max_x = max(list_all_x_coordinates)
        map_min_y = min(list_all_y_coordinates)
        map_max_y = max(list_all_y_coordinates)

        self.scale = self.__find_canvas_scale(map_max_x - map_min_x, map_max_y - map_min_y)

        map_centroid_x = self.scale * (map_min_x + map_max_x) / 2
        map_centroid_y = self.scale * (map_min_y + map_max_y) / 2

        return (map_centroid_x, map_centroid_y)


    def __find_canvas_scale(self, map_range_x, map_range_y):
        
        self.canvas_output_display.update()

        canvas_range_x = self.canvas_output_display.winfo_width()
        canvas_range_y = self.canvas_output_display.winfo_height()
        scale_x = canvas_range_x / map_range_x
        scale_y = canvas_range_y / map_range_y
        return min(scale_x, scale_y) * CANVAS_MAP_SCALE


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
        if type(self.list_transit_stations) is not list:
            raise TypeError("TypeError: The attribute 'list_transit_stations' must be a list")

        if len(self.list_transit_stations) == 0:
            raise ValueError("ValueError: The attribute 'list_transit_stations' cannot be empty")

        # Only add station name if station name is unique
        unique_station_names = set()
        list_station_names = []
        for station in self.list_transit_stations:
            if station.station_name not in unique_station_names:
                list_station_names.append(station.station_name)
                unique_station_names.add(station.station_name)

        self.list_station_names = sorted(list_station_names)


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
        if type(self.list_storefronts) is not list:
            raise TypeError("TypeError: The attribute 'list_storefronts' must be a list")

        if len(self.list_storefronts) == 0:
            raise ValueError("ValueError: The attribute 'list_storefronts' cannot be empty")

        list_store_categories = []
        for store in self.list_storefronts:
            if (store.retail_category not in list_store_categories) and (store.retail_category not in UNUSED_STORE_CATEGORY):
                list_store_categories.append(store.retail_category)

        list_store_categories.append(ADDITIONAL_STORE_CATEGORY)
        self.list_store_categories = sorted(list_store_categories)


    def __normalize_local_boundary_coordinates(self, coordinates):
        self.canvas_output_display.update()
        centroid_canvas = (self.canvas_output_display.winfo_width() / 2, self.canvas_output_display.winfo_height() / 2)
        scaled_centroid_local_area_boundary = self.__find_scaled_centroid_all_local_area_boundary()
        
        x_offset = centroid_canvas[0] - scaled_centroid_local_area_boundary[0]
        y_offset = centroid_canvas[1] - scaled_centroid_local_area_boundary[1]

        normalized_x_coordinate = self.scale * coordinates[0] + x_offset

        # Base point of canvas is in upper-left corner;
        # and y-coordinates is positive in the downward direction
        normalized_y_coordinates = -1 * (self.scale * coordinates[1] + y_offset)
        normalized_y_coordinates += self.canvas_output_display.winfo_height()

        return normalized_x_coordinate, normalized_y_coordinates


    def __populate_frame_title(self):
        self.label_title = ttk.Label(self.frame_title, **LABEL_TITLE)
        self.label_author = ttk.Label(self.frame_title, **LABEL_AUTHOR)
        self.label_title.pack(**DEFAULT_PACK_CONFIG)
        self.label_author.pack(**DEFAULT_PACK_CONFIG)


    def __populate_frame_search_button_control(self):
        self.button_search = ttk.Button(self.frame_search_button_control, **BUTTON_SEARCH, style='search.TButton', command=self.start_search_button_event)
        self.button_search.pack(**DEFAULT_PACK_CONFIG)


    def __populate_labelframe_category_control(self):
        self.store_category_variable = StringVar()
        self.combobox_category_control = ttk.Combobox(self.labelframe_category_control, textvariable = self.store_category_variable, **COMBOBOX_CATEGORY_CONTROL)
        self.combobox_category_control.pack(**DEFAULT_PACK_CONFIG)


    def __populate_labelframe_display_count_control(self):
        self.display_count_variable = IntVar()
        self.display_count_variable.set(10)
        self.scale_display_count = ttk.Scale(self.labelframe_display_count_control, variable = self.display_count_variable, **SCALE_DISPLAY_COUNT, command = self.update_label_display_count_event)
        self.scale_display_count.pack(**DEFAULT_PACK_CONFIG, side = LEFT)
        self.label_display_count = ttk.Label(self.labelframe_display_count_control, **LABEL_DISPLAY_COUNT)
        self.label_display_count.pack(**DEFAULT_PACK_CONFIG, side = LEFT)


    def __populate_labelframe_instructions(self):
        self.label_instructions = ttk.Label(self.labelframe_instructions, **LABEL_INSTRUCTIONS, style = 'message.TLabel')
        self.label_instructions.pack(**DEFAULT_PACK_CONFIG)


    def __populate_labelframe_message_display(self):
        self.label_message_display = ttk.Label(self.labelframe_message_display, **LABEL_LOADING_MESSAGE_START, style = 'message.TLabel')
        self.label_message_display.pack(**DEFAULT_PACK_CONFIG)


    def __populate_labelframe_output_display(self):

        self.notebook_output_display = ttk.Notebook(self.labelframe_output_display, **NOTEBOOK_OUTPUT_DISPLAY)

        self.tab_canvas = ttk.Frame(self.notebook_output_display, **FRAME_NOTEBOOK_MAP_VIEW)
        self.tab_treeview = ttk.Frame(self.notebook_output_display, **FRAME_NOTEBOOK_LIST_VIEW)
        self.notebook_output_display.add(self.tab_canvas, **TAB_NOTEBOOK_TAB_MAP_VIEW)
        self.notebook_output_display.add(self.tab_treeview, **TAB_NOTEBOOK_TAB_LIST_VIEW)
        self.notebook_output_display.pack(**DEFAULT_PACK_CONFIG)

        # Build Map View - Canvas
        self.canvas_output_display = Canvas(self.tab_canvas, **CANVAS_OUTPUT_DISPLAY)
        self.canvas_output_display.pack(**DEFAULT_PACK_CONFIG)

        # Build List View - Treeview
        self.treeview_output_display = ttk.Treeview(self.tab_treeview, **TREEVIEW_OUTPUT_DISPLAY, style = 'output.Treeview')
        self.scrollbar_output_display = ttk.Scrollbar(self.tab_treeview, **SCROLLBAR_OUTPUT_DISPLAY_DISPLAY, command = self.treeview_output_display.yview)

        self.treeview_output_display.grid(**TREEVIEW_OUTPUT_DISPLAY_GRID, **DEFAULT_GRID_CONFIG)
        self.scrollbar_output_display.grid(**SCROLLBAR_OUTPUT_DISPLAY_GRID, **DEFAULT_GRID_CONFIG)

        self.treeview_output_display.config(columns = HEADER_LIST_NEARBY_STORE)
        self.treeview_output_display.config(yscrollcommand = self.scrollbar_output_display.set)

        for header in HEADER_LIST_NEARBY_STORE:
            self.treeview_output_display.heading(header, text = header)

        self.treeview_output_display.column(**TREEVIEW_OUTPUT_DISPLAY_COLUMN_INDEX)
        self.treeview_output_display.column(**TREEVIEW_OUTPUT_DISPLAY_COLUMN_STORE_NAME)
        self.treeview_output_display.column(**TREEVIEW_OUTPUT_DISPLAY_COLUMN_DISTANCE)
        self.treeview_output_display.column(**TREEVIEW_OUTPUT_DISPLAY_COLUMN_ADDRESS)
        self.treeview_output_display.column(**TREEVIEW_OUTPUT_DISPLAY_COLUMN_RETAIL_CATEGORY)


    def __populate_labelframe_search_radius_control(self):
        self.search_radius_variable = DoubleVar()
        self.search_radius_variable.set(0.0)
        self.scale_search_radius = ttk.Scale(self.labelframe_search_radius_control, variable = self.search_radius_variable, **SCALE_SEARCH_RADIUS, command = self.update_label_search_radius_event)
        self.scale_search_radius.pack(**DEFAULT_PACK_CONFIG, side = LEFT)
        self.label_search_radius = ttk.Label(self.labelframe_search_radius_control, **LABEL_SEARCH_RADIUS)
        self.label_search_radius.pack(**DEFAULT_PACK_CONFIG, side = LEFT)


    def __populate_labelframe_station_control(self):
        self.transit_station_variable = StringVar()
        self.combobox_station_control = ttk.Combobox(self.labelframe_station_control, textvariable = self.transit_station_variable, **COMBOBOX_STATION_CONTROL)
        self.combobox_station_control.pack(**DEFAULT_PACK_CONFIG)


    def __populate_menus(self):
        '''
        Method Name: __populate_menus
            Assign information from a list of 'TransitStation' objects and a list of 'Storefront'
            objects to attributes of the 'GraphicalUserInterface' class
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the parameter 'list_transit_stations' is not a list
            ValueError -- raises if the parameter 'list_transit_stations' is an empty list
            TypeError -- raises if the parameter 'list_storefronts' is not a list
            ValueError -- raises if the parameter 'list_storefronts' is an empty list
        
        Returns:
            None
        '''
        self.__generate_list_station_names()
        self.__generate_list_store_categories()

        self.combobox_station_control.config(values=self.list_station_names)
        self.combobox_station_control.current(0) # Set first item in list as default

        self.combobox_category_control.config(values=self.list_store_categories)
        self.combobox_category_control.current(0) # Set first item in list as default


    def __refresh_labelframe_output_display(self):
        self.notebook_output_display.destroy()
        self.__populate_labelframe_output_display()


    def __set_grid_configurations(self):
        for row, grid_weight in PRIMARY_FRAME_GRID_ROW_WEIGHT.items():
            self.master.rowconfigure(row, weight = grid_weight)

        for column, grid_weight in PRIMARY_FRAME_GRID_COLUMN_WEIGHT.items():
            self.master.columnconfigure(column, weight = grid_weight)


    def __set_minimum_window_size(self):
        self.master.update() # Update the size of window after frame/widget creating
        self.master.minsize(self.master.winfo_width(), self.master.winfo_height())


    def __set_user_interface_state_ready(self):
        self.label_message_display.config(**LABEL_LOADING_MESSAGE_READY)
        self.scale_search_radius.config(state = NORMAL)
        self.scale_display_count.config(state = NORMAL)
        self.button_search.config(state = NORMAL)


    def __update_user_input(self):
        for station in self.list_transit_stations:
            if station.station_name == self.transit_station_variable.get():
                self.user_input.transit_station = station
        self.user_input.store_category = self.store_category_variable.get()
        self.user_input.search_radius = self.search_radius_variable.get()
        self.user_input.max_display_count = self.display_count_variable.get()
