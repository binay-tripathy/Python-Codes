def month_cal(s):
    # switch = {
    #     "January" : 31,
    #     "February" : '28 or 29'
    # }

    # return switch.get(s)
    if(s == "January"):
        return 31
    

if __name__ == "__main__":
    month = input("Enter the month : ")
    print(month_cal(month))