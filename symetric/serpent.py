def get_key():
    # Permet d'entrer une clé textuelle sans espaces
    cle_texte = input("Entrer la clé Serpent: ").upper().replace(" ", "")
    # Convertit les lettres en liste de nombres (A=0, B=1...)
    return [ord(c) - ord('A') for c in cle_texte]

def process(message, key, mode):
    # S-Box (Table de substitution) pour l'effet Serpent
    sbox = [3, 8, 15, 1, 10, 6, 5, 11, 14, 13, 4, 0, 2, 7, 12, 9, 20, 18, 16, 17, 19, 22, 21, 23, 25, 24]
    inv_sbox = [sbox.index(i) for i in range(26)]
    
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
    # Sécurité si la clé est vide
    if not key: key = [0]

    for i, c in enumerate(message):
        x = ord(c) - base
        # On récupère le décalage de la clé (en boucle)
        shift = key[i % len(key)]
        
        if mode == "encrypt":
            # On applique le décalage de la clé PUIS la substitution S-Box
            val = sbox[(x + shift) % 26]
        else:
            # On fait l'inverse : substitution inverse PUIS on retire le décalage
            val = (inv_sbox[x] - shift) % 26
            
        result += chr(val + base)
    return result

def encrypt(message, key):
    return process(message, key, "encrypt")

def decrypt(message, key):
    return process(message, key, "decrypt")