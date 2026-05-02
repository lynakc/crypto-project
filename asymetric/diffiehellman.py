from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def get_key():
    print("=== Diffie-Hellman + Signature ===")

    p = int(input("Entrer un nombre premier p: "))
    g = int(input("Entrer une base g: "))

    a = int(input("Clé privée Alice: "))
    b = int(input("Clé privée Bob: "))

    # =========================
    # DIFFIE-HELLMAN
    # =========================
    A = pow(g, a, p)
    B = pow(g, b, p)

    print("A (Alice):", A)
    print("B (Bob):", B)

    # =========================
    # SIGNATURE
    # =========================
    key_alice = ECC.generate(curve='P-256')
    key_bob = ECC.generate(curve='P-256')

    signer_alice = DSS.new(key_alice, 'fips-186-3')
    signer_bob = DSS.new(key_bob, 'fips-186-3')

    # Alice signe A
    hA = SHA256.new(str(A).encode())
    sig_A = signer_alice.sign(hA)

    # Bob signe B
    hB = SHA256.new(str(B).encode())
    sig_B = signer_bob.sign(hB)

    # =========================
    # VERIFICATION
    # =========================
    verifier_alice = DSS.new(key_alice.public_key(), 'fips-186-3')
    verifier_bob = DSS.new(key_bob.public_key(), 'fips-186-3')

    try:
        verifier_alice.verify(hA, sig_A)
        print("✔ Signature A valide")
    except:
        print("❌ Signature A invalide")
        return None

    try:
        verifier_bob.verify(hB, sig_B)
        print("✔ Signature B valide")
    except:
        print("❌ Signature B invalide")
        return None

    # =========================
    # CLE PARTAGEE
    # =========================
    K_alice = pow(B, a, p)
    K_bob = pow(A, b, p)

    print("Clé Alice:", K_alice)
    print("Clé Bob:", K_bob)

    if K_alice != K_bob:
        print("❌ Erreur")
        return None

    print("✔ Clé sécurisée (authentifiée)")
    return K_alice