
#Assignment 4 Q1

##import pdb
##pdb.set_trace()

'''breakpoint()
def summation(n):
    total=0
    for count in range (1,n):
        total+=count
    return total

def main():
    n=int(input("Enter number of terms:"))
    total=summation(n)
    print("Sum of first",n,"positive integers:",total)

if __name__=='__main__':
    main()'''

#Assignment 4 Q2
'''
breakpoint()
def invertedRightTriangle(nRows):
    for i in range(nRows,0):
        print("*"*i)

def main():
    nRows=int(input("Enter number of rows:"))
    invertedRightTriangle(nRows)
    print("Done")

if __name__=='__main__':
    main()
'''



#Assignment 4 Q3
'''
breakpoint()
def main():
    totalMarks=0
    i=0
    while True:
        marks=input("Enter marks for subject"+str(i+1)+":")
        if marks=='':
            break
        marks=int(marks)
        if marks<0 or marks>100:
            print("Invalid marks!!")
            continue
        i+=1
        totalMarks+=marks
    percentage=totalMarks//i
    print("Totalmarks",int(totalMarks))
    print("Percentage",round(percentage,2))

if __name__=='__main__':
    main()
'''



#Assignment 4 Q4
'''
breakpoint()
def isLeapYear(year):
    return year%400==0 or year%100==0 and year%4==0
year=int(input("Enter year:"))
print(isLeapYear(year))
'''


#Assignment 4 Q5
'''
breakpoint()
def findHCF(num1,num2):
    if num1<num2:
        minNum=num1
    else:
        minNum=num2
    for i in range(minNum,1,-1):
        if num1%i==0 and num2%i==0:
            HCF=i
    return HCF

def main():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print(findHCF(num1,num2))

if __name__=='__main__':
    main()
'''

