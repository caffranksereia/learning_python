import src.exercises.calc_somar.config as cf
from ..ui.ui_show_menu import show_menu
from ..ui.ui_close import close
from ..ui.ui_show_result import show_result
from src.exercises.calc_somar.core.convert_number_items import convert_number_string
from src.exercises.calc_somar.core.convert_number_items import verify
from src.exercises.calc_somar.core.get_input_user import get_input_user


class CalculatorMath:
    def run(self):
        while True:
            show_menu
            choice = input(cf.items_menu).strip().lower()
            if choice == "x":
                close()
                break
            elif choice == cf.pull_user_get_in[0]:
                self.addition_input()
                self.exponentation_input()
            else:
                show_result(cf.invalid_option)
            break

    # you can do anything with int and float
    @staticmethod
    def addition(*numbers):
        return sum(numbers)

    def _get_valid_numbers(self):
        raw_value = get_input_user()
        numbers = verify(raw_value)

        if not numbers:
            show_result(cf.NEED_TWO_NUMBERS)
            return None

        return numbers

    def addition_input(self, *numbers):

        n = get_input_user()
        numbers = verify(n)
        if not numbers:
            show_result(cf.NEED_TWO_NUMBERS)
            return
        result = self.addition(*numbers)

        show_result(result)
