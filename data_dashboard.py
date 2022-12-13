'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Data Dashboard - datadashboard.py

Program Description:
--------------------
For User:
This program searches for the location of nearby stores given a Transit Station.
The user can select a store category, a search radius, and a maximum number of
stores to display. The number of stores displayed on the map and table will
either be governed by the search radius or the maximum number of stores selected.

What the program does:
This program parses data (Transit Stations and Storefronts in Vancouver) and
represent them in a 'TransitStation' and a 'Storefront' objects respectively.
The program prompts user for a transit station, a store category, and a 
search radius. Then the program will output information of the nearby stores
around the transit station in a table; the output is also displayed in a
visualization of a map of Vancouver with the location of the transit station
and the nearby stores marked on it. The user can also specify the maximum number
of stores to display. The program will only display up to 1000 stores, and the
maximum search radius from a transit station is 5.0 km.

Classes used for user interaction:
--------
GraphicalUserInterface - controls how the terminal interacts with the user
UserInput -- represents a set of input a user has chosen
VisualizationView -- controls what is displayed in the visualization

Files ussed for model (download, parse, clean, object creation):
------------------------
dataset_downloader -- downloads online dataset and parse them into text
dataset_parameters -- creates DataDescriptor objects
local_area_boundary_factory -- clean data and creats 'LocalAreaBoundary' objects
storefront_factory -- cleans data and creates 'Storefront' objects
transit_station_factory -- cleans data and creates 'TransitStation' objects

Classes used for model:
------------------
DataDescriptor -- represents the parameters of a dataset
LocalAreaBoundary -- represents the geographical boundary of a local area
Storefront -- represents a storefront
TransitStation -- represents a transit station

File used for analysis:
------------------
nearby_stores_finder -- finds and creates 'NearbyStore' objects

Classes used for analysis:
---------------------
TransitStation -- calculates distances between TransitStation and any coordinates
NearbyStore -- represents a store near a selected transit station

Python libraries (with approval of use):
----------------------------------------
requests -- connects to an online dataset and parses data into text
re -- cleans data, removes/replaces unwanted characters in data
json -- extracts data from a json-encoded string (coordinates data)
'''

# Classes
from user_interface.graphical_user_interface import GraphicalUserInterface


# Main Function
def main():

    try:
        # Instantiate user input and user interface
        # In this program, the GUI acts as the console because the program is
        # event-driven. Dataset downloading/processing related functions are
        # called during the construction of the GUI. Analysis related functions
        # are called within user-triggered events.
        user_interface = GraphicalUserInterface()
        user_interface.start_user_interaction()

    # All errors raised are handled in the message window in the GUI
    # Application window will close after 10 seconds, and the exception
    # is re-raised here and printed in the terminal.
    # See GraphicaluserInterface.start_user_interaction for error handling
    except Exception as exception:
        print(exception)
        
if __name__ == "__main__":
    main()
