# Intercom
Given a list of customers in a text file, Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending).</br>


All code is located in the src directory

# How

We use the Haversine formula https://en.wikipedia.org/wiki/Haversine_formula to calculate the distance between the coordinates specified </br>

The code has 4 functions
1. read_data_from_file - given a file reads it line by line and deserializes the contents into a dictionary and returns a list of data read from file_to_read
2. calculate_distance_between_coordinates - Implementation of the  Haversine formulae to calculate the distance between co-coordinates
3. sort_list_of_dictionary_by_key - Given a list of dictionaries sorts the items in the list based on a key in the dictionary items
4. calculate_distances_to_customer_locations - Receives the data read from file and uses the above two methods to compute customers within the 100km range
5. execute is called to wrap up the functions together


# Assumptions
>1. The customer file will be located in same folder as code (downloaded and included)
>2. The coordinates from the customers will be valid and correct

# Environment
This is developed in python 3.6.4 should work with all versions of python >3 </br>
There is also included a docker container that can be executed if  you lack an up and running docker container

# How to execute
>. Running the code.

cd into the src directory and execute ``` python main.py ``` </br>

Using docker I have pushed an image to repository `kigsmtua/intercom` based on the dockerfile in this repository so the code can be execueted by running
```dockerr run kigsmtua/intercom```
