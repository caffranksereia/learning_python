from src.exercises.calculator.core.convert_number_items import convert_number_string
from src.exercises.calculator.ui.ui_close import close
import src.exercises.calculator.config as cf


def get_input_user():
    numbers = []

    while True:
        enter_user = input(f"{cf.INPUT_MESSAGE} ").strip()

        if enter_user.lower() == "x":
            break

        converted = convert_number_string(enter_user)

        if converted is None:
            print("Invalid")
            continue

        numbers.append(converted)

    return numbers
