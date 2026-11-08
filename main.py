import pyperclip
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a message
message = input("Enter a message to encrypt: ")
encrypted = cipher.encrypt(message.encode())
print("Encrypted:", encrypted.decode())

# Copy the encrypted message to clipboard
pyperclip.copy(encrypted.decode())
print("Encrypted message copied to clipboard.")

# Decrypt the message
encrypted_message = input("Enter message to decrypt: ")
try:
    decrypted = cipher.decrypt(encrypted_message.encode())
    print("Decrypted:", decrypted.decode())

    # Copy the decrypted message to clipboard`
    pyperclip.copy(decrypted.decode())
    print("Decrypted message copied to clipboard.")
    
except Exception:
    print("Decryption failed. Please ensure the encrypted message is correct.")