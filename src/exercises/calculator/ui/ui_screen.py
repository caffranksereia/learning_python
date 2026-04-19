import src.exercises.calculator.config as cf


def screen(phrase):
    print(cf.loading_screen_phrases, end="")
    for _ in range(cf.number_range):
        time.sleep(cf.timer_to_sleep)
        print("|", end="", flush=True)
    print(f"{phrase}\n")
