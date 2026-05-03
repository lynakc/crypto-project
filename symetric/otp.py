import random

def get_key():
    choix = input("1- Entrer clé manuelle (Texte) | 2- Générer clé aléatoire: ")
    if choix == "1":
    
        cle_texte = input("Entrer la clé: ").upper().replace(" ", "")
        return [ord(c) - ord('A') for c in cle_texte]
    else:
        n = int(input("Longueur de la clé à générer: "))
        key = [random.randint(0, 25) for _ in range(n)]
        print("Clé générée (nombres):", key)
        return key

def process(message, key, mode):
    typec = input("1- Message en majuscule | 2- Message en minuscule: ")

    if typec == "1":
        message = message.upper().replace(" ", "")
        base = ord('A')
    elif typec == "2":
        message = message.lower().replace(" ", "")
        base = ord('a')
    else:
        return None

    result = ""
    for i, c in enumerate(message):
        if i >= len(key): 
            break
        
        x = ord(c) - base
        
        if mode == "encrypt":
            val = (x + key[i]) % 26
        else:
            val = (x - key[i]) % 26
            
        result += chr(val + base)
    return result

def encrypt(message, key):
    return process(message, key, "encrypt")

def decrypt(message, key):
    return process(message, key, "decrypt")