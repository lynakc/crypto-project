def get_key():
  key = input("Entrer la clé: ")
  return key

#generation de la permutation
def KSA(key):
  key = [ord(c) for c in key] #transforme la cle en une liste de nombre (le code ACII de chaque caractere)
  s = list(range(256)) #une liste de 0 a 255
  j = 0

  for i in range(256):
    j = (j+s[i]+key[i%len(key)])%256
    s[i], s[j] = s[j], s[i] #permutation

  return s

#generation du flot pseudo-aleatoire
def PRGA(s, n):
  i = 0
  j = 0
  keystream = []

  for _ in range(n) :
    i = (i+1)%256
    j = (j+s[i])%256

    s[i], s[j] = s[j], s[i]
    k = s[(s[i]+s[j])%256]
    keystream.append(k)

  return keystream

def encrypt(message, key):
  s = KSA(key)
  keystream = PRGA(s, len(message))
  result = ""

  for i in range(len(message)):
    result += format(ord(message[i]) ^ keystream[i], '02x')

  return result


def decrypt(message, key):
  s = KSA(key)
  keystream = PRGA(s, len(message)//2)

  bytes_data = bytes.fromhex(message)

  result = ""

  for i in range(len(bytes_data)):
    result += chr(bytes_data[i] ^ keystream[i])
  
  return result