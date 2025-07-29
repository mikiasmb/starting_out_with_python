state_str = .05       # sales tax
country_str = .025       # rate


def main():
    total_sales = float(input("Enter the total sales for the month: "))

    cst = country_sales_tax(total_sales)
    sst = state_sales_tax(total_sales)
    total = cst + sst

    print(f"The amount of country sales tax - ${cst:,.2f}")
    print(f"The amount of state sales tax - ${sst:,.2f}")
    print(f"The total sales tax - ${total:,.2f}")


def country_sales_tax(total_sales):
    result = total_sales * country_str
    return result


def state_sales_tax(total_sales):
    result = total_sales * state_str
    return result


if __name__ == '__main__':
    main()
