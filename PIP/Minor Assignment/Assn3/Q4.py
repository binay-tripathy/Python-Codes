import random
n = random.randrange(0,38)
if(n==37):
    print("The spin resulted in 00")
else:
    print ("The spin resulted in ", n)

#Pay
if(n == 37):
    print("Pay 00")
else:
    print("Pay : ", n)

#Color
if((0<n<10 and n%2!=0) or (10<n<19 and n%2 == 0) or (19<n<29 and n%2 !=0) or (29<n<37 and n%2 == 0)):
    print("Red")
elif (n == 0 or n == 37):
    pass
else:
    print("Black")


#Odd_even
if(n == 0 or n==37):
    pass
elif(n%2 == 0):
    print("Even")
else:
    print("Odd")

#number_versus
if(n == 0 or n==37):
    pass
elif(1<=n<=18):
    print("Pay 1 to 18")
else:
    print("Pay 19 to 36")
