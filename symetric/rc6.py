
import struct

# ── RC6 constants ──
W = 32          
R = 20          
MOD = 2**W   

P32 = 0xB7E15163   
Q32 = 0x9E3779B9   


# ── Rotation helpers ───
def rotl(x, n):
    n &= 31
    return ((x << n) | (x >> (W - n))) & 0xFFFFFFFF

def rotr(x, n):
    n &= 31
    return ((x >> n) | (x << (W - n))) & 0xFFFFFFFF


# ── Key schedule ──
def key_schedule(key):
    key_bytes = [ord(c) for c in key]

    while len(key_bytes) % 4 != 0:
        key_bytes.append(0)

    u = W // 8                          
    c = len(key_bytes) // u           
    L = [0] * c
    for i in range(len(key_bytes) - 1, -1, -1):
        L[i // u] = (L[i // u] << 8) | key_bytes[i]

    t = 2 * R + 4                      
    S = [0] * t
    S[0] = P32
    for i in range(1, t):
        S[i] = (S[i-1] + Q32) & 0xFFFFFFFF

    A = B = i = j = 0
    v = 3 * max(c, t)
    for _ in range(v):
        A = S[i] = rotl((S[i] + A + B) & 0xFFFFFFFF, 3)
        B = L[j] = rotl((L[j] + A + B) & 0xFFFFFFFF, (A + B) & 31)
        i = (i + 1) % t
        j = (j + 1) % c

    return S


# ── PKCS7 padding ───
def pad(data):
    pl = 16 - (len(data) % 16)
    return data + bytes([pl] * pl)

def unpad(data):
    return data[:-data[-1]]


# ── Single block encrypt / decrypt ───
def encrypt_block(block, S):
    A, B, C, D = struct.unpack('<4I', block)
    B = (B + S[0]) & 0xFFFFFFFF
    D = (D + S[1]) & 0xFFFFFFFF
    for i in range(1, R + 1):
        t = rotl((B * (2*B + 1)) & 0xFFFFFFFF, 5)
        u = rotl((D * (2*D + 1)) & 0xFFFFFFFF, 5)
        A = (rotl(A ^ t, u & 31) + S[2*i])   & 0xFFFFFFFF
        C = (rotl(C ^ u, t & 31) + S[2*i+1]) & 0xFFFFFFFF
        A, B, C, D = B, C, D, A
    A = (A + S[2*R+2]) & 0xFFFFFFFF
    C = (C + S[2*R+3]) & 0xFFFFFFFF
    return struct.pack('<4I', A, B, C, D)

def decrypt_block(block, S):
    A, B, C, D = struct.unpack('<4I', block)
    C = (C - S[2*R+3]) & 0xFFFFFFFF
    A = (A - S[2*R+2]) & 0xFFFFFFFF
    for i in range(R, 0, -1):
        A, B, C, D = D, A, B, C
        u = rotl((D * (2*D + 1)) & 0xFFFFFFFF, 5)
        t = rotl((B * (2*B + 1)) & 0xFFFFFFFF, 5)
        C = (rotr((C - S[2*i+1]) & 0xFFFFFFFF, t & 31) ^ u) & 0xFFFFFFFF
        A = (rotr((A - S[2*i])   & 0xFFFFFFFF, u & 31) ^ t) & 0xFFFFFFFF
    D = (D - S[1]) & 0xFFFFFFFF
    B = (B - S[0]) & 0xFFFFFFFF
    return struct.pack('<4I', A, B, C, D)


# ── Key input ───
def get_key():
    key = input("Entrer la clé: ")
    return key


# ── Public API ──
def encrypt(message, key):
    S    = key_schedule(key)
    data = pad(message.encode("utf-8"))
    out  = b""
    for i in range(0, len(data), 16):
        out += encrypt_block(data[i:i+16], S)
    return out.hex()

def decrypt(message, key):
    S    = key_schedule(key)
    data = bytes.fromhex(message)
    out  = b""
    for i in range(0, len(data), 16):
        out += decrypt_block(data[i:i+16], S)
    return unpad(out).decode("utf-8")


