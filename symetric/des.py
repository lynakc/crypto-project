import random

def get_key():
  
    cle_texte = input("Entrer la clé (ex: SECRET): ").upper().replace(" ", "")
    
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
    
    if not key: key = [0]

    for i, c in enumerate(message):
        x = ord(c) - base
       
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