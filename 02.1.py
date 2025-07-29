def main():
    file = open("file.txt", "r")
    count = 0
    line_num = 1
    line = file.readline()
    while line != "":
        count += line_num
        line = file.readline()
    file.close()
    k = open("file.txt", "r")
    if count < 5:
        read_all = k.read().rstrip("\n")
        print(read_all)
    elif count >= 5:
        for i in range(3):
            a = k.readline().rstrip("\n")
            print(a)
    k.close()


if __name__ == '__main__':
    main()
