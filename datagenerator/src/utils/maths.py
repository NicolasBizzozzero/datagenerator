import random


def get_random_integer(floor: int, ceil: int) -> int:
    """ Return a random integer between 'floor' inclusive and 'ceil'
        exclusive.
    """
    return random.randint(floor, ceil)


if __name__ == '__main__':
    pass
