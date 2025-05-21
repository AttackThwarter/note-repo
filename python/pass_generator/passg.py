import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        count = int(input("Enter the number of passwords: "))
        length = int(input("Enter the length of each password: "))
        
        passwords = [generate_password(length) for _ in range(count)]
        
        print("\nGenerated passwords:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}: {pwd}")
        input("\nPress Enter to exit...")
        
    except ValueError:
        print("Please enter a valid number!")




if __name__ == "__main__":
    main()
