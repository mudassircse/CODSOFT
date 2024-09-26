import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_chars

    # Ensure password contains at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    # User input for password length
    length = int(input("Enter the desired password length: "))
    
    # Generate and display password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
