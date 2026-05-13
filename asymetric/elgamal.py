from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
from Crypto.Util.number import bytes_to_long, long_to_bytes
import random
import json
import os

KEY_FILE = "elgamal_key.json"


def get_key():
   
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as f:
            data = json.load(f)
        p = int(data["p"])
        g = int(data["g"])
        y = int(data["y"])
        x = int(data["x"])
        # reconstruct full key and public key
        private_key = ElGamal.construct((p, g, y, x))
        public_key  = ElGamal.construct((p, g, y))
    else:
        print("Génération d'une clé ElGamal 256-bit, veuillez patienter...")
        private_key = ElGamal.generate(256, get_random_bytes)
        public_key  = private_key.publickey()
        with open(KEY_FILE, "w") as f:
            json.dump({
                "p": str(private_key.p),
                "g": str(private_key.g),
                "y": str(private_key.y),
                "x": str(private_key.x),
            }, f)

    return public_key, private_key


def encrypt(message, keys):
   
    public_key, private_key = keys
    p = int(public_key.p)
    g = int(public_key.g)
    y = int(public_key.y)

    data       = message.encode("utf-8")
    chunk_size = (p.bit_length() // 8) - 1
    pairs      = []

    for i in range(0, len(data), chunk_size):
        block = data[i:i + chunk_size]
        m     = bytes_to_long(b"\x01" + block)
        k     = random.randrange(2, p - 2)
        c1    = pow(g, k, p)
        c2    = (m * pow(y, k, p)) % p
        pairs.append(f"{c1},{c2}")

    return ";".join(pairs)


def decrypt(ciphertext, keys):
    
    public_key, private_key = keys
    p = int(private_key.p)
    x = int(private_key.x)

    result = b""
    for pair in ciphertext.split(";"):
        c1, c2  = pair.split(",")
        c1, c2  = int(c1), int(c2)
        s       = pow(c1, x, p)
        s_inv   = pow(s, p - 2, p)
        m       = (c2 * s_inv) % p
        block   = long_to_bytes(m)
        result += block[1:]

    return result.decode("utf-8")


