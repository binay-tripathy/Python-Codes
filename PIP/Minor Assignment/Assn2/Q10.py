def sum_even():
    # sum = 0
    # while(n!=0):
    #     num = n%10
    #     n//=10
    #     if(num%2==0):
    #         sum+=num
    n = int(input("Enter a four digit number : "))
    num = n%10
    sum = (1-num%2) * num
    n//=10
    num = n%10
    sum += (1-num%2) * num
    n//=10
    num = n%10
    sum += (1-num%2) * num
    n//=10
    num = n%10
    sum += (1-num%2) * num
    print(sum)

if __name__ == '__main__':
    sum_even()