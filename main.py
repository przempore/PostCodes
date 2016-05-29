class PostCode:
    preCode = 0
    postCode = 0

    def __init__(self, pre, post):
        self.preCode = pre
        self.postCode = post

    def __lt__(self, other):
        if self.preCode < other.preCode:
            return self.preCode < other.preCode
        elif self.preCode == other.preCode:
            return self.postCode < other.postCode

    def __gt__(self, other):
        if self.preCode > other.preCode:
            return self.preCode > other.preCode
        elif self.preCode == other.preCode:
            return self.postCode > other.postCode

    def __eq__(self, other):
        return self.preCode == other.preCode and self.postCode == other.postCode

    def __add__(self, other):
        tmp = PostCode(0, 0)
        tmp.preCode = self.preCode + other.preCode
        if tmp.preCode >= 99:
            tmp.preCode = 0

        tmp.postCode = self.postCode + other.postCode
        if tmp.postCode >= 1000:
            tmp.preCode += 1
            tmp.postCode -= 1000
        return tmp

    def Print(self):
        print "{:02d}-{:03d}".format(self.preCode, self.postCode)


def printPostCode(firstPre, firstPost, secondPre, secondPost):
    first = PostCode(firstPre, firstPost)
    second = PostCode(secondPre, secondPost)

    first.Print()
    while(True):
        first += PostCode(0, 001)
        first.Print()
        if first == second:
            break
        pass


def main():
    try:
        f, s = raw_input("Type start post code: (in format xx-xxx) ").split("-")
        f2, s2 = raw_input("Type end post code: (in format xx-xxx) ").split("-")
    except ValueError:
        print "Wrong input data"

    printPostCode(int(f), int(s), int(f2), int(s2))

if __name__ == "__main__":
    main()