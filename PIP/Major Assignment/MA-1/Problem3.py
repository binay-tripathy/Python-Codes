def arbitrary_to_10(number, base):
    decimal = 0
    power = 0

    while number != 0:
        digit = number % 10
        if digit >= base:
            print("Invalid digit for the given base.")
            exit()
        decimal += digit * (base ** power)
        number //= 10
        power += 1

    return decimal


def base10_to_arbitrary(decimal, base):
    result = ""
    while decimal != 0:
        remainder = decimal % base
        if remainder > 9:
            result = chr(65 + remainder - 10) + result
        else:
            result = str(remainder) + result
        decimal //= base

    return result


def main():
    input_num = input("Enter the number: ")
    input_base = int(input("Enter the base of the input number (between 2 and 16): "))
    output = int(input("Enter the base to convert to (between 2 and 16): "))

    if not (2 <= input_base <= 16 and 2 <= output <= 16):
        print("Bases must be between 2 and 16.")
        exit()

    decimal = arbitrary_to_10(int(input_num), input_base)

    result = base10_to_arbitrary(decimal, output)

    print(f"The number {input_num} in base {input_base} is {result} in base {output}.")


if __name__ == "__main__":
    main()
