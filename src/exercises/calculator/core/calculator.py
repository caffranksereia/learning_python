import src.exercises.calculator.config as cf
from ..ui.ui_show_menu import show_menu
from ..ui.ui_close import close
from ..ui.ui_show_result import show_result
from src.exercises.calculator.core.convert_number_items import convert_number_string
from src.exercises.calculator.core.convert_number_items import verify
from src.exercises.calculator.core.get_input_user import get_input_user


class Calculator:
    def run(self):
        while True:
            show_menu
            choice = input(cf.items_menu).strip().lower()
            if choice == "x":
                close()
                break
            elif choice == cf.pull_user_get_in[0]:
                self.addition_input()

            elif choice == cf.pull_user_get_in[1]:
                self.subtraction_input()

            elif choice == cf.pull_user_get_in[3]:
                self.multiplication_input()

            elif choice == cf.pull_user_get_in[4]:
                self.division_input()

            elif choice == cf.pull_user_get_in[5]:
                self.division_truncate_input()

            elif choice == cf.pull_user_get_in[6]:
                self.exponentation_input()
            else:
                show_result(cf.invalid_option)
            break

    # you can do anything with int and float
    @staticmethod
    def addition(*numbers):
        return sum(numbers)

    @staticmethod
    def subt(*numbers):
        if len(numbers) < 2:
            return cf.NEED_TWO_NUMBERS

        res = numbers[0]

        for n in numbers[1:]:
            res -= n

        return res

    @staticmethod
    def multiplication(*numbers):
        if len(numbers) < 2:
            return cf.NEED_TWO_NUMBERS

        res = numbers[0]

        for n in numbers[1:]:
            res *= n
        return res

    @staticmethod
    def division(*numbers):
        if len(numbers) < 2:
            return cf.NEED_TWO_NUMBERS

        res = numbers[0]

        for n in numbers[1:]:
            if n == 0:
                return cf.DIVISION_BY_ZERO
            res /= n
        return res

    @staticmethod
    def division_truncate(*numbers):
        # its doesnt always return an integer and truncates

        if len(numbers) < 2:
            return cf.NEED_TWO_NUMBERS

        res = numbers[0]

        for n in numbers[1:]:
            if n == 0:
                return cf.DIVISION_BY_ZERO
            res //= n
        return res

    @staticmethod
    def exponentation(*numbers):
        if len(numbers) < 2:
            return cf.NEED_TWO_NUMBERS

        res = numbers[0]

        for n in numbers[1:]:
            res **= n
        return res

    @staticmethod
    def rest_division(*numbers):
        if len(numbers) < 2:
            return cf.NEED_TWO_NUMBERS

        res = numbers[0]

        for n in numbers[1:]:
            if n == 0:
                return cf.DIVISION_BY_ZERO
            res %= n
        return res

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

    def subtraction_input(self, *numbers):
        n = get_input_user()
        numbers = verify(n)
        if not numbers:
            show_result(cf.NEED_TWO_NUMBERS)
            return
        res = self.subt(*numbers)

        show_result(res)

    def multiplication_input(self, *numbers):
        n = get_input_user()
        numbers = verify(n)
        if not numbers:
            show_result(cf.NEED_TWO_NUMBERS)
            return
        res = self.multiplication(*numbers)

        show_result(res)

    """
        Division always returns a float, even when the numbers are integers.
    """

    def division_input(self, *numbers):
        n = get_input_user()
        numbers = verify(n)
        if not numbers:
            show_result(cf.NEED_TWO_NUMBERS)
            return
        res = self.division(*numbers)
        show_result(res)

    def division_truncate_input(self, *numbers):
        # its doesnt always return an integer and truncates
        n = get_input_user()
        numbers = verify(n)
        if not numbers:
            show_result(cf.NEED_TWO_NUMBERS)
            return
        res = self.division_truncate(*numbers)

        show_result(res)

    def exponentation_input(self, *numbers):
        n = get_input_user()
        numbers = verify(n)
        if not numbers:
            show_result(cf.NEED_TWO_NUMBERS)
            return
        res = self.exponentation(*numbers)

        show_result(res)

    def rest_division_input(
        self,
        *numbers,
    ):
        n = get_input_user()
        numbers = verify(n)
        if not numbers:
            show_result(cf.NEED_TWO_NUMBERS)
            return
        res = self.rest_division(*numbers)

        show_result(res)
