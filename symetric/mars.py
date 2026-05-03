def get_key():
  return input("Entrer la clé : ")

def simple_hash(key):
  return [ord(c) % 256 for c in key]

def F(x, k):
  
  return ((x ^ k) + ((x << 1) & 0xFFFFFFFF)) % (2**32)

def process_block(L, R, subkeys):
  for k in subkeys:
    L, R = R, L ^ F(R, k)
  return R, L

def encrypt(message, key):
  subkeys = simple_hash(key)

  
  while len(message) % 8 != 0:
    message += " "

  result = ""

  for i in range(0, len(message), 8):
    block = message[i:i+8]

    L = int.from_bytes(block[:4].encode(), 'big')
    R = int.from_bytes(block[4:].encode(), 'big')

    L, R = process_block(L, R, subkeys)

    result += (L.to_bytes(4, 'big') + R.to_bytes(4, 'big')).hex()

  return result

def decrypt(message, key):
  subkeys = simple_hash(key)[::-1]  

  result = ""

  for i in range(0, len(message), 16):
    block = bytes.fromhex(message[i:i+16])

    L = int.from_bytes(block[:4], 'big')
    R = int.from_bytes(block[4:], 'big')

    L, R = process_block(L, R, subkeys)

    result += (L.to_bytes(4, 'big') + R.to_bytes(4, 'big')).decode()

  return result.strip() 