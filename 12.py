def main():
    print("Enter two numbers below.")
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    max_number(n1, n2)


def max_number(n1, n2):
    print(f"{max(n1, n2)} is greater than {min(n1, n2)}")


main()
