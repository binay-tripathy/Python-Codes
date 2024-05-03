def anagrams(str1, str2):
    if (sorted(str1) == sorted(str2)):
        return True
    else:
        return False


str1 = input("Enter 1st string : ")
str2 = input("Enter 2nd string : ")
print(anagrams(str1, str2))
