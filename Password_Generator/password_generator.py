import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine the character sets based on user preferences
    all_chars = lower
    if use_uppercase:
        all_chars += upper
    if use_digits:
        all_chars += digits
    if use_special:
        all_chars += special

    # Ensure at least one character from each selected set is in the password
    password = []
    if use_uppercase:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))

    # Fill the rest of the password length with random characters from the combined set
    password.extend(random.choice(all_chars) for _ in range(length - len(password)))

    # Shuffle the password list to avoid predictable sequences
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

def main():
    print("Password Generator")

    # Prompt the user to specify the length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 4:
                print("Password length should be at least 4 to include all character types.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Prompt the user to specify character type preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_special)

    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
