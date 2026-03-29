def get_key():
  print("Entrer les 4 valeur de la matrice clé (2*2): ")
  a = int(input("a="))
  b = int(input("b="))
  c = int(input("c="))
  d = int(input("d="))

  return [[a,b], [c,d]]

def mod_inverse(a, m):
  for x in range(1, m):
    if (a * x) % m == 1:
      return x
  return None

def matrix_inverse(matrix):
  a, b = matrix[0]
  c, d = matrix[1]

  det = (a * d - b * c) % 26

  inv_det = mod_inverse(det, 26)

  if inv_det is None:
    print("Matrice non inversible")
    return None

  return [
    [(d * inv_det) % 26, (-b * inv_det) % 26],
    [(-c * inv_det) % 26, (a * inv_det) % 26]
  ]

def process(message, matrix):

  #rendre tout les caracteres majuscule et enlever les espaces
  message = message.upper().replace(" ", "") #ou message = message.low().replace(" ", "")

  # ajouter X si longueur impaire
  if len(message) % 2 != 0:
    message += "X" #ou message += "x"

  result = ""

  for i in range(0, len(message), 2):

    x = ord(message[i]) - ord('A') #ou ord("a")
    y = ord(message[i+1]) - ord('A')

    # multiplication matrice
    r1 = (matrix[0][0]*x + matrix[0][1]*y) % 26
    r2 = (matrix[1][0]*x + matrix[1][1]*y) % 26

    result += chr(r1 + ord('A')) #ou ord("a")
    result += chr(r2 + ord('A'))

  return result


def encrypt(message, key):
  return process(message, key)


def decrypt(message, key):
  inv_matrix = matrix_inverse(key)
  if inv_matrix is None:
    return None
  return process(message, inv_matrix)