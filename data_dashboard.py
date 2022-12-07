'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Data Dashboard - datadashboard.py

Program Description:
--------------------
This program parses data (Transit Stations and Storefronts in Vancouver) and
represent them in a 'TransitStation' and a 'Storefront' objects respectively.
The program prompts user for a transit station, a store category, and a 
search radius. Then the program will output information of the nearby stores
around the transit station in a table; the output is also displayed in a
visualization of a map of vancouver with the location of the transit station
and the nearby stores marked on it. The user can also specify the maximum number
of stores to display. The program will only display up to 1000 stores, and the
maximum search radius from a transit station is 5.0 km.

Classes:
--------
DataDescriptor - represents the parameters of a dataset
GraphicalUserInterface - controls how the terminal interacts with the user
LocalAreaBoundary -- represents the geographical boundary of a local area
NearbyStore - represents a store near a transit station
Storefront - represents a storefront
TransitStation - represents a transit station
UserInput -- represents a set of input a user has chosen
VisualizationView -- controls what is displayed in the visualization

File for model creation:
------------------------
dataset_downloader -- downloads online dataset and parse them into text
dataset_parameters -- creates DataDescriptor objects
local_area_boundary_factory -- clean data and creats 'LocalAreaBoundary' objects
storefront_factory - cleans data and creates 'Storefront' objects
transit_station_factory - cleans data and creates 'TransitStation' objects

File for analysis:
------------------
nearby_stores_finder -- finds and creates 'NearbyStore' objects


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

    except Exception as exception: # Reraises exceptions here
        print(exception)
        
if __name__ == "__main__":
    main()
