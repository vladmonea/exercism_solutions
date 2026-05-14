EXPECTED_BAKE_TIME = 40  # entire lasagna
PREPARATION_TIME = 2  # per layer

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    if elapsed_bake_time < 0:
        raise ValueError("elapsed_bake_time value[minutes] must be positive")
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(num_layers):
    """
    Return preparation time in minutes.

    This function takes the number of layers you want to add to the lasagna as an argument
    and returns how many minutes you would spend making them"""
    return PREPARATION_TIME * num_layers


def elapsed_time_in_minutes(num_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(num_layers) + elapsed_bake_time
