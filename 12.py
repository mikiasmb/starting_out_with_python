again = "y"  # Variable to control the loop for reading multiple lines
file_name = input("Enter file name: ")  # Prompt user to enter the file name

while True:  # Start an infinite loop to repeatedly ask for line numbers to read
    try:
        if again.lower() != "y":  # If the user doesn't want to continue, break the loop
            break
        else:
            # Open the file in read mode
            readFile = open(f"{file_name}.txt", "r")
            # Read all lines from the file and store them in a list
            datas = readFile.readlines()
            print(f"{file_name} has {len(datas)} lines.")  # Display the number of lines in the file
            print("Which line do you want to read.")
            readFile.close()  # Close the file
            read_line = int(input("Enter: "))  # Prompt user to enter the line number they want to read

            # Print the specified line (subtracting 1 because list indices start at 0)
            print(datas[read_line - 1].strip())

            # Ask if the user wants to read another line
            print("Do you want to read another line. \ny for yes anything else no.")
            again = input(": ")

    except IOError:  # Handle the case where the file cannot be found or opened
        print(f"{file_name} is not found.")
        break  # Exit the loop if the file cannot be found
    except ValueError:  # Handle invalid input for the line number (e.g., non-integer input)
        print("Error! Invalid input.")
    except IndexError:  # Handle invalid line number (e.g., out of range)
        print("Error! Invalid input.")
