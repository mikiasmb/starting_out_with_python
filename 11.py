def main():
    # Get the 3x3 grid of numbers from the user
    lo_shu_square = get_numbers()

    # Display the square
    print()
    lo(lo_shu_square)
    print()

    # Check if rows, columns, and diagonals sum to 15
    check_rows(lo_shu_square)
    check_columns(lo_shu_square)
    check_main_diagonal(lo_shu_square)
    check_secondary_diagonal(lo_shu_square)


def get_numbers():
    # Initialize a 3x3 list with zeros
    lo_shu_square = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

    # Populate the 3x3 list with user input
    for row in range(3):
        for col in range(3):
            number = int(input("Enter a number: "))
            lo_shu_square[row][col] = number

    return lo_shu_square


def lo(square):
    for i in range(3):
        for j in range(3):
            print(square[i][j], end=" ")
        print()


def check_rows(square):
    for row in range(3):
        total = sum(square[row])  # Sum the elements in the row
        if total > 15:
            print(f"Row {row + 1} is greater than 15.")
        elif total < 15:
            print(f"Row {row + 1} is less than 15.")
        else:
            print(f"Row {row + 1} sums to 15.")


def check_columns(square):
    for col in range(3):
        total = sum(square[row][col] for row in range(3))  # Sum the elements in the column
        if total > 15:
            print(f"Column {col + 1} is greater than 15.")
        elif total < 15:
            print(f"Column {col + 1} is less than 15.")
        else:
            print(f"Column {col + 1} sums to 15.")


def check_main_diagonal(square):
    # Sum the elements in the main diagonal
    total = sum(square[i][i] for i in range(3))
    if total > 15:
        print("Main diagonal is greater than 15.")
    elif total < 15:
        print("Main diagonal is less than 15.")
    else:
        print("Main diagonal sums to 15.")


def check_secondary_diagonal(square):
    # Sum the elements in the secondary diagonal
    total = sum(square[i][2 - i] for i in range(3))
    if total > 15:
        print("Secondary diagonal is greater than 15.")
    elif total < 15:
        print("Secondary diagonal is less than 15.")
    else:
        print("Secondary diagonal sums to 15.")


if __name__ == '__main__':
    main()
