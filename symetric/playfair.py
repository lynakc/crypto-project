import string



def get_key():
    return input("Entrer la clé: ")



def generate_matrix(key):
    key = key.upper().replace("J", "I")

    seen = set()
    matrix = []

    
    for c in key:
        if c.isalpha() and c not in seen:
            seen.add(c)
            matrix.append(c)

    
    for c in string.ascii_uppercase:
        if c == "J":
            continue
        if c not in seen:
            seen.add(c)
            matrix.append(c)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_pos(matrix, c):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return i, j



def prepare(message):
    message = message.upper().replace("J", "I").replace(" ", "")

    pairs = []
    i = 0

    while i < len(message):
        a = message[i]

        if i + 1 < len(message):
            b = message[i + 1]
        else:
            b = "X"

        if a == b:
            pairs.append((a, "X"))
            i += 1
        else:
            pairs.append((a, b))
            i += 2

    return pairs



def process(message, matrix, mode):

    
    message = message.upper().replace(" ", "")

    pairs = prepare(message)
    result = ""

    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        
        if r1 == r2:
            if mode == "encrypt":
                result += matrix[r1][(c1 + 1) % 5]
                result += matrix[r2][(c2 + 1) % 5]
            else:
                result += matrix[r1][(c1 - 1) % 5]
                result += matrix[r2][(c2 - 1) % 5]

        
        elif c1 == c2:
            if mode == "encrypt":
                result += matrix[(r1 + 1) % 5][c1]
                result += matrix[(r2 + 1) % 5][c2]
            else:
                result += matrix[(r1 - 1) % 5][c1]
                result += matrix[(r2 - 1) % 5][c2]

        
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result



def encrypt(message, key):
    matrix = generate_matrix(key)
    return process(message, matrix, "encrypt")


def decrypt(message, key):
    matrix = generate_matrix(key)
    return process(message, matrix, "decrypt")