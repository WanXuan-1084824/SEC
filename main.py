from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

cipher = Fernet(key)
# Encrypt a message
message = input("Enter a message to encrypt: ")
encrypted = cipher.encrypt(message.encode())
print("Encrypted:", encrypted.decode())

# Decrypt the message
encrypted_message = input("Enter message to decrypt: ")
try:
    decrypted = cipher.decrypt(encrypted_message.encode())
    print("Decrypted:", decrypted.decode())
except Exception:
    print("Decryption failed. Please ensure the encrypted message is correct.")