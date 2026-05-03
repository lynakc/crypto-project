from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def get_key():
  try:
    with open("private.pem", "rb") as f:
      private_key = RSA.import_key(f.read())
  except:
    key = RSA.generate(1024)
    private_key = key
    with open("private.pem", "wb") as f:
      f.write(private_key.export_key())

  public_key = private_key.publickey()
  return public_key, private_key


def encrypt(message, keys):
  public_key, private_key = keys

  cipher = PKCS1_OAEP.new(public_key)
  ciphertext = cipher.encrypt(message.encode())

  return ciphertext.hex()


def decrypt(ciphertext, keys):
  public_key, private_key = keys

  cipher = PKCS1_OAEP.new(private_key)
  decrypted = cipher.decrypt(bytes.fromhex(ciphertext))

  return decrypted.decode()