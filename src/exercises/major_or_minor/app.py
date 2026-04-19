from .core.major_or_minor import NumberMaiorOrMinor


def main():
    number = NumberMaiorOrMinor()
    rest = number.run()
    print(rest)


if __name__ == "__main__":
    main()
