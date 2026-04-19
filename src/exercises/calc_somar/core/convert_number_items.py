def convert_number_string(value):
    try:
        return float(value)
    except ValueError:
        return None


def verify(value):
    try:
        numbers = [float(x) for x in value.split()]
    except ValueError:
        return None

    if len(numbers) < 2:
        return None

    return numbers
