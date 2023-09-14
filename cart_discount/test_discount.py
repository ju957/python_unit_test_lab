import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_two_prices_no_discount(self):
        prices = [10, 4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_one_price(self):
        prices = [10]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_no_prices(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_three_prices_all_duplicates(self):
        prices = [10, 10, 10]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_three_prices_lowest_are_duplicates(self):
        prices = [10, 20, 10]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_three_prices_highest_are_duplicates(self):
        prices = [20, 20, 10]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_three_prices_with_float_numbers(self):
        prices = [10.63423, 4.500005, 20.11]
        expected_discount = 4.500005
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_three_prices_one_negative_trigger_ValueError(self):
        prices = [10, 4, -20]
        with self.assertRaises(ValueError):
            discount(prices)

    def test_list_of_two_prices_with_one_string_trigger_ValueError(self):
        prices = [10, 4, 'allisaurus']
        with self.assertRaises(ValueError):
            discount(prices)

    def test_string_instead_of_price_list(self):
        prices = ['typical']
        with self.assertRaises(ValueError):
            discount(prices)

    def test_tuple_of_three_prices(self):
        prices = (10, 4, 20)
        with self.assertRaises(ValueError):
            discount(prices)

    def test_sets_of_three_prices(self):
        prices = (10, 4, 20)
        with self.assertRaises(ValueError):
            discount(prices)

    def test_string_named_list_trigger_ValueError(self):
        prices = 'list'
        with self.assertRaises(ValueError):
            discount(prices)

    # basic funct
    # 2 prices
    # 1 price
    #  no prices
    # all duplicates
    # lowest duplicates
    # highest duplicates
    # float numbers
    # negative numbers
    # string
    #

    
    # TODO more unit tests here. Each test should test one scenario


if __name__ == '__main__':
    unittest.main()