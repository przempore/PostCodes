def printPostCode(first, second):
    for f in range(int(first), 100, 1):
        for s in range(int(second), 1000, 1):
            print "{:02d}-{:03d}".format(f, s)


def main():
    f, s = raw_input("Give start postcode in format xx-xxx ").split("-")
    printPostCode(f, s)


if __name__ == "__main__":
    main()