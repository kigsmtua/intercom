import json
from copy import deepcopy
from math import radians, sin, cos, asin, sqrt


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
     R = 6371 km (radius of the earth)

     coordinates - set containing the coordinates to
                   compute distance to from office
    """

    office_latitude = radians(53.339428)
    office_longitude = radians(-6.257664)

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


# This is what happens when the values that come alongs
def find_distances_to_locations(list_of_data):
    # We can consume all values that come here as hallucinogens
    # The values come along as the importance of sort items here
    items = []
    for data in list_of_data:
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])
        distance_to_point  = calculate_distance_between_coordinates((latitude, longitude)) # noqa
        if distance_to_point <= 100:
            items.append(data)

    return items


file_contents = read_data_from_file("customers.txt")
print(find_distances_to_locations(file_contents))
