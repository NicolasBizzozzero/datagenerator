def dataify(*columns, lines=1000, header=True):
    data = []
    if header:
        data.append(_retrieve_header(columns))

    for _ in range(lines):
        new_line = []
        for col in columns:
            new_line.append(col.compute_value())
        data.append(new_line)

    return data


def _retrieve_header(columns):
    return [col.get_label() for col in columns]
