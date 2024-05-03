num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

max = max(num1, num2)
min = min(num1, num2)
gcd = 1

if (max % min == 0):
    gcd = min
else:
    while (min > 1):
        if (num1 % min == 0 and num2 % min == 0):
            gcd = min
            break
        min -= 1
    else:
        gcd = 1

if (gcd == 1):
    print("The nos are coprime")
