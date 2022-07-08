from cryptography.fernet import Fernet

def load_key():
    # Load the previously generated key
    return open("unique.key", "rb").read()

key = load_key()
f = Fernet(key)

# type the encrypted string
message = # Do not include any '' or "" because the key CAN'T be a string!

# print decrypted string
decrypted_encrypted = f.decrypt(message)
print(decrypted_encrypted)