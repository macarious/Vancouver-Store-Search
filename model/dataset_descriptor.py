'''
CS 5001, Fall 2022
HUI, Macarious Kin Fung

Data Dashboard Final Project

Class DataExtractor -- see docstring below

This file is used by the following:
resource.dataset_parameters.py
'''

class DatasetDescriptor:
    '''
    Class Name: DatasetDescriptor
        Object of this class holds properties used to acquire data
        from a dataset as its instance attributes. The parameters used to
        instantiate a 'DatasetDescriptor' are the dataset name, url,
        and expected header. The delimiter symbol is an optional parameter
        and it is default to ';'.

        The following methods are available:
            __init__ (constructor)
            __str__
            __eq__
    '''
    def __init__(self, dataset_name, url, expected_headers, delimiter = ';'):
        '''
        Method Name: __init__
            Constructor for 'DatasetDescriptor'
        
        Parameters:
            dataset_name -- str, name of dataset
            url -- str, url for accessing dataset
            expected_headers -- dict of str, list of expected headings in dataset
            delimiter -- str, delimiter expected from dataset
        
        Raises:
            TypeError -- raises if the parameter 'dataset_name' is not a string
            TypeError -- raises if the parameter 'url' is not a string
            TypeError -- raises if the parameter 'expected_headers' is not a dictionary
            TypeError -- raises if the keys of the parameter 'expected_headers' is not a string
            TypeError -- raises if the values of the parameter 'expeected_headers' is not a string
            TypeError -- raises if the parameter 'delimiter' is not a string
        
        Returns:
            None
        '''
        if type(dataset_name) is not str:
            raise TypeError("TypeError: When instantiating a DatasetDescriptor, the parameter 'dataset_name' must be a string")

        if type(url) is not str:
            raise TypeError("TypeError: When instantiating a DatasetDescriptor, the parameter 'url' must be a string")

        if type(expected_headers) is not dict:
            raise TypeError("TypeError: When instantiating a DatasetDescriptor, the parameter 'expected_headers' must be a dictionary")

        if not all(type(key) is str for key in expected_headers.keys()):
            raise TypeError("TypeError: When instantiating a DatasetDescriptor, the parameter 'expected_headers' must contain strings as keys")

        if not all(type(value) is str for value in expected_headers.values()):
            raise TypeError("TypeError: When instantiating a DatasetDescriptor, the parameter 'expected_headers' must contain strings as values")

        if type(delimiter) is not str:
            raise TypeError("TypeError: When instantiating a DatasetDescriptor, the parameter 'delimiter' must be a string")
        
        self.dataset_name = dataset_name
        self.url = url
        self.expected_headers = expected_headers
        self.delimiter = delimiter


    def __str__(self):
        '''
        Method Name: __str__
            Defines a string when a 'DatasetDescriptor' object is converted to a string
            (ex. when calling the 'str' and 'print' functions)
        
        Parameters:
            Nothing
        
        Raises:
            TypeError -- raises if the attribute 'dataset_name' is not a string
            TypeError -- raises if the attribute 'url' is not a string
            TypeError -- raises if the attribute 'expected_headers' is not a dictionary
            TypeError -- raises if the keys of the attribute 'expected_headers' is not a string
            TypeError -- raises if the values of the attribute 'expeected_headers' is not a string
            TypeError -- raises if the attribute 'delimiter' is not a string
        
        Returns:
            str, the string used when 'str' or 'print' function is called
        '''
        if type(self.dataset_name) is not str:
            raise TypeError("TypeError: The attribute 'dataset_name' must be a string")

        if type(self.url) is not str:
            raise TypeError("TypeError: The attribute 'url' must be a string")

        if type(self.expected_headers) is not dict:
            raise TypeError("TypeError: The attribute 'expected_headers' must be a dictionary")

        if not all(type(key) is str for key in self.expected_headers.keys()):
            raise TypeError("TypeError: The attribute 'expected_headers' must contain strings as keys")

        if not all(type(value) is str for value in self.expected_headers.values()):
            raise TypeError("TypeError: The attribute 'expected_headers' must contain strings as values")

        if type(self.delimiter) is not str:
            raise TypeError("TypeError: The attribute 'delimiter' must be a string")

        return (
            f"Dataset Name: {self.dataset_name}\n"
            f"URL: {self.url}\n"
            f"Delimiter: {self.delimiter}\n"
            f"Expected Headings: {self.expected_headers}\n"
        )

    
    def __eq__(self, other):
        '''
        Method Name: __eq__
            Used to compare two 'DatasetDescriptor' objects
        
        Parameters:
            other -- DatasetDescriptor, object representing information about retrieving data
        
        Raises:
            TypeError -- raises if the attribute 'dataset_name' is not a string
        
        Returns:
            bool, True if the attributes 'dataset_name' are the same, False otherwise
        '''
        if (type(self.dataset_name) is not str) or (type(other.dataset_name) is not str):
            raise TypeError("TypeError: The attribute 'dataset_name' must be a string")

        return self.dataset_name == other.dataset_name


    