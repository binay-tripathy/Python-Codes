import pdb
pdb.set_trace()


def invertedRightTriangle(nRows):
    for i in range(nRows, 0):  # need to add a decrement operator
        print("*"*i)


def main():
    nRows = int(input("Enter number of rows:"))
    invertedRightTriangle(nRows)
    print("Done")


if __name__ == '__main__':
    main()
