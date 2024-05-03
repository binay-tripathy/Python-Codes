# import math
# def f(x):
#   result = 0
#   for i in range(1, 50, 4):
#     result += math.pow(x, i)/math.factorial(i)
#   for i in range(3, 50, 4):
#     result += math.pow(x, i)/math.factorial(i)
#   return result

# x = float(input("Enter the value of x: "))
# result1 = f(x)
# result2 = math.sin(x)
# print(result2 - result1)
# print((result2 - result1) > (1e-6))


def palin(str):
    if (str[:] == str[::-1]):
      print("Plaindrome")
    else:
       print("Not palin")
palin("malayalam")