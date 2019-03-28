import unittest
from main import * # noqa
import config


class CalculateCustomerWithinDistanceTest(unittest.TestCase):

    def test_only_customers_within_range_are_produced(self):
        customers = read_data_from_file("testcustomers.txt")
        customers_within_range = calculate_distances_to_customer_locations(customers)

        # Distances we've calculated to more than 100kms
        expected_customer_list = [{'latitude': '53.2451022', 'user_id': 4,
                                  'name': 'Ian Kehoe', 'longitude': '-6.238335'}, {'latitude': '53.1302756',
                                  'user_id': 5, 'name': 'Nora Dempsey', 'longitude': '-6.2397222'}]
        self.assertEqual(customers_within_range, expected_customer_list)

    def test_correct_distance_is_computed(self):
        # We know distance between coordinates is 10.57 km from
        # https://gps-coordinates.org/distance-between-coordinates.php
        distance = calculate_distance_between_coordinates((53.2451022, -6.238335))
        self.assertEqual(round(distance, 2), 10.57)

    def test_items_in_list_are_sorted(self):
        unsorted_list = [{'latitude': '53.2451022', 'user_id': 9,
                          'name': 'Ian Kehoe', 'longitude': '-6.238335'}, {'latitude': '53.1302756',
                           'user_id': 6, 'name': 'Nora Dempsey', 'longitude': '-6.2397222'}]
        expected_list = unsorted_list = [{'latitude': '53.2451022', 'user_id': 6,
                                          'name': 'Ian Kehoe', 'longitude': '-6.238335'}, {'latitude': '53.1302756',
                                          'user_id': 9, 'name': 'Nora Dempsey', 'longitude': '-6.2397222'}]

        sorted_list = sort_list_of_dictionary_by_key(unsorted_list, 'user_id')
        self.assertEqual(sorted_list,  expected_list)


if __name__ == '__main__':
    unittest.main()
