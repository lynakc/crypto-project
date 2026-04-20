import random

def get_key():
    # On récupère une chaîne de caractères (ex: "MA_CLE")
    cle_texte = input("Entrer la clé (ex: SECRET): ").upper().replace(" ", "")
    # On la transforme en liste de nombres pour le calcul
    return [ord(c) - ord('A') for c in cle_texte]

def process(message, key, mode):
    typec = input("1- Message en majuscule | 2- Message en minuscule: ")
    if typec == "1":
        message = message.upper().replace(" ", "")
        base = ord('A')
    elif typec == "2":
        message = message.lower().replace(" ", "")
        base = ord('a')
    else: return None

    result = ""
    # Si la clé est vide pour éviter une division par zéro
    if not key: key = [0]

    for i, c in enumerate(message):
        x = ord(c) - base
        # On utilise le modulo sur la longueur de la clé pour boucler (style Vigenere/DES)
        shift = key[i % len(key)]
        
        if mode == "encrypt":
            val = (x + shift) % 26
        else:
            val = (x - shift) % 26
        result += chr(val + base)
    return result

def encrypt(message, key):
    return process(message, key, "encrypt")

def decrypt(message, key):
    return process(message, key, "decrypt")