import hashlib

def get_key():
  return None  # pas de clé pour un hash


def encrypt(message, key=None):
  hash_object = hashlib.md5(message.encode())
  return hash_object.hexdigest()


def decrypt(message, key=None):
  return "❌ Impossible de déchiffrer un hash"