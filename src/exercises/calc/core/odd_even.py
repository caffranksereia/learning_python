import src.exercises.calc.config as cf


def odd_even():
    user_input = input(cf.TEXT_DIGITE)

    value = verify_digit_and_convert(user_input)

    if value is None:
        print(cf.TEXT_INVALID)
        return

    result = verify_is_even_odd(value)

    print(f"{cf.TEXT_COMPLETE}: {value} is {result}")


def get_is_even_odd(value):
    return cf.TEXT_ODD if value % cf.NUMBER_PAR == 0 else cf.TEXT_ODD


def verify_digit_and_convert(value):
    try:
        return int(value.strip())
    except ValueError:
        return None
