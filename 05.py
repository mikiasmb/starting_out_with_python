def main():
    value = float(input("Enter the actual value of a piece of property: "))
    print(f"Assessment value - ${assessment(value)}")
    print(f"Property tax - ${property_tax(assessment(value))}")


def assessment(value):
    result = value * .6
    return result


def property_tax(result):
    tax = (result * .72) / 100
    return f"{tax:,.2f}"


if __name__ == '__main__':
    main()
