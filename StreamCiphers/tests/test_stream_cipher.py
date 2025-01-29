"""
Tests for stream cipher encryption and decryption.
"""
import pytest
from stream_ciphers.cipher import generate_key_stream, encrypt_decrypt

def test_generate_key_stream():
    key_stream = generate_key_stream(16)
    assert len(key_stream) == 16

def test_encrypt_decrypt():
    plaintext = b"HelloWorld123456"
    key_stream = generate_key_stream(len(plaintext))  # Ensure key_stream is defined
    ciphertext = encrypt_decrypt(plaintext, key_stream)
    decrypted = encrypt_decrypt(ciphertext, key_stream)
    assert decrypted == plaintext
