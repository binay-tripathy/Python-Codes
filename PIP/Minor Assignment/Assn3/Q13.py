import math


x = int(input("Enter x : "))
n = int(input("Enter n : "))

sum = 1
for i in range(1, n, 1):
    if (i % 4 == 0):
        sum += pow(x, i)/math.factorial(n)
    elif (i % 2 == 0):
        sum -= pow(x, i)/math.factorial(n)
    else:
        sum += 0
print(sum)
