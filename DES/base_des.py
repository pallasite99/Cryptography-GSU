"""
Module for basic DES encryption and decryption.
"""
import binascii  # Standard library import
from Cryptodome.Cipher import DES  # Third-party library import

def pad(text):
    """Pads input text to make it a multiple of 8 bytes."""
    while len(text) % 8 != 0:
        text += ' '
    return text

# Define an 8-byte key
KEY = b'8bytekey'  # Must be exactly 8 bytes

# Create a DES cipher in ECB mode
CIPHER = DES.new(KEY, DES.MODE_ECB)

# Encrypt
PLAINTEXT = "Hello123"
PADDED_TEXT = pad(PLAINTEXT)
CIPHERTEXT = CIPHER.encrypt(PADDED_TEXT.encode())
print("Ciphertext:", binascii.hexlify(CIPHERTEXT))

# Decrypt
DECRYPTED_TEXT = CIPHER.decrypt(CIPHERTEXT).decode().strip()
print("Decrypted:", DECRYPTED_TEXT)
