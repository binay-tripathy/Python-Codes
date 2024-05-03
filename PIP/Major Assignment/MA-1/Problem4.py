import random

def generate_random_password():
    length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for i in range(length))
    return password

if __name__ == "__main__":
    password = generate_random_password()
    print(f"Randomly generated password: {password}")
