"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - the layers in the lasagna.
    :return: int - time to bake the layers at 2 mins for each layer.

    Function that takes the number of layer of lasagna has been in the oven as
    an argument and returns how many minutes the number of layers of lasagna still needs to bake at 2 mins per layer.
    """
    return number_of_layers*2

def elapsed_time_in_minutes(number_of_layers, elapsed_break_time):
    """Calculate the preparation time.

    :param number_of_layers: int - the layers in the lasagna.
    :return: int - time to bake the layers at 2 mins for each layer.

    Function that takes the number of layer of lasagna has been in the oven as
    an argument and returns how many minutes the number of layers of lasagna still needs to bake at 2 mins per layer.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_break_time
