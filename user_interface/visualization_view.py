'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class Name -- VisualizationView, see docstring below

This file is used by the following:
visualization_view
'''

from user_interface.gui_parameters import *
from tkinter import ttk


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
        display_map_nearby_stores
        display_legend

        The following methods are private:
        _calculate_canvas_scale
        _calculate_scaled_centroid_all_local_area_boundary
        _draw_all_local_area_boundaries
        _draw_local_area_boundary
        _draw_circle_marker
        _mark_transit_station
        _mark_nearby_stores
        _mark_search_radius
        _normalize_coordinates
        _print_local_area_names
    '''
    def __init__(self, graphical_user_interface):
        '''
        Method Name: __init__
            Constructor for 'VisualizationView'
        
        Parameters:
            name -- str, local area boundary name
            coordinates -- tuple of (float, float), coordinates of local area boundary, in
                EPSG 26910 format, a local projected coordinate system in metres
            local_area -- str, the neighbourhood the station is located
        
        Raises:
            TypeError -- raises if parameter 'list_local_area_boundaries' is not a list
            ValueError -- raises if parameter 'list_local_area_boundaries' is an empty list
            TypeError -- raises if parameter 'list_nearby_stores' is not a list
            ValueError -- raises if parameter 'list_nearby_stores' is an empty list
        
        Returns:
            None
        '''
        if type(graphical_user_interface.list_local_area_boundaries) is not list:
            raise TypeError("TypeError: The parameter 'list_local_area_boundaries' must be a list")

        if len(graphical_user_interface.list_local_area_boundaries) == 0:
            raise ValueError("ValueError: The parameter 'list_local_area_boundaries' cannot be empty")

        if type(graphical_user_interface.list_nearby_stores) is not list:
            raise TypeError("TypeError: The parameter 'list_nearby_stores' must be a list")

        if len(graphical_user_interface.list_nearby_stores) == 0:
            raise ValueError("ValueError: The parameter 'list_nearby_stores' cannot be empty")

        self.name = 'Visualization View'
        self.canvas = graphical_user_interface.canvas_output_display
        self.legend = graphical_user_interface.labelframe_output_legend
        self.user_input = graphical_user_interface.user_input
        self.list_local_area_boundaries = graphical_user_interface.list_local_area_boundaries
        self.list_nearby_stores = graphical_user_interface.list_nearby_stores

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
            Nothing
            
        Returns:
            str, the string used when 'str' or 'print' functions is called
        '''
        return (
            f"{self.name}\n"
            f"Input -- Station: {self.user_input.transit_station.station_name}\n"
            f"Input -- Store Category: {self.user_input.store_category}\n"
            f"Input -- Search Radius: {self.user_input.search_radius}\n"
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
        '''
        Method Name: display_map_nearby_stores
            Displays a map with the local area boundaries and features drawn on
            the canvas widget.
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        self.scale = self._calculate_canvas_scale()
        self._draw_all_local_area_boundaries()
        self._print_local_area_names()
        self._mark_search_radius()
        self._mark_nearby_stores()
        self._mark_transit_station()


    def display_legend(self):
        '''
        Method Name: display_legend
            Displays the legend with the list of neighbourhood area and the storefront
            and transit station markers.
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
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


    def _calculate_canvas_scale(self):
        '''
        Method Name: _calculate_canvas_scale
            Calculates the scale from the EPSG 26910 coordinates to the canvas size
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'list_local_area_boundaries' is not a list
            ValueError -- raises if the attribute 'list_local_area_boundaries' is an empty list
        
        Returns:
            float, scale to convert EPSG 26910 coordinates to fit within the canvas
        '''
        if type(self.list_local_area_boundaries) is not list:
            raise TypeError("TypeError: The attribute 'list_local_area_boundaries' must be a list")
        
        if len(self.list_local_area_boundaries) == 0:
            raise ValueError("ValueError: The attribute 'list_local_area_boundaries' must not be empty")

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


    def _calculate_scaled_centroid_all_local_area_boundary(self):
        '''
        Method Name: _calculate_scaled_centroid_all_local_area_boundary
            Calculates the centroid (scaled) for all the local area
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'map_min_x' is not a float
            TypeError -- raises if the attribute 'map_max_x' is not a float
            TypeError -- raises if the attribute 'map_min_y' is not a float
            TypeError -- raises if the attribute 'map_max_y' is not a float
        
        Returns:
            tuple of floats, coordinates of centroid
        '''
        if type(self.map_min_x) is not float:
            raise TypeError("TypeError: The attribute 'map_min_x' must be a float")

        if type(self.map_max_x) is not float:
            raise TypeError("TypeError: The attribute 'map_max_x' must be a float")

        if type(self.map_min_y) is not float:
            raise TypeError("TypeError: The attribute 'map_min_y' must be a float")

        if type(self.map_max_y) is not float:
            raise TypeError("TypeError: The attribute 'map_max_y' must be a float")

        map_centroid_x = self.scale * (self.map_min_x + self.map_max_x) / 2
        map_centroid_y = self.scale * (self.map_min_y + self.map_max_y) / 2

        return (map_centroid_x, map_centroid_y)


    def _draw_all_local_area_boundaries(self):
        '''
        Method Name: _draw_all_local_area_boundaries
            Draws the boundaries of all local areas on the canvas
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'list_local_area_boundaries' is not a list
            ValueError -- raises if the attribute 'list_local_area_boundaries' is an empty list
        
        Returns:
            None
        '''
        if type(self.list_local_area_boundaries) is not list:
            raise TypeError("TypeError: The attribute 'list_local_area_boundaries' must be a list")
        
        if len(self.list_local_area_boundaries) == 0:
            raise ValueError("ValueError: The attribute 'list_local_area_boundaries' must not be empty")

        for local_area_boundary in self.list_local_area_boundaries:
            self._draw_local_area_boundary(local_area_boundary.list_boundary_coordinates)


    def _draw_local_area_boundary(self, list_boundary_coordinates):
        '''
        Method Name: _draw_local_area_boundary
            Draws the boundary of a local area on the canvas
        
        Parameters:
            list_boundary_coordinates -- list of tuples of floats, list of all coordinates which
                when connected, form a boundary of a local area
        
        Raises:
            TypeError -- raises if the parameter 'list_boundary_coordinates' is not a list
            ValueError -- raises if the parameter 'list_boundary_coordinates' is an empty list
        
        Returns:
            None
        '''
        if type(list_boundary_coordinates) is not list:
            raise TypeError("TypeError: The attribute 'list_boundary_coordinates' must be a list")
        
        if len(list_boundary_coordinates) == 0:
            raise ValueError("ValueError: The attribute 'list_boundary_coordinates' must not be empty")

        list_polygon_coordinates = []
        for coordinates in list_boundary_coordinates:
            coordinates = self._normalize_coordinates(coordinates)
            list_polygon_coordinates.append(coordinates[0])
            list_polygon_coordinates.append(coordinates[1])
        self.canvas.create_polygon(list_polygon_coordinates, **CANVAS_DRAW_MAP)


    def _draw_circle_marker(self, coordinates, radius, config_settings):
        '''
        Method Name: _draw_circle_marker
            Draws the boundary of a local area on the canvas
        
        Parameters:
            coordinates -- tuple of floats, coordinates of the centre of circle marker
            radius -- float, radius of circle marker
            config_settings -- dict, information containing configuration settings
        
        Raises:
            TypeError -- raises if the parameter 'coordinates' is not a tuple
            ValueError -- raises if the parameter 'coordinates' does not contain exactly 2 floats
            TypeError -- raises if the parameter 'radius' is not a float or a integer
            ValueError -- raises if the parameter 'radius' is a less than or equal to 0
            TypeError -- raises if the parameter 'config_settings' is not a dictionary
        
        Returns:
            None
        '''
        if type(coordinates) is not tuple:
            raise TypeError("TypeError: The parameter 'coordinates' must be a tuple")

        if (len(coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in coordinates)):
            raise ValueError("ValueError: The parameter 'coordinates' must contain exactly 2 floats")

        if (type(radius) is not float) and (type(radius) is not int):
            raise TypeError("TypeError: The parameter 'radius' must be a float or integer")

        if radius < 0:
            raise ValueError("ValueError: The parameter 'radius' must be a positive number")

        if type(config_settings) is not dict:
            raise TypeError("TypeError: The parameter 'config_settings' must be a dict")

        marker_coordinates = self._normalize_coordinates(coordinates)
        marker_points = [
            marker_coordinates[0] - radius,
            marker_coordinates[1] - radius,
            marker_coordinates[0] + radius,
            marker_coordinates[1] + radius,
        ]
        self.canvas.create_oval(marker_points, **config_settings)


    def _mark_transit_station(self):
        '''
        Method Name: _mark_transit_station
            Mark the location of the transit station on the map
        
        Parameters:
            Nothing

        Raises:
            TypeError -- raises if the attribute 'coordinates' of class 'TransitStation' is not a tuple
            ValueError -- raises if the attribute 'coordinates' of class 'TransitStation' does not contain exactly 2 floats
        
        Returns:
            None
        '''
        marker_coordinates = self.user_input.transit_station.coordinates

        if type(marker_coordinates) is not tuple:
            raise TypeError("TypeError: The attribute 'coordinates' of class 'TransitStation' must be a tuple")

        if (len(marker_coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in marker_coordinates)):
            raise ValueError("ValueError: The attribute 'coordinates' of class 'TransitStation' must contain exactly 2 floats")

        self._draw_circle_marker(marker_coordinates, CANVAS_STATION_MARKER_RADIUS, CANVAS_STATION_MARKER)


    def _mark_nearby_stores(self):
        '''
        Method Name: _mark_nearby_stores
            Mark the locations of nearby stores on the map
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'max_display_count' of class 'UserInput' is not an integer
        
        Returns:
            None
        '''
        if type(self.user_input.max_display_count) is not int:
            raise TypeError("TypeError: The attribute 'max_display_count' of class 'UserInput' must be a integer")

        display_count = min(len(self.list_nearby_stores), self.user_input.max_display_count)
        for i in range(display_count):
            marker_coordinates = self.list_nearby_stores[i].storefront.coordinates
            self._draw_circle_marker(marker_coordinates, CANVAS_STORE_MARKER_RADIUS, CANVAS_STORE_MARKER)

    
    def _mark_search_radius(self):
        '''
        Method Name: _mark_search_radius
            Mark the locations of nearby stores on the map
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'coordinates' of class 'TransitStation' is not a tuple
            ValueError -- raises if the attribute 'coordinates' of class 'TransitStation' does not contain exactly 2 floats
            TypeError -- raises if the attribute 'search_radius' of class 'UserInput' is not a float
            ValueError -- raises if the attribute 'search_radius' of class 'UserInput' is not a float
            TypeError -- raises if the attribute 'scale' is not a float
            ValueError -- raises if the attribute 'scale' is less than or equal to 0
        
        Returns:
            None
        '''
        marker_coordinates = self.user_input.transit_station.coordinates
        search_radius = self.user_input.search_radius

        if type(marker_coordinates) is not tuple:
            raise TypeError("TypeError: The attribute 'coordinates' of class 'TransitStation' must be a tuple")

        if (len(marker_coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in marker_coordinates)):
            raise ValueError("ValueError: The attribute 'coordinates' of class 'TransitStation' must contain exactly 2 floats")

        if type(search_radius) is not float:
            raise TypeError("TypeError: The attribute 'search_radius' of class 'UserInput' must be a float")

        if search_radius < 0:
            raise ValueError("ValueError: The attribute 'search_radius' of class 'UserInput' cannot be negative")

        if type(self.scale) is not float:
            raise TypeError("TypeError: The attribute 'scale' must be a float")

        if self.scale <= 0:
            raise ValueError("ValueError: The attribute 'scale' must be a positive number")

        radius = self.scale * search_radius
        self._draw_circle_marker(marker_coordinates, radius, CANVAS_SEARCH_MARKER)


    def _normalize_coordinates(self, coordinates):
        '''
        Method Name: _normalize_coordinates
            Mark the locations of nearby stores on the map
        
        Parameters:
            coordinates -- tuple of floats, x- and y-coordinates
        
        Raises:
            TypeError -- raises if the parameter 'coordinates' is not a tuple
            ValueError -- raises if the parameter 'coordinates' does not contain exactly 2 floats
            TypeError -- raises if the attribute 'scale' is not a float
            ValueError -- raises if the attribute 'scale' is less than or equal to 0
        
        Returns:
            tuple of floats, coordinates of noramlized coordinates
        '''
        if type(coordinates) is not tuple:
            raise TypeError("TypeError: The parameter 'coordinates' must be a tuple")

        if (len(coordinates) != COORDINATE_COUNT) or (not all(type(value) is float for value in coordinates)):
            raise ValueError("ValueError: The parameter 'coordinates' must contain exactly 2 floats")

        if type(self.scale) is not float:
            raise TypeError("TypeError: The attribute 'scale' must be a float")

        if self.scale <= 0:
            raise ValueError("ValueError: The attribute 'scale' must be a positive number")

        self.canvas.update()
        centroid_canvas = (self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2)
        scaled_centroid_local_area_boundary = self._calculate_scaled_centroid_all_local_area_boundary()
        
        x_offset = centroid_canvas[0] - scaled_centroid_local_area_boundary[0]
        y_offset = centroid_canvas[1] - scaled_centroid_local_area_boundary[1]

        normalized_x_coordinate = self.scale * coordinates[0] + x_offset

        # Map is translated by the bottom-right corner to the top-right corner of canvas
        # Translate map downward by the height of canvas
        # and y-coordinates is positive in the downward direction
        normalized_y_coordinates = -1 * (self.scale * coordinates[1] + y_offset)
        normalized_y_coordinates += self.canvas.winfo_height()

        return normalized_x_coordinate, normalized_y_coordinates


    def _print_local_area_names(self):
        '''
        Method Name: _print_local_area_names
            Displays the local area abbreviation on the map
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'list_local_area_boundaries' is not a list
            ValueError -- raises if the attribute 'list_local_area_boundaries' is an empty list
        
        Returns:
            None
        '''
        if type(self.list_local_area_boundaries) is not list:
            raise TypeError("TypeError: The attribute 'list_local_area_boundaries' must be a list")
        
        if len(self.list_local_area_boundaries) == 0:
            raise ValueError("ValueError: The attribute 'list_local_area_boundaries' must not be empty")

        for local_area in self.list_local_area_boundaries:
            text_coordinates = self._normalize_coordinates(local_area.centroid_coordinates)
            self.canvas.create_text(*text_coordinates, text = local_area.abbreviation, **CANVAS_LOCAL_AREA_NAME)