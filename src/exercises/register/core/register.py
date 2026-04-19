from datetime import datetime
import config as cf


class RegisterUser:

    def run(self):
        name = input(cf.NAME_INPU).strip()
        last_name = input(cf.LAST_NAME).strip()

        age_input = input(cf.OLD_AGE).strip()
        age = self.verify_digit_and_convert(age_input)

        if age is None:
            print("Invalid age")
            return None

        birthday_input = input(cf.BIRTHDAY_INPUT).strip()
        birthday = self.verify_is_valid_date(birthday_input)

        if birthday is None:
            print(cf.INVALID_BIRTH)
            return None

        height_input = input(cf.HEIGHT_INPUT).strip()
        height = self.convert_height(height_input)

        if height is None:
            print(cf.INVALID_HEIGHT)
            return None

        age_verification = self.verify_age(age)

        return {
            "Name": name,
            "Last Name": last_name,
            "Age": age,
            "Birthday": birthday.strftime(cf.DATE_FORMAT),
            "Age verification": age_verification,
            "Height (m)": height,
        }

    def verify_digit_and_convert(self, value):
        try:
            return int(value)
        except ValueError:
            return None

    def convert_height(self, height):
        height_converting = self.verify_digit_and_convert(height)

        if height_converting is None:
            return None

        return height_converting / cf.NUMBER_CONVERT_METERS

    @staticmethod
    def verify_age(age):
        return cf.legal if age >= cf.OF_LEGAL_AGE else cf.NOT_LEGAL

    @staticmethod
    def verify_is_valid_date(birthday):
        try:
            return datetime.strptime(birthday, cf.DATE_FORMAT)
        except ValueError:
            return None
