import hashlib
import random
import string


def hash_password(password):
    """
    Convert the password into a SHA-256 hash.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def generate_strong_password(length=16):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*"

    all_characters = uppercase + lowercase + digits + symbols

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return "".join(password)