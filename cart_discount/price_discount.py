def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    if not isinstance(item_prices, list):  # This checks if the initial argument is formatted as something besides a list.
                                           # Tuples and sets aren't allowed for an easier time catching single strings or prices.
        raise ValueError('Argument must be a list of positive numbers. Non-list types are not allowed.')
    for item in item_prices:  # For loop checks every single item
        if type(item) not in [int, float]:  # This catches any invalid data entries which can't be properly read
                                            # by min(), e.g. string, None, lists, anything non-numeric.
            raise ValueError('An item isn\'t an integer or floating point number. Please enter a valid price before retrying.')
        if item <= 0:
            raise ValueError('All items must be a positive number. Negative or zero values are not allowed.')

    if len(item_prices) >= 3:
        discounted_item = min(item_prices)
    else:
        discounted_item = 0

    return discounted_item


if __name__ == '__main__':
    main()
