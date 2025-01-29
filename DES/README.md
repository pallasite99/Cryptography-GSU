# Data Encryption Standard (DES)

## Overview
The **Data Encryption Standard (DES)** is a symmetric-key block cipher developed by IBM and adopted by the U.S. government in 1977. It encrypts data in 64-bit blocks using a 56-bit key, following a **Feistel network** structure with 16 rounds of processing.

## Features
- **Symmetric Key Encryption**: Same key for encryption and decryption.
- **Block Cipher**: Encrypts data in fixed-size blocks of 64 bits.
- **Feistel Structure**: Uses permutation and substitution functions.
- **16 Rounds**: Applies key-dependent transformations iteratively.

## Installation
To run DES encryption/decryption in Python, install the required package:

```sh
pip install pycryptodome
```

```sh
pip install pycryptodomex
```

## Usage
### Encrypting Data
```python
from Crypto.Cipher import DES
import binascii

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

key = b'8bytekey'  # Must be exactly 8 bytes
cipher = DES.new(key, DES.MODE_ECB)
plaintext = pad("Hello123")
ciphertext = cipher.encrypt(plaintext.encode())

print("Ciphertext:", binascii.hexlify(ciphertext))
```

### Decrypting Data
```python
decrypted_text = cipher.decrypt(ciphertext).decode().strip()
print("Decrypted:", decrypted_text)
```

## Security Concerns
- DES is vulnerable to **brute-force attacks** due to its small key size.
- **Triple DES (3DES)** improves security by applying DES three times.
- **AES** is recommended for modern encryption needs.

## References
- [NIST DES Specification](https://csrc.nist.gov/publications/fips/fips46-3/fips46-3.pdf)
- [Wikipedia - Data Encryption Standard](https://en.wikipedia.org/wiki/Data_Encryption_Standard)

## License
This project is licensed under the MIT License.
