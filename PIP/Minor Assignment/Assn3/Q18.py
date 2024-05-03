x = int(input("Enter a non-negative integer : "))
y = int(input("Enter another non-negative integer : "))

term = f'{x}'

for i in range(1, y):
    term = term + '+' + str(x)

print(f'{x} * {y} = {term}')
