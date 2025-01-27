import pytest
from StreamCiphers.cipher import generate_key_stream, encrypt_decrypt


def test_generate_key_stream_length():
    """Test if the generated key stream has the correct length."""
    length = 16
    key_stream = generate_key_stream(length)
    assert len(key_stream) == length, "Key stream length does not match the expected length."


def test_encrypt_decrypt():
    """Test if encryption and decryption work correctly."""
    plaintext = b"Hello, Stream Cipher!"
    key_stream = generate_key_stream(len(plaintext))
    ciphertext = encrypt_decrypt(plaintext, key_stream)
    decrypted_text = encrypt_decrypt(ciphertext, key_stream)
    assert decrypted_text == plaintext, "Decrypted text does not match the original plaintext."


def test_encrypt_with_different_key_streams():
    """Test if encrypting with different key streams produces different results."""
    plaintext = b"Test message"
    key_stream1 = generate_key_stream(len(plaintext))
    key_stream2 = generate_key_stream(len(plaintext))
    ciphertext1 = encrypt_decrypt(plaintext, key_stream1)
    ciphertext2 = encrypt_decrypt(plaintext, key_stream2)
    assert ciphertext1 != ciphertext2, "Ciphertexts should differ with different key streams."


def test_invalid_key_stream_length():
    """Test if the function raises an error when key stream length is invalid."""
    plaintext = b"Hello, World!"
    invalid_key_stream = generate_key_stream(len(plaintext) - 1)  # Key stream is too short
    with pytest.raises(ValueError):
        encrypt_decrypt(plaintext, invalid_key_stream)


def test_empty_plaintext():
    """Test if encrypting and decrypting an empty plaintext works."""
    plaintext = b""
    key_stream = generate_key_stream(len(plaintext))
    ciphertext = encrypt_decrypt(plaintext, key_stream)
    decrypted_text = encrypt_decrypt(ciphertext, key_stream)
    assert decrypted_text == plaintext, "Empty plaintext decryption failed."

