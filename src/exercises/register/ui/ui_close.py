import src.exercises.register.config as cf
from src.exercises.register.ui.ui_screen import screen


def close():
    screen("Bye... bye...")
    print(cf.EXIT_MESSAGE)
