'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class Name -- GraphicalUserInterface, see docstring below

This file also acts as the controller because this program
is event-driven. Dataset downloading, analysis, and various user
display are executed after the application window has been built,
and/or after the mainloop method has been called.

These functions are used by the driver file:
data_dashboard.py
'''
# Modules and Functions
from model.local_area_boundary_factory import create_local_area_boundary_list_from_url
from analysis.nearby_stores_finder import find_nearby_stores
from model.storefront_factory import create_storefront_list_from_url
from model.transit_station_factory import create_transit_station_list_from_url

# Classes
from model.dataset_descriptor import DatasetDescriptor
from user_interface.user_input import UserInput
from user_interface.visualization_view import VisualizationView

# Downloaded Libraries
import requests # Only for error handling (downloading of data is in dataset_downloader.py)
from tkinter import *
from tkinter import ttk

# Parameters / Constants
from resources.dataset_url import LOCAL_AREA_BOUNDARY
from resources.dataset_url import TRANSIT_STATIONS_DATASET
from resources.dataset_url import STOREFRONTS_DATASET
from user_interface.gui_parameters import *


CLOSE_WINDOW_TIMER = 10000 # milliseconds
CLOSE_WINDOW_COUNTDOWN_INTERVAL = 1000 # milliseconds
MILLISECOND_TO_SECOND_CONVERSION = 1 / 1000
ADDITIONAL_STORE_CATEGORY = 'All'
UNUSED_STORE_CATEGORY = ['Vacant', 'Vacant UC', 'Unknown']
# GUI-related parameters are saved in user_interface.gui_parameters


class GraphicalUserInterface:
    '''
    Class Name: GraphicalUserInterface
        This class represents the graphical user interface which interacts with
        a user to prompt for input and display output to the user graphically.
        Since this program is event-driven, this class also acts as the driver.

        #################################################
        # This method acts like the driver / controller #
        #################################################
        start_user_interface

        #############################################
        # This method calls model-related functions #
        #############################################
        create_list_of_objects_from_url

        ################################################
        # This method calls analysis-related functions #
        ################################################
        start_search_button_event
        
        The following methods are available:
        __init__ (Constructor)
        __str__
        __eq__
        build_application_window
        update_label_search_radius_event
        update_label_display_count_event

        The following methods are private:
        _configure_style
        _create_primary_frames
        _display_list_nearby_stores
        _handle_exception_in_gui
        _generate_list_station_names
        _generate_list_store_categories
        _populate_frame_title
        _populate_frame_search_button_control
        _populate_labelframe_category_control
        _populate_labelframe_display_count_control
        _populate_labelframe_instructions
        _populate_labelframe_message_display
        _populate_labelframe_output_display
        _populate_labelframe_search_radius_control
        _populate_labelframe_station_control
        _poplulate_menus
        _refresh_labelframe_output_display
        _set_grid_configuration
        _set_minimum_window_size
        _set_user_interface_state_ready
        _update_user_input
    '''
    def __init__(self):
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
        self.user_input = None # Placeholder for a 'UserInput' object

        self.list_transit_stations = [] # Placeholder empty list, list of 'Transit Station' objects from url
        self.list_storefronts = [] # Placeholder empty list, list of 'Storefront' objects from url
        self.list_local_area_boundaries = []  # Placeholder empty list, for output display in GUI
        
        self.list_station_names = [] # Placeholder empty list, for menu display in GUI
        self.list_store_categories = [] # Placeholder empty list, for menu display in GUI
        self.list_nearby_stores = []  # Placeholder empty list, for output display in GUI


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


    def start_user_interaction(self):
        '''
        Method Name: start_user_interaction
            Commences the graphical user interface. This method acts as the 'Controller'.
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        try:
            self.build_application_window()
            self.create_list_of_objects_from_url() # Download, clean, and convert dataset into objects
            self._populate_menus()
            self._set_user_interface_state_ready() # Enable all widgets
            self.master.mainloop() # Interact with the model and the view
            
        # Print error message in GUI for 10 seconds before closing application window
        # Afterwards, reraise exception in data_dashboard, to be displayed in terminal
        except requests.HTTPError as exception: 
            self._handle_exception_in_gui(exception)
            raise exception
        except requests.ConnectionError as exception: 
            self._handle_exception_in_gui(exception)
            raise exception
        except requests.TooManyRedirects as exception: 
            self._handle_exception_in_gui(exception)
            raise exception
        except requests.Timeout as exception: 
            self._handle_exception_in_gui(exception)
            raise exception
        
        # TypeError, ValueError, and AttributeError are 'abstracted' from the users      
        # Print a generic error message in GUI for 10 seconds before closing application window
        # Afterwards, reraise the actual exception in data_dashboard, to be displayed in terminal
        except TypeError as exception:
            self._handle_exception_abstract()
            raise exception
        except ValueError as exception:
            self._handle_exception_abstract()
            raise exception
        except AttributeError as exception:
            self._handle_exception_abstract()
            raise exception
        
        # All other 'unexpected' errors are reraised in data_dashboard, to be displayed
        # in terminal only
        except Exception as exception:
            raise exception


    def build_application_window(self):
        '''
        Method Name: build_application_window
            Build the main application window by creating all frames/widgets.
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        self.master = Tk()  # Create tk object - root level
        self.master.title(APPLICATION_NAME)
        self.master.resizable(False, False)

        self._configure_style()
        self._create_primary_frames()

        # Populate each of the primary frames with appropriate frames and widgets
        self._populate_frame_title()
        self._populate_labelframe_message_display()
        self._populate_labelframe_instructions()
        self._populate_labelframe_station_control()
        self._populate_labelframe_category_control()
        self._populate_labelframe_search_radius_control()
        self._populate_labelframe_display_count_control()
        self._populate_frame_search_button_control()
        self._populate_labelframe_output_display()

        self._set_minimum_window_size()


    def create_list_of_objects_from_url(self):
        '''
        Method Name: create_list_of_objects_from_url
            Creates list of objects for each of the three dataset from online dataset:
            (1) 'TransitStation', (2) 'Storefronts', (3) 'LocalAreaBoundary'
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        transit_station_dataset_parameters = DatasetDescriptor(**TRANSIT_STATIONS_DATASET)
        storefront_dataset_parameters = DatasetDescriptor(**STOREFRONTS_DATASET)
        local_area_boundary_dataset_parameters = DatasetDescriptor(**LOCAL_AREA_BOUNDARY)
        self.list_transit_stations = create_transit_station_list_from_url(transit_station_dataset_parameters)
        self.list_storefronts = create_storefront_list_from_url(storefront_dataset_parameters)
        self.list_local_area_boundaries = create_local_area_boundary_list_from_url(local_area_boundary_dataset_parameters)


    def start_search_button_event(self):
        '''
        Method Name: start_search_button_event
            Event triggers when the search button is clicked. Refreshes the current map
            view and list view. Finds a list of nearby stores according to the most recent
            user input. Displays the results in a map view and a list view.
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self._update_user_input()

        # Analysis is done in the 'nearbystores_finder' module
        self.list_nearby_stores = find_nearby_stores(self.user_input, self.list_storefronts)

        self._refresh_labelframe_output_display() # Refresh labelframe to clear existing output

        if len(self.list_nearby_stores) == 0:
            self.label_message_display.config(**LABEL_LOADING_MESSAGE_COMPLETE_NO_RESULTS)

        else:
            self._display_list_nearby_stores()
            current_map_view = VisualizationView(self)
            current_map_view.display_legend()
            current_map_view.display_map_nearby_stores()
            self.label_message_display.config(**LABEL_LOADING_MESSAGE_COMPLETE_NORMAL)


    def update_label_search_radius_event(self, event):
        '''
        Method Name: update_label_search_radius_event
            Event triggers when user adjust the search radius slider. Updates the text label
            adjacent to the search radius slider.
        
        Parameters:
            event -- event, represents an event triggered in the mainloop
        
        Raises:
            Nothing

        Returns:
            None
        '''
        label_text = LABEL_SEARCH_RADIUS['text']
        search_radius = self.search_radius_variable.get() * METRE_TO_KILOMETRE_CONVERSTION
        if search_radius != 0:
            label_text = DISTANCE_UNIT_FORMAT.format(search_radius) + ' ' + DISTANCE_UNIT_SCROLLBAR
        self.label_search_radius.config(text = label_text)


    def update_label_display_count_event(self, event):
        '''
        Method Name: update_label_display_count_event
            Event triggers when user adjust the display count slider. Updates the text label
            adjacent to the display count slider.
        
        Parameters:
            event -- event, represents an event triggered in the mainloop
        
        Raises:
            Nothing

        Returns:
            None
        '''
        label_text = self.display_count_variable.get()
        self.label_display_count.config(text = label_text)


    def _configure_style(self):
        '''
        Method Name: _configure_style
            Configures the style of the various widgets in the program.
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.style = ttk.Style()
        self.style.configure(**STYLE_BUTTON_SEARCH)
        self.style.configure(**STYLE_LABEL_MESSAGES)
        self.style.configure(**STYLE_LABEL_INSTRUCTIONS)
        self.style.configure(**STYLE_TREEVIEW_OUTPUT)


    def _create_primary_frames(self):
        '''
        Method Name: _create_primary_frames
            Creates the primary, top-level frames in the application window.
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
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


    def _display_list_nearby_stores(self):
        '''
        Method Name: _display_list_nearby_stores
            Creates the primary, top-level frames in the application window.
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        display_count = min(len(self.list_nearby_stores), self.user_input.max_display_count)
        for i in range(display_count):
            self.treeview_output_display.insert('', index = i, iid = i, text = i + 1) # Insert new row with index starting at 1 (ex. column ID = 0 -> text = 1)
            self.treeview_output_display.set(i, TREEVIEW_OUTPUT_DISPLAY_COLUMN_STORE_NAME['column'], self.list_nearby_stores[i].storefront.business_name)
            self.treeview_output_display.set(i, TREEVIEW_OUTPUT_DISPLAY_COLUMN_DISTANCE['column'], DISTANCE_UNIT_FORMAT.format(self.list_nearby_stores[i].distance * METRE_TO_KILOMETRE_CONVERSTION) + ' ' + DISTANCE_UNIT_DISPLAY)
            self.treeview_output_display.set(i, TREEVIEW_OUTPUT_DISPLAY_COLUMN_ADDRESS['column'], self.list_nearby_stores[i].storefront.full_address)
            self.treeview_output_display.set(i, TREEVIEW_OUTPUT_DISPLAY_COLUMN_RETAIL_CATEGORY['column'], self.list_nearby_stores[i].storefront.retail_category)


    def _generate_list_station_names(self):
        '''
        Method Name: _generate_list_station_names
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


    def _generate_list_store_categories(self):
        '''
        Method Name: _generate_list_store_categories
            Generate a list of store categories form a list of 'Storefront' objects
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if attribute 'list_storefront' is not a list
            ValueError -- raises if attribute 'list_storefront' is an empty list
        
        Returns:
            None
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


    def _handle_exception_abstract(self):
        close_window_timer = CLOSE_WINDOW_TIMER # milliseconds
        while close_window_timer >= 0:
            message_text = f"An expected error has occured.\nWindow will close in {int(close_window_timer * MILLISECOND_TO_SECOND_CONVERSION)} seconds."
            self.label_message_display.config(LABEL_LOADING_MESSAGE_ERROR, text = message_text)
            self._wait(CLOSE_WINDOW_COUNTDOWN_INTERVAL) # milliseconds
            close_window_timer -= CLOSE_WINDOW_COUNTDOWN_INTERVAL # milliseconds


    def _handle_exception_in_gui(self, exception):
        close_window_timer = CLOSE_WINDOW_TIMER # millseconds
        while close_window_timer >= 0:
            message_text = f"{exception}\nWindow will close in {int(close_window_timer * MILLISECOND_TO_SECOND_CONVERSION)} seconds."
            self.label_message_display.config(LABEL_LOADING_MESSAGE_ERROR, text = message_text)
            self._wait(CLOSE_WINDOW_COUNTDOWN_INTERVAL) # milliseconds
            close_window_timer -= CLOSE_WINDOW_COUNTDOWN_INTERVAL # milliseconds


    def _populate_frame_title(self):
        '''
        Method Name: _populate_frame_title
            Populate the 'title' frame with a label'
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.label_title = ttk.Label(self.frame_title, **LABEL_TITLE)
        self.label_author = ttk.Label(self.frame_title, **LABEL_AUTHOR)
        self.label_title.pack(**DEFAULT_PACK_CONFIG)
        self.label_author.pack(**DEFAULT_PACK_CONFIG)


    def _populate_frame_search_button_control(self):
        '''
        Method Name: _populate_frame_search_button_control
            Populate the 'search button contro' frame with a button
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.button_search = ttk.Button(self.frame_search_button_control, **BUTTON_SEARCH, style = STYLE_BUTTON_SEARCH['style'], command = self.start_search_button_event)
        self.button_search.pack(**DEFAULT_PACK_CONFIG)


    def _populate_labelframe_category_control(self):
        '''
        Method Name: _populate_labelframe_category_control
            Populate the 'category control' label frame with a combobox (drop-down menu)
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.store_category_variable = StringVar()
        self.combobox_category_control = ttk.Combobox(self.labelframe_category_control, textvariable = self.store_category_variable, **COMBOBOX_CATEGORY_CONTROL)
        self.combobox_category_control.pack(**DEFAULT_PACK_CONFIG)


    def _populate_labelframe_display_count_control(self):
        '''
        Method Name: _populate_labelframe_display_count_control
            Populate the 'display count control' label frame with a scale (slider) and a label
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.display_count_variable = IntVar()
        self.display_count_variable.set(SCALE_DISPLAY_COUNT['from_'])
        self.scale_display_count = ttk.Scale(self.labelframe_display_count_control, variable = self.display_count_variable, **SCALE_DISPLAY_COUNT, command = self.update_label_display_count_event)
        self.scale_display_count.pack(**DEFAULT_PACK_CONFIG, side = LEFT)
        self.label_display_count = ttk.Label(self.labelframe_display_count_control, **LABEL_DISPLAY_COUNT)
        self.label_display_count.pack(**DEFAULT_PACK_CONFIG, side = LEFT)


    def _populate_labelframe_instructions(self):
        '''
        Method Name: _populate_labelframe_instructions
            Populate the 'instructions' label frame with a label
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.label_instructions = ttk.Label(self.labelframe_instructions, **LABEL_INSTRUCTIONS, style = STYLE_LABEL_INSTRUCTIONS['style'])
        self.label_instructions.pack(**DEFAULT_PACK_CONFIG)


    def _populate_labelframe_message_display(self):
        '''
        Method Name: _populate_labelframe_message_display
            Populate the 'message display' label frame with a label
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.label_message_display = ttk.Label(self.labelframe_message_display, **LABEL_LOADING_MESSAGE_START, style = STYLE_LABEL_MESSAGES['style'])
        self.label_message_display.pack(**DEFAULT_PACK_CONFIG)


    def _populate_labelframe_output_display(self):
        '''
        Method Name: _populate_labelframe_output_display
            Populate the 'output display' label frame with a notebook. The notebook contains
            two tabs:
                (1) Map View -- canvas and a label frame
                (2) List View -- treeview and a scroll bar
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.notebook_output_display = ttk.Notebook(self.labelframe_output_display, **NOTEBOOK_OUTPUT_DISPLAY)

        # Build two separate tabs within labelframe_output_display
        self.tab_canvas = ttk.Frame(self.notebook_output_display, **FRAME_NOTEBOOK_MAP_VIEW)
        self.tab_treeview = ttk.Frame(self.notebook_output_display, **FRAME_NOTEBOOK_LIST_VIEW)
        self.notebook_output_display.add(self.tab_canvas, **TAB_NOTEBOOK_TAB_MAP_VIEW)
        self.notebook_output_display.add(self.tab_treeview, **TAB_NOTEBOOK_TAB_LIST_VIEW)
        self.notebook_output_display.pack(**DEFAULT_PACK_CONFIG)

        # Tab 1 -- Build map view (visualization) - Canvas (map view) with legend
        self.canvas_output_display = Canvas(self.tab_canvas, **CANVAS_OUTPUT_DISPLAY)
        self.labelframe_output_legend = ttk.Labelframe(self.tab_canvas, **LABELFRAME_OUTPUT_LEGEND)
        self.canvas_output_display.grid(**CANVAS_OUT_DISPLAY_GRID, **DEFAULT_GRID_CONFIG)
        self.labelframe_output_legend.grid(**LABELFRAME_OUTPUT_LEGEND_GRID, **DEFAULT_GRID_CONFIG)

        # Tab 2 -- Build list view - Treeview with scrollbar
        self.treeview_output_display = ttk.Treeview(self.tab_treeview, **TREEVIEW_OUTPUT_DISPLAY, style = STYLE_TREEVIEW_OUTPUT['style'])
        self.scrollbar_output_display = ttk.Scrollbar(self.tab_treeview, **SCROLLBAR_OUTPUT_DISPLAY, command = self.treeview_output_display.yview)

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


    def _populate_labelframe_search_radius_control(self):
        '''
        Method Name: _populate_labelframe_search_radius_control
            Populate the 'search radius control' label frame with a scale (slider) and a label
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.search_radius_variable = DoubleVar()
        self.search_radius_variable.set(SCALE_SEARCH_RADIUS['from_'])
        self.scale_search_radius = ttk.Scale(self.labelframe_search_radius_control, variable = self.search_radius_variable, **SCALE_SEARCH_RADIUS, command = self.update_label_search_radius_event)
        self.scale_search_radius.pack(**DEFAULT_PACK_CONFIG, side = LEFT)
        self.label_search_radius = ttk.Label(self.labelframe_search_radius_control, **LABEL_SEARCH_RADIUS)
        self.label_search_radius.pack(**DEFAULT_PACK_CONFIG, side = LEFT)


    def _populate_labelframe_station_control(self):
        '''
        Method Name: _populate_labelframe_station_control
            Populate the 'station control' label frame with a combobox (drop-down menu)
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.transit_station_variable = StringVar()
        self.combobox_station_control = ttk.Combobox(self.labelframe_station_control, textvariable = self.transit_station_variable, **COMBOBOX_STATION_CONTROL)
        self.combobox_station_control.pack(**DEFAULT_PACK_CONFIG)


    def _populate_menus(self):
        '''
        Method Name: _populate_menus
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
        if type(self.list_transit_stations) is not list:
            raise TypeError("TypeError: The attribute 'list_transit_stations' must be a list")

        if len(self.list_transit_stations) == 0:
            raise ValueError("ValueError: The attribute 'list_transit_stations' cannot be empty")
            
        if type(self.list_storefronts) is not list:
            raise TypeError("TypeError: The attribute 'list_storefronts' must be a list")

        if len(self.list_storefronts) == 0:
            raise ValueError("ValueError: The attribute 'list_storefronts' cannot be empty")
            
        self._generate_list_station_names()
        self._generate_list_store_categories()

        self.combobox_station_control.config(values = self.list_station_names)
        self.combobox_station_control.current(0) # Set first item in list as default

        self.combobox_category_control.config(values = self.list_store_categories)
        self.combobox_category_control.current(0) # Set first item in list as default


    def _refresh_labelframe_output_display(self):
        '''
        Method Name: _refresh_labelframe_output_display
            Refreshes the 'output display' notebook by destroying it and recreating it
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.notebook_output_display.destroy()
        self._populate_labelframe_output_display()


    def _set_minimum_window_size(self):
        '''
        Method Name: _set_minimum_window_size
            Set the minimim window size to its current size
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.master.update() # Update the size of window after frame/widget creating
        self.master.minsize(self.master.winfo_width(), self.master.winfo_height())


    def _set_user_interface_state_ready(self):
        '''
        Method Name: _set_user_interface_state_ready
            Enable widgets after application has finished downloading the dataset
            and populating the menus
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.label_message_display.config(**LABEL_LOADING_MESSAGE_READY)
        self.scale_search_radius.config(state = NORMAL)
        self.scale_display_count.config(state = NORMAL)
        self.button_search.config(state = NORMAL)


    def _update_user_input(self):
        '''
        Method Name: _update_user_input
            Create a 'UserInput' object with the current user input
        
        Parameters:
            Nothing
        
        Raises:
            Nothing

        Returns:
            None
        '''
        self.user_input = UserInput()
        for station in self.list_transit_stations:
            if station.station_name == self.transit_station_variable.get():
                self.user_input.transit_station = station
        self.user_input.store_category = self.store_category_variable.get()
        self.user_input.search_radius = self.search_radius_variable.get()
        self.user_input.max_display_count = self.display_count_variable.get()


    def _wait(self, time):
        '''
        Method Name: _wait
            Pauses the event for a specific time in milliseconds
        
        Parameters:
            time -- int, in milliseconds
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        dummy_var = IntVar()
        self.master.after(time, dummy_var.set, 1)
        self.master.wait_variable(dummy_var)
