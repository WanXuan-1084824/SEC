from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

cipher = Fernet(key)
# Encrypt a message
message = b"Hello, this is a secret message!"
encrypted = cipher.encrypt(message)
print("Encrypted:", encrypted)

# Decrypt the message
decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted.decode())