import random
import string

def generate_password(length, use_uppercase, use_special, use_numbers):
    # Base character set
    character_set = string.ascii_lowercase  # Always include lowercase letters

    if use_uppercase:
        character_set += string.ascii_uppercase  # Add uppercase letters
    if use_special:
        character_set += string.punctuation  # Add special characters
    if use_numbers:
        character_set += string.digits  # Add numbers

    print(f"Character set used for generation: {character_set}")  # Display character set for debugging

    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    # Ask if the user wants to specify the length
    specify_length = input("Would you like to specify a length for the password? (y/n): ").lower() == 'y'

    if specify_length:
        length = int(input("Enter the desired password length (minimum 8 characters, maximum 100 characters): "))
        while length < 8 or length > 100:
            print("Please enter a length between 8 and 100 characters.")
            length = int(input("Enter the desired password length: "))
    else:
        length = 12  # Default length

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_special = input("Include special characters (e.g. !@#$%^&*)? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    
    # Generate and display the password
    password = generate_password(length, use_uppercase, use_special, use_numbers)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
