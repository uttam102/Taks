import random
import string

def generate_password(length):
    """
    Generate a strong random password with a mix of letters, numbers, and symbols.
    
    Args:
        length (int): The desired length of the password
        
    Returns:
        str: A randomly generated password
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols
    
    # Ensure the password contains at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)


def main():
    """
    Main function to run the password generator program.
    """
    print("=" * 50)
    print("STRONG PASSWORD GENERATOR")
    print("=" * 50)
    
    while True:
        try:
            # Get password length from user
            length = int(input("\nEnter the desired password length (minimum 4): "))
            
            # Validate input
            if length < 4:
                print("Password length must be at least 4 characters!")
                continue
            
            # Generate password
            password = generate_password(length)
            
            # Display the generated password
            print("\n" + "=" * 50)
            print(f"Your generated password is: {password}")
            print("=" * 50)
            
            # Ask if user wants to generate another password
            another = input("\nGenerate another password? (y/n): ").lower()
            if another != 'y':
                print("\n Thank you for using the Password Generator!")
                break
                
        except ValueError:
            print(" Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\n Program terminated by user.")
            break


if __name__ == "__main__":
    main()