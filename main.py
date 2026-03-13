from symetric import cesar
from symetric import vigenere
from symetric import affine
from symetric import hill
from symetric import playfair
from symetric import otp #one time pad
from symetric import substitution
from symetric import rc4
from symetric import des
from symetric import aes
from symetric import feistel
from symetric import twofish
from symetric import serpent
from symetric import rc6
from symetric import mars


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

  message = input("Message: ")
  key = input("Clé: ")
  method = input("1 Chiffrement / 2 Déchiffrement: ")

  if choice == "1":
      algo = cesar
  elif choice == "2":
      algo = vigenere
  elif choice == "3":
      algo = affine
  elif choice == "4":
      algo = playfair
  elif choice == "5":
      algo = hill
  elif choice == "6":
      algo = otp
  elif choice == "7":
      algo = substitution
  elif choice == "8":
      algo = rc4
  elif choice == "9":
      algo = des
  elif choice == "10":
      algo = aes
  elif choice == "11":
      algo = feistel
  elif choice == "12":
      algo = twofish
  elif choice == "13":
      algo = serpent
  elif choice == "14":
      algo = rc6
  elif choice == "15":
      algo = mars
  else:
    print("Choix invalide")
    return

  if method == "1":
    result = algo.encrypt(message, key)
  else:
    result = algo.decrypt(message, key)

  print("Result:", result)


def main():

  while True:

    print("\n===== Type Cryptographie =====")
    print("1 - Cryptographie symétrique")
    print("2 - Cryptographie asymétrique")
    print("0 - Exit")

    choice = input("Choix: ")

    if choice == "1":
      symmetric_menu()

    elif choice == "2":
      print("asymmetric_menu()") #apres on enleve print

    elif choice == "0":
      print("Au revoir")
      break

    else:
      print("Choix invalide")


if __name__ == "__main__":
  main()