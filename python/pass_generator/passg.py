import random
import os
import gc
import string
from time import sleep

def generate_password(length=12):
    letters_digits = string.ascii_letters + string.digits
    special_chars = "@!#$%^&*()=+"
    
    all_chars = letters_digits + special_chars
    
    password = random.choice(special_chars)
    
    remaining_length = length - 1
    password += ''.join(random.choice(all_chars) for _ in range(remaining_length))
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def secure_clear(var):
    if isinstance(var, list):
        for i in range(len(var)):
            var[i] = '0' * len(var[i]) if isinstance(var[i], str) else 0
    elif isinstance(var, str):
        var = '0' * len(var)
    return None

def main():
    try:
        count = int(input("Enter the number of passwords: "))
        length = int(input("Enter the length of each password: "))
        
        passwords = [generate_password(length) for _ in range(count)]
        
        print("\nGenerated passwords:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}: {pwd}")
            
        
        print("\n1 minute to CLEAR")
        sleep(60)
        
        secure_clear(passwords)
        
        gc.collect()
        
    except ValueError:
        print("Please enter a valid number!")
    finally:
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
