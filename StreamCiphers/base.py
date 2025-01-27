import os

def generate_key_stream(length):
    """Generate a pseudorandom key stream of specified length."""
    return os.urandom(length)

def encrypt_decrypt(plaintext, key_stream):
    """Encrypt or decrypt plaintext using the XOR operation."""
    return bytes([pt ^ key for pt, key in zip(plaintext, key_stream)])

# Example usage
plaintext = b"Hello, Stream Cipher!"
key_stream = generate_key_stream(len(plaintext))

# Encrypt the plaintext
ciphertext = encrypt_decrypt(plaintext, key_stream)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_text = encrypt_decrypt(ciphertext, key_stream)
print("Decrypted Text:", decrypted_text)
