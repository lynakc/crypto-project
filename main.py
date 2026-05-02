import random
import hashlib

from symetric import cesar
from symetric import vigenere
from symetric import affine
from symetric import hill
from symetric import playfair
from symetric import otp
from symetric import substitution
from symetric import rc4
from symetric import des
from symetric import aes
from symetric import feistel
from symetric import twofish
from symetric import serpent
from symetric import rc6
from symetric import mars

from asymetric import diffiehellman
from asymetric import rsa
from asymetric import elgamal


# =========================
# SYMMETRIC MENU
# =========================
def symmetric_menu():

  print("\n--- Cryptographie symétrique ---")
  print("1 - Cesar")
  print("2 - Vigenere")
  print("3 - Affine")
  print("4 - Playfair")
  print("5 - Hill")
  print("6 - One Time Pad")
  print("7 - Substitution Aléatoire")
  print("8 - RC4")
  print("9 - DES")
  print("10 - AES")
  print("11 - Feistel")
  print("12 - Twofish")
  print("13 - Serpent")
  print("14 - RC6")
  print("15 - MARS")

  choice = input("Choisir un algorithme: ")

  algo_map = {
    "1": cesar,
    "2": vigenere,
    "3": affine,
    "4": playfair,
    "5": hill,
    "6": otp,
    "7": substitution,
    "8": rc4,
    "9": des,
    "10": aes,
    "11": feistel,
    "12": twofish,
    "13": serpent,
    "14": rc6,
    "15": mars
  }

  if choice not in algo_map:
    print("Choix invalide")
    return

  algo = algo_map[choice]

  message = input("Message: ")
  key = algo.get_key()

  method = input("1- Chiffrement | 2- Déchiffrement: ")

  if method == "1":
    result = algo.encrypt(message, key)
  elif method == "2":
    result = algo.decrypt(message, key)
  else:
    print("Choix invalide")
    return

  print("Résultat:", result)


# =========================
# ASYMMETRIC MENU
# =========================
def asymmetric_menu():

  print("\n--- Cryptographie asymétrique ---")
  print("1 - Diffie-Hellman")
  print("2 - RSA")
  print("3 - Elgamal")

  choice = input("Choisir un algorithme: ")

  if choice == "1":
    key = diffiehellman.get_key()
    print("Clé finale Diffie-Hellman:", key)
    return

  elif choice == "2":
    algo = rsa
  elif choice == "3":
    algo = elgamal
  else:
    print("Choix invalide")
    return

  message = input("Message: ")
  key = algo.get_key()

  method = input("1- Chiffrement | 2- Déchiffrement: ")

  if method == "1":
    result = algo.encrypt(message, key)
  elif method == "2":
    result = algo.decrypt(message, key)
  else:
    print("Choix invalide")
    return

  print("Résultat:", result)


# =========================
# HASH MENU (NEW)
# =========================
def hash_menu():

  print("\n--- Fonctions de hachage ---")
  print("1 - SHA-256")
  print("2 - MD5")

  choice = input("Choisir: ")
  message = input("Message: ")

  

  message_final = message.strip().replace('\n', '').replace('\r', '')

# SHA-256
  if choice == "1":

# Vérification binaire pour être sûr de ce qu'on envoie à l'algo
    data_to_hash = message_final.encode()

    h = hashlib.sha256(data_to_hash).hexdigest()
    print(f"Hash SHA-256 : {h}")

# MD5
  elif choice == "2":
    h = hashlib.md5(message_final.encode()).hexdigest()
    print("Hash MD5:", h)

  else:
    print("Choix invalide")


# =========================
# MAIN LOOP
# =========================
def main():

  while True:

    print("\n===== Type de Cryptographie =====")
    print("1 - Cryptographie symétrique")
    print("2 - Cryptographie asymétrique")
    print("3 - Fonctions de hachage")
    print("0 - Exit")

    choice = input("Choix: ")

    if choice == "1":
      symmetric_menu()

    elif choice == "2":
      asymmetric_menu()

    elif choice == "3":
      hash_menu()

    elif choice == "0":
      print("Au revoir")
      break

    else:
      print("Choix invalide")


if __name__ == "__main__":
  main()