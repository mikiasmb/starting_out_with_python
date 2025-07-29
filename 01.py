def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(f"Initials: {get_initials(first_name, last_name)}")
    print(f"Full name: {get_fullname(first_name, last_name)}")
    print(f"Short name: {get_shortname(first_name, last_name)}")


def get_initials(first_name, last_name):
    initials = first_name[0] + "." + last_name[0]
    return initials.title()


def get_fullname(first_name, last_name):
    fullname = first_name + " " + last_name
    return fullname.title()


def get_shortname(first_name, last_name):
    shortname = first_name[0] + last_name
    return shortname


if __name__ == '__main__':
    main()
