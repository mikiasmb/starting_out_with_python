again = "y"
file_name = input("Enter file name (without extension): ")

while True:
    try:
        if again.lower() != "y":
            break

        with open(f"{file_name}.txt", "r") as readFile:
            datas = readFile.readlines()
            print(f"{file_name} has {len(datas)} lines.")
            read_line = int(input("Which line do you want to read: "))

            if read_line <= 0 or read_line > len(datas):
                raise IndexError("Line number out of range")

            print(datas[read_line - 1].strip())
            print("Do you want to read another line? \ny for yes, anything else for no.")
            again = input(": ")

    except IOError:
        print("Error! File not found or cannot be opened.")
        break
    except ValueError:
        print("Error! Invalid input. Please enter a valid line number.")
    except IndexError as e:
        print(f"Error! {e}")

print("Goodbye!")
