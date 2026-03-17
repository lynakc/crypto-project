def get_key():

  shift = int(input("Nombre de positions : "))
  direction = input("Direction (droite/gauche) : ")

  return (shift, direction)


def encrypt(message, key):

  shift, direction = key

  if direction == "gauche":
    shift = -shift

  result = ""

  for c in message:

    if c.isalpha(): #verifier si le caractere est une lettre

      base = ord('A') if c.isupper() else ord('a') #ord code ASCII d'un caractere

      result += chr((ord(c) - base + shift) % 26 + base) #quitter le code ASCII appliquer le decalage, revenir au code ASCII

    else:
      result += c

  return result


def decrypt(message, key):

  shift, direction = key

  if direction == "droite":
    shift = -shift
  else:
    shift = shift

  return encrypt(message, (shift, "droite"))