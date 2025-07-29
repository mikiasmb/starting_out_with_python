def main():
    number = int(input("Enter a number: "))
    print(is_prime(number))


def is_prime(number):
    o = number % number
    a = number % 1
    b = number % 2
    c = number % 3
    if (o == 0) and (a == 0) and ((b == 0) or (c == 0)):
        return False
    elif (o == 0) and (a == 0):
        return True


if __name__ == '__main__':
    main()
