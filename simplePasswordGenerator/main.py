import random
import string

def gen_password(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    password = ''.join(random.choice(letters) for i in range(length))
    return password

if __name__ == "__main__":
	print("How long would you like your password to be?")
	inp = int(input("> "))
	print(gen_password(inp))