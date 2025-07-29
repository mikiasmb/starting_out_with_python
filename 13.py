def main():
    time = int(input("Enter object’s falling time (in seconds): "))
    print(f"The object falls - {falling_distance(time):,.2f} meter.")


def falling_distance(time):
    if 1 <= time <= 10:
        d = (.5 * 9.8) * time ** 2
        return d
    else:
        d = "Time exceeds limit"
        return d


main()
