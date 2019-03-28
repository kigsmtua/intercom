import json
from math import radians, sin, cos, asin, sqrt

from config import OFFICE_LATITUDE, OFFICE_LONGITUDE, RADIUS_WITHIN_OFFICE


def read_data_from_file(file_to_read):
    """
      Reads data from file and returns a dictionary of data that can be output
      return a list of dictionaries
    """
    with open(file_to_read) as contents:
        list_of_data = []
        for line in contents:
            list_of_data.append(json.loads(line))

    return list_of_data


def calculate_distance_between_coordinates(coords):

    """
     We use the harvesine formulae to calculate the distance
     between two points on a sphere.

     a = sin²(φB - φA/2) + cos φA * cos φB * sin²(λB - λA/2)
     c = 2 * atan2( √a, √(1−a) )
     R = 6371 km (radius of the earth) * c

     coordinates - set containing the coordinates to
                   compute distance to from office
    """

    office_latitude = radians(OFFICE_LATITUDE)
    office_longitude = radians(OFFICE_LONGITUDE)

    loc_b_latitude, loc_b_longitude = map(radians, [coords[0], coords[1]])

    loc_b_latitude_distance = loc_b_latitude - office_latitude
    loc_b_longitude_distance = loc_b_longitude - office_longitude

    # According to sin²(φB - φA/2) + cos φA * cos φB * sin²(λB - λA/2)
    a = sin(loc_b_latitude_distance/2) ** 2 + \
        cos(office_latitude) * cos(loc_b_latitude) * \
        sin(loc_b_longitude_distance/2) ** 2

    # Distance in delta
    c = 2 * asin(sqrt(a))

    distance_in_km = 6371 * c  # Convert to kilometres

    return distance_in_km


def sort_list_of_dictionary_by_key(list, sort_key):
    """
        Given a list of dictionary sort the items in the dictionary based on
        A specified key
    """

    sorted_list = sorted(list, key=lambda k: k[sort_key])
    return sorted_list


def calculate_distances_to_customer_locations(customer_data):
    """
      Given customer locations, compute the distance between the customers
      returns list of customers who are within a given range
    """
    customer_within_radius = []
    for customer in customer_data:
        latitude = float(customer['latitude'])
        longitude = float(customer['longitude'])
        distance_to_point  = calculate_distance_between_coordinates((latitude, longitude)) # noqa
        # Check to see whether customer is within the 100km radius inclusive
        if distance_to_point <= RADIUS_WITHIN_OFFICE:
            customer_within_radius.append(customer)
    return sort_list_of_dictionary_by_key(customer_within_radius, 'user_id')


def execute():
    """
        Main method, computes the customers within 100kms of the office
    """
    customer_data = read_data_from_file("customers.txt")
    print(calculate_distances_to_customer_locations(customer_data))


if __name__ == "__main__":
    execute()
