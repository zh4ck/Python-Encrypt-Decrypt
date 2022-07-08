from cryptography.fernet import Fernet

def load_key():
    # Load the previously generated key
    return open("unique.key", "rb").read()

key = load_key()
f = Fernet(key)

# type message to be encrypted
message = input().encode()

# encrypt the message
encrypted = f.encrypt(message)

# print the encrypted message
print(encrypted)