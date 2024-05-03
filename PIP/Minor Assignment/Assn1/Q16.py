days = eval(input("Enter the no of days : "))
hours = eval(input("Enter the no of hours : "))
minutes = eval(input("Enter the no of minutes : "))
seconds = eval(input("Enter the no of seconds : "))
t_seconds = (days*24*60*60) + (hours*60*60) + (minutes*60) + seconds
print("The no of seconds is : " , t_seconds)