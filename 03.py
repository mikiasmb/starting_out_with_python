def main():
    file_name = input("Enter file name to read: ")
    try:
        file = open(f"{file_name}.txt", "r")
        line_num = 1
        for line in file:
            print(f"{line_num}: {line.rstrip("\n")}")
            line_num += 1
        file.close()
    except IOError:
        print(f"Error: The file '{file_name}' was not found.")


if __name__ == '__main__':
    main()
