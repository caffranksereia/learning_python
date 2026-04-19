from .core.register import RegisterUser


def main():
    app = RegisterUser()
    user = app.run()
    if user:
        print("\nUser data:", user)


if __name__ == "__main__":
    main()
