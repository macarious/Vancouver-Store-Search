'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Data Dashboard - datadashboard.py

This program parses data (Transit Stations and Storefronts in Vancouver) and
represent them in a 'TransitStation' and a 'Storefront' objects respectively.
The program prompts user for a transit station, a store category, and a 
search radius. Then the program will output information of the nearby stores
around the transit station in a table, based on the user input. The user can also
specify the maximum number of stores to display. The program will only display
up to 100 stores in the terminal screen.

The following classes are used:
DataDescriptor - describes the parameters needed to download online data
TransitStation - represents a transit station
Storefront - represents a storefront
NearbyStore - represents a store near a transit station
TerminalInterface - controls how the terminal interacts with the user

The following custom modules are used:
dataset_downloader - downloads online dataset and them parse into text
transit_station_factory - cleans data and creates 'TransitStation' objects
storefront_factory - cleans data and creates 'Storefront' objects
nearby_stores_finder -  finds and creates 'NearbyStore' objects
dataset_table_printer - creates dataframe from list of objects

The following libraries/modules are used (with approval):
pandas - creates 'dataframe' objects
requests - connects to an online dataset and parses data into text
re - cleans data, removes/replaces unwanted characters in data
json - extracts data from a json-encoded string (coordinates data)
'''
# Classes
from model.user_input import UserInput
from user_interface.graphical_user_interface import GraphicalUserInterface


# Main Function
def main():

    # try:
        # Instantiate user input and user interface
        # In this program, the GUI acts as the console because the program is
        # event-driven. Dataset downloading/processing related functions are
        # called during the construction of the GUI. Analysis related functions
        # are called within user-triggered events.
        user_input = UserInput()
        user_interface = GraphicalUserInterface(user_input)
        user_interface.build_application_window()
        user_interface.start_user_interaction()

    # except Exception as exception: # Reraises exceptions from called functions/methods
    #     print(exception)
        
if __name__ == "__main__":
    main()
