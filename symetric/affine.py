def get_key():
  a = int(input("Entrer a (premier avec 26): "))
  b = int(input("Entrer b: "))
  return a, b

def mod_inverse(a, m):
  for x in range(1, m):
    if (a * x) % m == 1:
      return x
  return None

def process(message, a, b, mode):

  typec = input("1- Message en majuscule | 2- Message en minuscule: ")

  if typec == "1":
    message = message.upper().replace(" ", "")
    base = ord('A')
  elif typec == "2":
    message = message.lower().replace(" ", "")
    base = ord('a')
  else:
    print("Choix invalide")
    return None

  result = ""

  if mode == "encrypt":
    for c in message:
      x = ord(c) - base
      result += chr((a*x + b) % 26 + base)
  else:
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
      print("a non inversible")
      return None

    for c in message:
      y = ord(c) - base
      result += chr((a_inv*(y - b)) % 26 + base)

  return result


def encrypt(message, key):
  a, b = key
  return process(message, a, b, "encrypt")

def decrypt(message, key):
  a, b = key
  return process(message, a, b, "decrypt")