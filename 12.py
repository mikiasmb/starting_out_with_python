def main():
    file = open("steps.txt", "r")
    total = 0
    all = 0
    for i in range(12):
        for j in range(30):
            line = int(file.readline())
            total += line
        print(f"Month {i+1} = {total}")
        all += total
    print(all)


if __name__ == '__main__':
    main()
