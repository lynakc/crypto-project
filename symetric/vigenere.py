def get_key():
  key = input("Entrer la clé (mot) : ")
  return key

def generate_key(message, key):
  key = list(key)
  key_extended = []

  j = 0
  for i in range(len(message)):
    if message[i].isalpha():
      key_extended.append(key[j % len(key)])
      j += 1
    else:
      key_extended.append(message[i])

  return "".join(key_extended)

def process(message, key, mode):

  key = generate_key(message, key)
  result = ""

  for i in range(len(message)):

    if message[i].isalpha():

      m = message[i]
      k = key[i]

      base = ord('A') if m.isupper() else ord('a')
      shift = ord(k.lower()) - ord('a')

      if mode == "encrypt":
        result += chr((ord(m) - base + shift) % 26 + base)
      else:
        result += chr((ord(m) - base - shift) % 26 + base)

    else:
      result += message[i]

  return result

def encrypt(message, key):
  return process(message, key, "encrypt")

def decrypt(message, key):
  return process(message, key, "decrypt")