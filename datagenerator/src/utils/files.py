def get_line(filepath: str, line_number: int) -> str:
    """ Return the content of file at the line indicated by line_number. Return
        an empty string if line_number outreach the actual number of lines in
        file.
    """
    if line_number <= 0:
        return ""
    current_index = 0
    with open(filepath) as file:
        for line in file:
            current_index += 1
            if current_index == line_number:
                return line
    # If we are here, then the file has a number of lines inferior
    # to line_number
    return ""


if __name__ == '__main__':
    pass
