import string

def get_key():
  return input("Entrer la clé: ")

def generate_matrix(key):
  key = key.upper().replace("J", "I")
  seen = set()
  matrix = []

  for c in key + string.ascii_uppercase:
    if c not in seen and c != "J":
      seen.add(c)
      matrix.append(c)

  return [matrix[i:i+5] for i in range(0,25,5)]

def find_pos(matrix, c):
  for i in range(5):
    for j in range(5):
      if matrix[i][j] == c:
        return i, j

def prepare(message):
  message = message.upper().replace("J","I").replace(" ","")
  pairs = []
  i = 0

  while i < len(message):
    a = message[i]
    b = message[i+1] if i+1 < len(message) else "X"

    if a == b:
      pairs.append((a,"X"))
      i += 1
    else:
      pairs.append((a,b))
      i += 2

  return pairs

def process(message, matrix, mode):

  typec = input("1- Message en majuscule | 2- Message en minuscule: ")

  if typec == "1":
    message = message.upper().replace(" ", "")
  elif typec == "2":
    message = message.lower().replace(" ", "")
  else:
    print("Choix invalide")
    return None

  pairs = prepare(message)
  result = ""

  for a,b in pairs:
    r1,c1 = find_pos(matrix,a)
    r2,c2 = find_pos(matrix,b)

    if r1 == r2:
      if mode == "encrypt":
        result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
      else:
        result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]

    elif c1 == c2:
      if mode == "encrypt":
        result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
      else:
        result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]

    else:
      result += matrix[r1][c2] + matrix[r2][c1]

  return result


def encrypt(message, key):
  matrix = generate_matrix(key)
  return process(message, matrix, "encrypt")

def decrypt(message, key):
  matrix = generate_matrix(key)
  return process(message, matrix, "decrypt")