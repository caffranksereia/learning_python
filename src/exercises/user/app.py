from .core.package_user import get_info_user


def main():
    user = get_info_user()
    if user:
        print("\nReturned data:", user)


if __name__ == "__main__":
    main()
