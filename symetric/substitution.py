import string
import random

ALPHABET = string.ascii_uppercase

def get_key():
    while True:
        key = input("Entrer la clé (26 lettres A-Z sans répétition): ").upper()

        if len(key) != 26:
            print(" La clé doit contenir exactement 26 lettres.")
            continue

        if set(key) != set(ALPHABET):
            print(" La clé doit contenir chaque lettre A-Z une seule fois.")
            continue

        return key

def create_maps(key):
    encrypt_map = {}
    decrypt_map = {}

    for i in range(len(ALPHABET)):
        plain_char = ALPHABET[i]
        cipher_char = key[i]

        encrypt_map[plain_char] = cipher_char
        decrypt_map[cipher_char] = plain_char

    return encrypt_map, decrypt_map


def encrypt(message, key):
    message = message.upper()
    encrypt_map, _ = create_maps(key)

    result = ""

    for char in message:
        if char in ALPHABET:
            result += encrypt_map[char]
        else:
            result += char

    return result


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    _, decrypt_map = create_maps(key)

    result = ""

    for char in ciphertext:
        if char in ALPHABET:
            result += decrypt_map[char]
        else:
            result += char

    return result