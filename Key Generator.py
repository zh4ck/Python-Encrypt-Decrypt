from cryptography.fernet import Fernet

def write_key():
    # Generate a new key and save it as a .key file
    key = Fernet.generate_key()
    with open("unique.key", "wb") as key_file:
        key_file.write(key)

write_key()