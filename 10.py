def main():
    feet = int(input("Enter a number of feet: "))
    print(f"{feet_to_inches(feet)} inches in {feet} feet")


def feet_to_inches(feet):
    result = feet * 12
    return result


main()
