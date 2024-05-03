num1= int(input("Enter 1st number : "))
num2= int(input("Enter 2nd number : "))

max = max(num1,num2)
min = min(num1,num2)

if(max % min == 0):
    print ("The GCD is : ", min)
else:
    while(min>1):
        if(num1%min == 0 and num2%min == 0):
            print ("The GCD is : ", min)
            break
        min -= 1
    else:
        print("The GCD is : ", 1)