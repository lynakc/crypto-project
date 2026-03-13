# Cryptography Algorithms Project

## Overview

This project implements several cryptographic algorithms in Python as part of a coursework project.

The goal is to implement both **classical and modern cryptographic algorithms**, organized into two categories:

* Symmetric cryptography
* Asymmetric cryptography

The project is built using **Python** and organized in a modular structure so that each algorithm is implemented in a separate file.

---

# Project Structure

```
crypto-project/
│
├── main.py
│
├── sym/
│   ├── cesar.py
│   ├── vigenere.py
│   ├── affine.py
│   ├── hill.py
│   ├── playfair.py
│   ├── otp.py
│   ├── substitution.py
│   ├── rc4.py
│   ├── des.py
│   ├── aes.py
│   ├── feistel.py
│   ├── twofish.py
│   ├── serpent.py
│   ├── rc6.py
│   └── mars.py
│
└── asym/
    ├── rsa.py
    ├── elgamal.py
    └── diffie_hellman.py
```

* `main.py` : main interface and menu
* `sym/` : symmetric cryptography algorithms
* `asym/` : asymmetric cryptography algorithms

Each algorithm is implemented in its own file.

---

# Implemented Algorithms

## Symmetric Cryptography

* Caesar Cipher
* Vigenere Cipher
* Affine Cipher
* Playfair Cipher
* Hill Cipher
* One-Time Pad
* Random Substitution Cipher
* RC4
* DES
* AES
* Feistel Structure
* Twofish
* Serpent
* RC6
* MARS

## Asymmetric Cryptography

(To be implemented later)

* RSA
* ElGamal
* Diffie-Hellman

---

# Algorithm Interface (IMPORTANT)

To keep the project consistent, **all algorithms must follow the same function structure**.

Each algorithm file must implement the following functions:

```python
def encrypt(message, key):
    """
    Encrypt the given message using the provided key.
    Returns the ciphertext.
    """
    pass


def decrypt(ciphertext, key):
    """
    Decrypt the given ciphertext using the provided key.
    Returns the original message.
    """
    pass
```

### Parameters

* `message` : plaintext message to encrypt
* `ciphertext` : encrypted message
* `key` : encryption key (type depends on the algorithm)

### Return Value

Each function must return a **string containing the result**.

Example usage from `main.py`:

```python
from sym import cesar

cipher = cesar.encrypt("hello", 3)
plain = cesar.decrypt(cipher, 3)
```

---

# How to Run

Run the main program:

```
python main.py
```

The program will display a menu allowing the user to:

1. Choose symmetric or asymmetric cryptography
2. Select an algorithm
3. Choose encryption or decryption
4. Enter the message and key

---


# Notes

All algorithms must:

* follow the common encrypt/decrypt interface
* avoid interactive input inside the algorithm files
* return results instead of printing them
