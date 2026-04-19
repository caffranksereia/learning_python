import config as cf


class NumberMaiorOrMinor:
    def run(self):
        return self.get_info_user()

    def get_info_user(self):
        try:
            first_number = int(input(cf.FIRST_NUMBER))
            second_number = int(input(cf.SECOND_NUMBER))
            rest = self.classify_decision(first_number, second_number)

            return rest

        except ValueError:
            print("Not is number!")
            return

    @staticmethod
    def classify_decision(first_number, second_number):

        if first_number > second_number and first_number >= second_number:
            print(
                f"first number {first_number=} is greater than or equal to second {second_number=}"
            )
        elif first_number < second_number and first_number <= second_number:
            print(
                f"first number {first_number=} is less than or equal to second {second_number=}"
            )
        elif first_number == second_number:
            print(f"first number {first_number=} is equal to second {second_number=}")
        elif first_number != second_number:
            print(f"first number {first_number=} is not equal to  {second_number=}")
        else:
            print("nothing here")
