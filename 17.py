print("Reboot the computer and try to connect.")
p1 = input("Did that fix the problem? ")
if p1.lower() == "no":
    print("Reboot the router and try to connect. ")
    p2 = input("Did that fix the problem? ")
    if p2.lower() == "no":
        print("Make sure the cables between the router & modem are plugged in firmly.")
        p3 = input("Did that fix the problem? ")
        if p3.lower() == "no":
            print("Move the router to a new location and try to connect.")
            p4 = input("Did that fix the problem? ")
            if p4.lower() == "no":
                print("Get a new router.")
            elif p4.lower() == 'yes':
                exit()
        elif p3.lower() == 'yes':
            exit()
    elif p2.lower() == 'yes':
        exit()
elif p1.lower() == 'yes':
    exit()

                                       # the use of .lower() function is to change the user input to lowercase
                                   # the use of exit() function is to exit the code

