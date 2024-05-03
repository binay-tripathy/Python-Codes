def repetitive(str):
    mod_str = str[0]
    for i in range(1, len(str)):
        if (str[i] == str[i-1]):
            mod_str += '*'
        else:
            mod_str += str[i]
    return mod_str


str = input("Enter a string: ")
print(repetitive(str))
