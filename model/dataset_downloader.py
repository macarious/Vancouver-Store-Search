'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Module Name -- dataset_downloader

This file contains functions which are used to retrieve data from the
following source from a URL, and returns a string of text

These functions are used by the following driver file:
storefront_factory.py
transit_station_factory.py
local_area_boundary_factory.py
'''

# Modules
import requests


TIMEOUT = 5 # seconds, used for retrieving data
CONNECTION_MAX_ATTEMPT = 3 # Maximum number of connection attempts before raising connection/timeout errors


def read_url(url):
    '''
    Function name: read_url
        Reads the content from a URL and returns a str of text from the data retrieved
        
    Parameters:
        url -- str, name of the URL to be read

    Raises:
        TypeError -- raises if URL is not a str
        HTTP Error -- raises if HTTP request returns an unsuccessful status code
        ConnectionError -- raises if network problem occurs
        TooManyRedirects -- raises if there are too many redirect attempts
        Timeout -- raises if the connection has timed out while trying to connect to url
        ValueError -- raises if text does not contain any content

    Returns:
        str, text from Response object
    '''
    if type(url) is not str:
        raise TypeError("TypeError: The parameter 'url' for function 'read_url' must be a string")

    # 'Try-except' block is only used to catch all connection-related errors

    try:
        response = requests.get(url, timeout = TIMEOUT)

    except requests.HTTPError:
        raise requests.HTTPError("Error: A HTTP error has occured; URL may be invalid")

    except requests.ConnectionError:
        raise ConnectionError("Error: Cannot connect to URL due to a network problem")

    except requests.TooManyRedirects:
        raise requests.TooManyRedirects("Error: There are too many redirects while attempting to connect to URL")

    except requests.Timeout:
            raise TimeoutError(f"Error: Connection has timed out while attempting to connect to URL")

    text = response.text

    if text == '':
        raise ValueError("ValueError: Text does not contain any content")

    return text
