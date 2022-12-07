'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

File Name -- This file contains all the constants used to build and control
the graphical user interface

This file are used by the file:
graphical_user_interface.py
visualization_view.py
'''

# Constants for Graphical User Interface

APPLICATION_NAME = 'Store Finder Dashboard'
DEFAULT_GRID_CONFIG = {
    'sticky' : 'nsew',
    'ipadx' : 2,
    'ipady' : 2,
    'padx' : 2,
    'pady' : 2,
}
DEFAULT_PACK_CONFIG = {
    'fill' : 'both',
    'ipadx' : 5,
    'ipadx' : 5,
    'padx' : 5,
    'pady' : 5,
}
FRAME_TITLE = {'width': 0, 'height': 24, 'relief': 'solid'}
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
    'relief' : 'solid',
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
    'relief' : 'solid'
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
    'relief' : 'solid'
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
    'relief' : 'solid'
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
    'relief' : 'solid'
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
    'relief' : 'solid'
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
    'relief' : 'flat'
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
    'relief' : 'solid'
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
    'text' : 'The program has finished searching.\nNo results found. Please adjust the search radius.',
    'foreground' : 'red',
}
LABEL_LOADING_MESSAGE_ERROR = {
    'foreground' : 'red',
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
    'to' : 5000,
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
    'from_' : 50,
    'to' : 1000,
    'state' : 'disabled',
    'length' : 300,
}
LABEL_DISPLAY_COUNT = {
    'text' : 50,
    'font' : ('Arial', 10),
    'width' : 10,
}
BUTTON_SEARCH = {
    'text' : 'SEARCH',
    'state' : 'disabled',
}
NOTEBOOK_OUTPUT_DISPLAY = {
    'width' : 650,
    'height' : 460,
}
FRAME_NOTEBOOK_MAP_VIEW = {
    'width' : 700,
    'height' : 460,
    'relief' : 'flat',
}
FRAME_NOTEBOOK_LIST_VIEW = {
    'width' : 650,
    'height' : 460,
    'relief' : 'solid',
}
TAB_NOTEBOOK_TAB_MAP_VIEW = {
    'text' : 'Map View',
    'sticky' : 'w',
}
TAB_NOTEBOOK_TAB_LIST_VIEW = {
    'text' : 'List View',
    'sticky' : 'w',
}
CANVAS_OUTPUT_DISPLAY = {
    'width' : 465,
    'height' : 450,
}
CANVAS_OUT_DISPLAY_GRID = {
    'row' : 0,
    'column' : 0,
}
LABELFRAME_OUTPUT_LEGEND = {
    'text' : 'Legend',
    'width' : 180,
    'height' : 450,
    'relief' : 'solid',
}
LABELFRAME_OUTPUT_LEGEND_GRID = {
    'row' : 0,
    'column' : 1,
}
TREEVIEW_OUTPUT_DISPLAY = {
    'height' : 20
}
TREEVIEW_OUTPUT_DISPLAY_GRID = {
    'row' : 0,
    'column' : 0,
}
SCROLLBAR_OUTPUT_DISPLAY = {
    'orient' : 'vertical'
}
SCROLLBAR_OUTPUT_DISPLAY_GRID = {
    'row' : 0,
    'column' : 1,
}
TREEVIEW_OUTPUT_DISPLAY_COLUMN_INDEX = {
    'column' : '#0', # Default name for root column
    'width' : 50,
    'anchor' : 'e',
}
TREEVIEW_OUTPUT_DISPLAY_COLUMN_STORE_NAME = {
    'column' : 'Store Name',
    'width' : 200,
    'anchor' : 'e',
}
TREEVIEW_OUTPUT_DISPLAY_COLUMN_DISTANCE = {
    'column' : 'Distance',
    'width' : 60,
    'anchor' : 'e',
}
TREEVIEW_OUTPUT_DISPLAY_COLUMN_ADDRESS = {
    'column' : 'Address',
    'width' : 145,
    'anchor' : 'e',
}
TREEVIEW_OUTPUT_DISPLAY_COLUMN_RETAIL_CATEGORY = {
    'column' : 'Retail Category',
    'width' : 175,
    'anchor' : 'e',
}
STYLE_BUTTON_SEARCH = {
    'style' : 'search.TButton',
    'font' : ('Arial', 16),
}
STYLE_LABEL_MESSAGES = {
    'style' : 'messages.TLabel',
    'font' : ('Arial', 10, 'bold'),
}
STYLE_LABEL_INSTRUCTIONS = {
    'style' : 'instructions.TLabel',
    'font' : ('Arial', 10),
}
STYLE_TREEVIEW_OUTPUT = {
    'style' : 'output.Treeview',
    'font' : ('Arial', 8),
}

HEADER_LIST_NEARBY_STORE = ['Store Name', 'Distance', 'Address', 'Retail Category',]
DISTANCE_UNIT_DISPLAY = 'km'
DISTANCE_UNIT_SCROLLBAR = 'km'
METRE_TO_KILOMETRE_CONVERSTION = 1 / 1000
DISTANCE_UNIT_FORMAT = '{:.1f}'
ADDITIONAL_STORE_CATEGORY = 'All'
UNUSED_STORE_CATEGORY = ['Vacant', 'Vacant UC', 'Unknown']


# Constants used for Visualization (Map View)

COORDINATE_COUNT = 2 # Coordinates are represented by 2 values
DEFAULT_GRID_CONFIG = {
    'sticky' : 'nsew',
    'ipadx' : 2,
    'ipady' : 2,
    'padx' : 2,
    'pady' : 2,
}
DEFAULT_PACK_CONFIG = {
    'fill' : 'both',
    'ipadx' : 5,
    'ipadx' : 5,
    'padx' : 5,
    'pady' : 5,
}
CANVAS_MAP_SCALE = 0.90
CANVAS_DRAW_MAP = {
    'outline' : 'gray20',
    'fill' : 'gray80',
    'width' : 1,
}
CANVAS_LOCAL_AREA_NAME = {
    'fill' : 'gray30',
    'font' : ('Arial', 8, 'bold'),
}
CANVAS_STORE_MARKER_RADIUS = 2
CANVAS_STORE_MARKER = {
    'outline' : 'DarkSeaGreen4',
    'fill' : 'DarkSeaGreen3',
    'width' : 1,
}
CANVAS_STATION_MARKER_RADIUS = 4
CANVAS_STATION_MARKER = {
    'outline' : 'red4',
    'fill' : 'red3',
    'width' : 1,
}
CANVAS_SEARCH_MARKER = {
    'outline' : 'DarkSeaGreen4',
    'fill' : '',
    'width' : 1,
}
LABEL_LEGEND_LEFT = {
    'width' : 6,
    'font' : ('Arial', 8, 'bold'),
}
LABEL_LEGEND_RIGHT = {
    'width' : 45,
    'font' : ('Arial', 8),
}
STATION_MARKER_LEGEND_LEFT = {
    'text' : '\u2b24', # Unicode for big circle
    'foreground' : CANVAS_STATION_MARKER['fill'],
}
STATION_MARKER_LEGEND_TEXT = 'Transit Station'
STORE_MARKER_LEGEND_LEFT = {
    'text' : '\u25cf', # Unicode for circle
    'foreground' : CANVAS_STORE_MARKER['fill'],
}
STORE_MARKER_LEGEND_TEXT = 'Storefront'