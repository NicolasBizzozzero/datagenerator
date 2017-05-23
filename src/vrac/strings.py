def concatenation(*strings: str) -> str:
    """ Return the concatenation of all str passed as input, or an empty string
    if nothing has been passed.
    """
    result = ""
    for string in strings:
        result = "{0}{1}".format(result, string)
    return result


if __name__ == '__main__':
    pass
