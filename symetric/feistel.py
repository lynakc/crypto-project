def get_key():
    while True:
        key_string = input("Entrer la clé: ")
        if key_string:
            break
        print("La clé ne peut pas être vide")

    while True:
        try:
            rounds = int(input("Entrer le nombre de rounds (recommandé 6-16): "))
            if rounds > 0:
                break
            else:
                print("Le nombre de rounds doit être > 0")
        except:
            print("Entrer un nombre valide")

    return {"key": key_string, "rounds": rounds}


# ── Helpers ──
def to_hex(text):
    return text.encode("latin1").hex()

def from_hex(hex_text):
    return bytes.fromhex(hex_text).decode("latin1")

def xor_strings(a, b):
    
    return "".join(chr(ord(a[i]) ^ ord(b[i % len(b)])) for i in range(len(a)))

def split_message(message):
    mid = len(message) // 2
    return message[:mid], message[mid:]


# ── Subkey generation ────
def generate_subkeys(key, rounds):
    key_bytes = [ord(c) for c in key]
    subkeys = []
    for i in range(rounds):
        rotated = key_bytes[i % len(key_bytes):] + key_bytes[:i % len(key_bytes)]
        mixed   = [(val + i) % 256 for val in rotated]
        subkeys.append("".join(chr(v) for v in mixed))
    return subkeys


# ── Feistel round function ──
def F(right, key):
    key = (key * (len(right) // len(key) + 1))[:len(right)]
    return xor_strings(right, key)

def feistel_round(left, right, key):
    return right, xor_strings(left, F(right, key))


# ── Public API ───
def encrypt(message, key):
    
    key_string = key["key"]
    rounds     = key["rounds"]

    if len(message) % 2 != 0:
        message += "\x00"                        

    left, right = split_message(message)
    subkeys     = generate_subkeys(key_string, rounds)

    for i in range(rounds):
        left, right = feistel_round(left, right, subkeys[i])

    return to_hex(left + right)


def decrypt(ciphertext, key):
 
    key_string = key["key"]
    rounds     = key["rounds"]

    ciphertext  = from_hex(ciphertext)
    left, right = split_message(ciphertext)
    subkeys     = generate_subkeys(key_string, rounds)

    for i in reversed(range(rounds)):
        new_right = left
        new_left  = xor_strings(right, F(left, subkeys[i]))
        left, right = new_left, new_right

    return (left + right).rstrip("\x00")         