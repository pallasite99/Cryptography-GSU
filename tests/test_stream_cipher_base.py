import pytest
from stream_cipher.cipher import generate_key_stream, encrypt_decrypt

def test_generate_key_stream_length():
    length = 16
    key_stream = generate_key_stream(length)
    assert len(key_stream) == length, "Key stream length mismatch"

def test_encrypt_decrypt():
    plaintext = b"Hello, Stream Cipher!"
    key_stream = generate_key_stream(len(plaintext))
    ciphertext = encrypt_decrypt(plaintext, key_stream)
    decrypted_text = encrypt_decrypt(ciphertext, key_stream)
    assert decrypted_text == plaintext, "Decrypted text does not match plaintext"
