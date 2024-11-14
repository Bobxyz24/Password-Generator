# password_generator.py

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Sample usage
print("Generated Password:", generate_password(12))
