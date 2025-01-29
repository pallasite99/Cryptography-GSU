"""
Module for stream cipher encryption and decryption.
"""

import os

def generate_key_stream(length):
    """Generate a pseudorandom key stream of specified length."""
    if length <= 0:
        raise ValueError("Key stream length must be greater than zero.")
    return os.urandom(length)

def encrypt_decrypt(plaintext, key_stream):
    """Encrypt or decrypt plaintext using the XOR operation."""
    if len(plaintext) != len(key_stream):
        raise ValueError("Plaintext and key stream must be of the same length.")
    return bytes([pt ^ key for pt, key in zip(plaintext, key_stream)])
