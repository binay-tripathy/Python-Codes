humanAge = int(input("Enter the human age : "))
assert humanAge > 0
dogAge=10.5
if(humanAge<2):
    print("Dog Age = " , dogAge*humanAge, " years")

elif(humanAge>=2):
    print("Dog Age = " , ((humanAge-2)*4) + (dogAge*2), " years")