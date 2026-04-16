import random

def is_prime(n):
  if n < 3:
    return False
  for i in range(2, int(n**0.5) + 1): #verifier de 2 a racine de n
    if n % i == 0:
      return False
  return True

def pgcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def get_key():
  print("=== Génération des clés RSA ===")

  while True:
    p = int(input("Entrer un nombre premier p: "))
    if is_prime(p):
      break
    print("p n'est pas premier, veuiller réessayer")

  while True:
    q = int(input("Entrer un nombre premier q: "))
    if is_prime(q):
      break
    print("q n'est pas premier, veuiller réessayer")

  n = p * q
  phi = (p - 1) * (q - 1)

  while True:
    e = int(input("Entrer e (premier avec phi): "))
    if pgcd(e, phi) == 1:
      break
    print("e n'est pas premier avec phi(n), veuiller réessayer")
  # calcul de d (inverse modulaire)
  d = mod_inverse(e, phi)

  del p
  del q

  #print("Clé publique (e, n):", (e, n))
  #print("Clé privée (d, n):", (d, n))

  return (e, d, n)

def mod_inverse(e, phi):
  def extended_pgcd(a, b):
    if a==0:
      return b, 0, 1
    pgcd, x1, y1 = extended_pgcd(b%a, a)
    x = y1 - (b//a)*x1
    y = x1
    return pgcd, x, y
  
  pgcd_val, x, y = extended_pgcd(e, phi)
  if pgcd_val != 1:
    return None
  
  return x%phi

def encrypt(message, key):
  e, d, n = key

  result = []
  for char in message: #boucle pour chaque caractere du message
    c = pow(ord(char), e, n) #calculer x^e mod n
    result.append(str(c))

  return " ".join(result)
  #return pow(int(message),e,n)

def decrypt(message, key):
  e, d, n = key

  result = ""
  numbers = message.split() #decouper la liste

  for num in numbers:
    m = pow(int(num), d, n)
    result += chr(m)
  
  return result
  #return pow(int(message),d,n)