def main():
    file = open("golf.txt", "r")
    line = file.readline()
    while line != "":
        name = line.rstrip("\n")
        print(f"Name: {name}")
        score = file.readline().rstrip("\n")
        print(f"Score: {score}")
        line = file.readline()
    file.close()


if __name__ == '__main__':
    main()
