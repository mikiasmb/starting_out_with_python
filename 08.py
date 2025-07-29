def main():
    sf = float(input("Enter the square feet of wall space to be painted: "))      # square feet
    ppg = float(input("Enter the price of the paint per gallon: "))             # price per gallon

    gallons = no_of_gallon(sf)
    labor_hrs = hrs_of_labor(sf)
    cost_paint = paint_cost(gallons, ppg)
    cost_labor = labor_cost(labor_hrs)
    total = total_cost(cost_paint, cost_labor)
    print()
    print(f"Num of gallons - {gallons} gallons")
    print(f"Hrs of labor - {labor_hrs:.2f} hrs")
    print(f"Paint cost - ${cost_paint:,.2f}")
    print(f"Labor cost - ${cost_labor:,.2f}")
    print(f"Total cost - ${total:,.2f}")


def no_of_gallon(sf):
    result = sf / 112
    return result


def paint_cost(gallons, ppg):
    result = ppg * gallons
    return result


def hrs_of_labor(sf):
    result = (sf * 8) / 112
    return result


def labor_cost(hrs_labor):
    result = hrs_labor * 35
    return result


def total_cost(cost_paint, cost_labor):
    result = cost_paint + cost_labor
    return result


if __name__ == '__main__':
    main()
