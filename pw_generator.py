# the following code creates a password for you

import random
import string

while True:
    try:
        # Try to convert the input to an integer
        length = int(input("How many characters would you like your password to be? "))
        
        # If the input is successfully converted, generate the password
        def generate_password(length):
            # Define the character set
            characters = string.ascii_letters + string.digits + string.punctuation
        
            # Generate a random password
            password = ''.join(random.choice(characters) for i in range(length))
        
            return password

        print("Generated Password:", generate_password(length))
        break

    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Incorrect response detected. Please enter numbers only.")
        

