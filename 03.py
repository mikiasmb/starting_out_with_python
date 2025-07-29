def main():
    cost = float(input("Enter the replacement cost of a building: "))
    print(insurance(cost))


def insurance(cost):
    result = cost * .8
    return f"${result}"


main()
