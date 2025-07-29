classA = 20
classB = 15
classC = 10


def main():
    print("Enter number of tickets sold based on each class below.")
    ticket_a = int(input("Class A: "))
    ticket_b = int(input("Class B: "))
    ticket_c = int(input("Class C: "))
    income_ca, income_cb, income_cc, total = sales(ticket_a, ticket_b, ticket_c)
    print(f"Income from Class A - ${income_ca}")
    print(f"Income from Class B - ${income_cb}")
    print(f"Income from Class C - ${income_cc}")
    print(f"Total Income - ${total}")


def sales(ticket_a, ticket_b, ticket_c):
    income_ca = ticket_a * classA
    income_cb = ticket_b * classB
    income_cc = ticket_c * classC
    total = income_ca + income_cb + income_cc
    return income_ca, income_cb, income_cc, total


if __name__ == '__main__':
    main()
