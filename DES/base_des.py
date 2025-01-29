from Cryptodome.Cipher import DES
import binascii

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Define an 8-byte key
key = b'8bytekey'  # Must be exactly 8 bytes

# Create a DES cipher in ECB mode
cipher = DES.new(key, DES.MODE_ECB)

# Encrypt
plaintext = "Hello123"
padded_text = pad(plaintext)
ciphertext = cipher.encrypt(padded_text.encode())
print("Ciphertext:", binascii.hexlify(ciphertext))

# Decrypt
decrypted_text = cipher.decrypt(ciphertext).decode().strip()
print("Decrypted:", decrypted_text)
