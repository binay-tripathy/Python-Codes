def UpperCase(str):
    print(str.upper())
def main():
    str = input("Enter a string in lowercase : ")
    assert str.islower()
    UpperCase(str)
if __name__ == '__main__':
    main()