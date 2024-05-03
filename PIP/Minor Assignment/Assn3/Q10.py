num1= int(input("Enter 1st number : "))
num2= int(input("Enter 2nd number : "))

# lcm = 1
max = max(num1,num2)
min = min(num1,num2)
if(max % min == 0):
    print ("The LCM is : ", max)
else:
    # for i in range(max,num1*num2, max+1):
    #     # if(num1%i == 0 or num2%i == 0):
    #     #     lcm*=i
    #     if(i%num1 == 0 and i%num2 == 0):
    #         print ("The LCM is : ", i)

    while(max<(num1*num2)):
        if(max%num1 == 0 and max%num2 == 0):
            print ("The LCM is : ", max)
            break
        max = max+1
    else:
        print("The LCM is : ", num1*num2)