def main():
    km = float(input("Enter distance in kilometer: "))
    print(miles(km))


def miles(km):
    ml = km * 0.6214
    return f"{ml:,.2f}"


main()
