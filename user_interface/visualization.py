'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class Name -- VisualizationView, see docstring below

This file is used by the following:
visualization_view
'''

from tkinter import *
from tkinter import ttk


COORDINATE_COUNT = 2 # Coordinates are represented by 2 values
DEFAULT_GRID_CONFIG = {
    'sticky' : 'new',
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


class VisualizationView:
    '''
    Class Name: VisualizationView
        Object of this class holds the different category of data acquired
        from a dataset as its instance attributes. The parameters used to instantiate
        a 'VisualizationView' are the local area abbreciation (Map ID), the name of
        the neighbourhood, the coordinates which connects the boundary, and the
        coordinate of the centroid of the neighbourhood.

        The following methods are available:
        __init__ (constructor)
        __str__ 
        __eq__
    '''
    def __init__(self, gui):
        '''
        Method Name: __init__
            Constructor for 'VisualizationView'
        
        Parameters:
            name -- str, local area boundary name
            coordinates -- tuple of (float, float), coordinates of local area boundary, in
                EPSG 26910 format, a local projected coordinate system in metres
            local_area -- str, the neighbourhood the station is located
        
        Raises:
            TypeError --
            TypeError --
            TypeError --
            TypeError --
            TypeError --
        
        Returns:
            None
        '''
        self.name = 'Visualization View'
        self.canvas = gui.canvas_output_display
        self.legend = gui.labelframe_output_legend
        self.user_input = gui.user_input
        self.list_local_area_boundaries = gui.list_local_area_boundaries
        self.list_nearby_stores = gui.list_nearby_stores

        self.map_min_x = 0.0
        self.map_max_x = 0.0
        self.map_min_y = 0.0
        self.map_max_y = 0.0
        self.scale = 1.0

    
    def __str__(self):
        '''
        Method Name: __str__
            Defines a string when a 'VisualizationView' object is converted to a string (ex. when
            the 'str' or 'print' function is called)
        
        Parameters:
            Nothing
        
        Raises:
            TypeError --
            
        Returns:
            str, the string used when 'str' or 'print' functions is called
        '''
        return (
            f"{self.name}:\n"
            f"Input -- Station: {self.user_input.name}\n"
            f"Input -- Store Category : {self.user_input.store_category}\n"
            f"Input -- Search Radius : {self.user_input.search_radius}\n"
        )

    
    def __eq__(self, other):
        '''
        Method Name: __eq__
           Used to compare two 'VisualizationView' objects
        
        Parameters:
            other -- VisualizationView, object representing a local area boundary
        
        Raises:
            TypeError -- raises if the parameter 'other' is not a 'VisualizationView' object
        
        Returns:
            bool, True if the 'station_name' attributes are the same; False otherwise
        '''
        if type(other) is not VisualizationView:
            raise TypeError("TypeError: The parameter 'other' must be a 'VisualizationView' object")

        return self.user_input == other.user_input


    def display_map_nearby_stores(self):
        self.scale = self.__calculate_canvas_scale()
        self.__draw_all_local_area_boundaries()
        self.__print_local_area_names()
        self.__mark_search_radius()
        self.__mark_nearby_stores()
        self.__mark_transit_station()


    def display_legend(self):
        i = 0
        ttk.Label(self.legend, **STATION_MARKER_LEGEND_LEFT, **LABEL_LEGEND_LEFT).grid(row = i, column = 0)
        ttk.Label(self.legend, text = STATION_MARKER_LEGEND_TEXT, **LABEL_LEGEND_RIGHT).grid(row = i, column = 1)

        i += 1
        ttk.Label(self.legend, **STORE_MARKER_LEGEND_LEFT, **LABEL_LEGEND_LEFT).grid(row = i, column = 0)
        ttk.Label(self.legend, text = STORE_MARKER_LEGEND_TEXT, **LABEL_LEGEND_RIGHT).grid(row = i, column = 1)

        for local_area_boundary in self.list_local_area_boundaries:
            i += 1
            label_text_left = local_area_boundary.abbreviation
            label_text_right = local_area_boundary.name

            ttk.Label(self.legend, text = label_text_left, **LABEL_LEGEND_LEFT).grid(row = i, column = 0)
            ttk.Label(self.legend, text = label_text_right, **LABEL_LEGEND_RIGHT).grid(row = i, column = 1)


    def __calculate_canvas_scale(self):
        list_all_x_coordinates = []
        list_all_y_coordinates = []
        for local_area_boundary in self.list_local_area_boundaries:
            list_x_coordinates, list_y_coordinates = zip(*local_area_boundary.list_boundary_coordinates)
            list_all_x_coordinates.extend(list_x_coordinates)
            list_all_y_coordinates.extend(list_y_coordinates)

        self.map_min_x = min(list_all_x_coordinates)
        self.map_max_x = max(list_all_x_coordinates)
        self.map_min_y = min(list_all_y_coordinates)
        self.map_max_y = max(list_all_y_coordinates)

        map_range_x = self.map_max_x - self.map_min_x
        map_range_y = self.map_max_y - self.map_min_y
        self.canvas.update()

        canvas_range_x = self.canvas.winfo_width()
        canvas_range_y = self.canvas.winfo_height()
        scale_x = canvas_range_x / map_range_x
        scale_y = canvas_range_y / map_range_y

        return CANVAS_MAP_SCALE * min(scale_x, scale_y)


    def __calculate_scaled_centroid_all_local_area_boundary(self):
        map_centroid_x = self.scale * (self.map_min_x + self.map_max_x) / 2
        map_centroid_y = self.scale * (self.map_min_y + self.map_max_y) / 2

        return (map_centroid_x, map_centroid_y)


    def __draw_all_local_area_boundaries(self):
        for local_area_boundary in self.list_local_area_boundaries:
            self.__draw_local_area_boundary(local_area_boundary.list_boundary_coordinates)


    def __draw_local_area_boundary(self, list_boundary_coordinates):
        list_polygon_coordinates = []
        for coordinates in list_boundary_coordinates:
            coordinates = self.__normalize_coordinates(coordinates)
            list_polygon_coordinates.append(coordinates[0])
            list_polygon_coordinates.append(coordinates[1])
        self.canvas.create_polygon(list_polygon_coordinates, **CANVAS_DRAW_MAP)


    def __draw_circle_marker(self, coordinates, radius, config_settings):
        marker_coordinates = self.__normalize_coordinates(coordinates)
        marker_points = [
            marker_coordinates[0] - radius,
            marker_coordinates[1] - radius,
            marker_coordinates[0] + radius,
            marker_coordinates[1] + radius,
        ]
        self.canvas.create_oval(marker_points, **config_settings)


    def __mark_transit_station(self):
        marker_coordinates = self.user_input.transit_station.coordinates
        self.__draw_circle_marker(marker_coordinates, CANVAS_STATION_MARKER_RADIUS, CANVAS_STATION_MARKER)


    def __mark_nearby_stores(self):
        display_count = min(len(self.list_nearby_stores), self.user_input.max_display_count)
        for i in range(display_count):
            marker_coordinates = self.list_nearby_stores[i].storefront.coordinates
            self.__draw_circle_marker(marker_coordinates, CANVAS_STORE_MARKER_RADIUS, CANVAS_STORE_MARKER)

    
    def __mark_search_radius(self):
        marker_coordinates = self.user_input.transit_station.coordinates
        radius = self.scale * self.user_input.search_radius
        self.__draw_circle_marker(marker_coordinates, radius, CANVAS_SEARCH_MARKER)


    def __normalize_coordinates(self, coordinates):
        self.canvas.update()
        centroid_canvas = (self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2)
        scaled_centroid_local_area_boundary = self.__calculate_scaled_centroid_all_local_area_boundary()
        
        x_offset = centroid_canvas[0] - scaled_centroid_local_area_boundary[0]
        y_offset = centroid_canvas[1] - scaled_centroid_local_area_boundary[1]

        normalized_x_coordinate = self.scale * coordinates[0] + x_offset

        # Map is translated by the bottom-right corner to the top-right corner of canvas
        # Translate map downward by the height of canvas
        # and y-coordinates is positive in the downward direction
        normalized_y_coordinates = -1 * (self.scale * coordinates[1] + y_offset)
        normalized_y_coordinates += self.canvas.winfo_height()

        return normalized_x_coordinate, normalized_y_coordinates


    def __print_local_area_names(self):
        for local_area in self.list_local_area_boundaries:
            text_coordinates = self.__normalize_coordinates(local_area.centroid_coordinates)
            self.canvas.create_text(*text_coordinates, text = local_area.abbreviation, **CANVAS_LOCAL_AREA_NAME)