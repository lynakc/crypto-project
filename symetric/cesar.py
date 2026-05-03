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

    if c.isalpha(): 

      base = ord('A') if c.isupper() else ord('a')

      result += chr((ord(c) - base + shift) % 26 + base) 

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