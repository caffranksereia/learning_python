import config as cf


def get_info_user():

    name = input(cf.SAY_NAME).strip()
    age_input = input(cf.AGE).strip()

    age = convert_to_int(age_input)

    if age is None:
        print(cf.INVALID_INPUT)
        return None

    res = package_info(name, age)
    return res


def package_info(name, age):
    if not name or not age:
        print(cf.INVALID_INPUT)
    data = [name, age]

    print("\n--- User Info ---")
    print(f"Name: {name}")
    print(f"Age: {age}")

    print(data[0])
    print(data[0][0])
    if len(name) > 12:
        print(data[12])

    print(data[0][::-1])
    print(len(name))

    if " " in data[0]:
        print(cf.SPACE_YOU_HAVE_YOUR_NAME)
    else:
        print(cf.NOT_HAVE_SPACE)

    return {
        "name": name,
        "age": age,
    }


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None
