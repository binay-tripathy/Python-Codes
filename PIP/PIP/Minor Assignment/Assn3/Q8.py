num= int(input("Enter a number : "))
sum = 0
for i in range(1,num):
    if(num%i == 0):
        sum+=i

if(num == sum):
    print("The number is a perfect no")
else:
    print("The number is not a perfect no")