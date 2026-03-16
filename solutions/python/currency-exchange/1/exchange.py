"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """
    Calcualte Exchangeable Money
    
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.

    This function caluculate the final amount that you can receive after currency exchange.
    """

    return float(budget / exchange_rate)


def get_change(budget, exchanging_value):
    """
    Calculate the change amount.
    
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    
    This function calculates the remaining change amount that you can get after the exchange.
    """

    return float(budget - exchanging_value)


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the total bill value
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.

    This functon return the value of the total bill
    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    Calculate the number of bills there.
    
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.

    This function returns the number of bills that a customer can receive during currecy exchange.
    """

    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """
    Calculate the leftover amount in the bill
    
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.

    This function returns the leftover amount after bill charged.
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the new currency value
    
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.

    This function return the maximum value of the new currency after calculating exchange rate plus the spread.
    """
    after_spread = (spread / 100) * exchange_rate + exchange_rate
    exchanged = exchange_money(budget, after_spread)
    return (exchanged // denomination) * denomination