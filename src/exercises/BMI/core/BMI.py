import src.exercises.BMI.config as cf


class BmiUser:
    def run(self):
        self.question_user()

    @staticmethod
    def calc_bmi(weight, height):
        bmi = weight / (height**2)

        return bmi

    @staticmethod
    def show_result(name, height, weight, bmi, category):
        print(
            f"{name} has {height:.2f}m height, {weight:.2f}kg weight, "
            f"{bmi:.2f} BMI, category: {category}"
        )

    @staticmethod
    def get_float_input(message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print(cf.INVALID_MESSAGE)

    def question_user(self):
        name = input(cf.MESSAGE_START).split()
        height = self.get_float_input(input(cf.MESSAGE_HEIGHT))
        weight = self.get_float_input(input(cf.MESSAGE_WEIGHT))

        bmi = self.calc_bmi(height, weight)
        category = self.classfy_bmi(bmi)

        self.show_result(name, height, weight, bmi, category)

    def classify_bmi(
        self,
        bmi,
    ):
        if bmi <= cf.MENOR:
            return cf.MENOR_INDICE
        elif bmi <= cf.NORMAL:
            return cf.NORMAL_INDICE
        elif bmi <= cf.OVERWEIGHT:
            return cf.OVERWEIGHT_INDICE
        elif bmi <= cf.OBESITY_GRAU_1:
            return cf.OBESITY_GRAU_1_INDICE
        else:
            cf.OBESITY_GRAU_GRAVE_INDICE
