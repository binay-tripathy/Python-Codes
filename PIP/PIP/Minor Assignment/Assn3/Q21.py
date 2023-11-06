n = int(input("Enter a number : "))

if (n < 2):
    print("Invalid")
else:
    factor = 2
    while (factor <= n):
        if (n % factor == 0):
            print(factor)
            n //= factor
        else:
            factor += 1
