def hex2int(hex_digit):
    hex_digit = hex_digit.upper()
    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    if hex_digit not in hex_map:
        print("Error: Invalid hexadecimal digit.")
        exit()

    return hex_map[hex_digit]

def int2hex(decimal_num):
    if not 0 <= decimal_num <= 15:
        print("Error: Input value must be between 0 and 15.")
        exit()

    hex_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
               8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    return hex_map[decimal_num]



hex_input = input("Enter a hexadecimal digit: ")
decimal_result = hex2int(hex_input)
print(f"The decimal equivalent of {hex_input} is {decimal_result}.")



decimal_input = int(input("Enter a decimal number between 0 and 15: "))
hex_result = int2hex(decimal_input)
print(f"The hexadecimal equivalent of {decimal_input} is {hex_result}.")
