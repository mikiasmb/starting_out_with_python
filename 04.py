def main():
    loan, insurance, gas, oil, tires, maintenance = inputs()
    print(f"Monthly cost - ${monthly(loan, insurance, gas, oil, tires, maintenance)}")
    print(f"Annual cost - ${annual(loan, insurance, gas, oil, tires, maintenance)}")


def inputs():
    print("Enter the monthly cost of the following.")
    loan = float(input("Loan payment: "))
    insurance = float(input("Insurance: "))
    gas = float(input("Gas: "))
    oil = float(input("Oil: "))
    tires = float(input("Tires: "))
    maintenance = float(input("Maintenance: "))
    return loan, insurance, gas, oil, tires, maintenance


def monthly(loan, insurance, gas, oil, tires, maintenance):
    cost = loan + insurance + gas + oil + tires + maintenance
    return cost


def annual(loan, insurance, gas, oil, tires, maintenance):
    cost = 12 * (loan + insurance + gas + oil + tires + maintenance)
    return cost


if __name__ == '__main__':
    main()
