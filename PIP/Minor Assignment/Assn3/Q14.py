x = int(input("Enter a number : "))
temp = x
rev = 0

while (x > 0):
    rev *= (10+(x % 10))
    x //= 10
if (temp == rev):
    print("true")
else:
    print("false")
