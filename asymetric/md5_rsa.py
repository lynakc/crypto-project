import hashlib
from Crypto.PublicKey import RSA


# ----------- GENERATION DES CLES -----------

def get_key():
    try:
        with open("private.pem", "rb") as f:
            private_key = RSA.import_key(f.read())
    except:
        key = RSA.generate(1024)
        private_key = key
        with open("private.pem", "wb") as f:
            f.write(private_key.export_key())

    public_key = private_key.publickey()
    return public_key, private_key


# ----------- SIGNATURE -----------

def encrypt(message, keys):
    public_key, private_key = keys

    # 1. hash du message
    hash_msg = hashlib.md5(message.encode()).digest()

    # 2. signature avec clé privée
    signature = pow(int.from_bytes(hash_msg, 'big'),
                    private_key.d,
                    private_key.n)

    return hex(signature)


# ----------- VERIFICATION -----------

def decrypt(signature_hex, keys):
    public_key, private_key = keys

    message = input("Entrer le message original pour vérification: ")

    # 1. hash du message
    hash_msg = hashlib.md5(message.encode()).digest()

    # 2. récupération signature
    signature_int = int(signature_hex, 16)

    # 3. "déchiffrement" avec clé publique
    decrypted_hash = pow(signature_int,
                         public_key.e,
                         public_key.n)

    decrypted_hash_bytes = decrypted_hash.to_bytes(16, 'big')

    # 4. comparaison
    if decrypted_hash_bytes == hash_msg:
        return "✅ Signature valide"
    else:
        return "❌ Signature invalide"