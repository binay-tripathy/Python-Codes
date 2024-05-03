num = int(input("Enter a four digit number : "))
sum = 0
# for i in range(0, 4):
#     sum += num%10
#     num//=10
sum = num%10
term = str(num%10)
num//=10
sum+=num%10
term = str(num%10) + ' + ' + term 
num//=10
sum+=num%10
term = str(num%10) + ' + ' + term
num//=10
sum+=num%10
term = str(num%10) + ' + ' + term
print(term , ' = ' , sum)