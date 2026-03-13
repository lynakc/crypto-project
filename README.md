# Projet d'Algorithmes de Cryptographie

## Présentation

Ce projet consiste à implémenter plusieurs algorithmes de cryptographie en Python.

L’objectif est d’implémenter des **algorithmes de cryptographie classiques et modernes**, organisés en deux catégories principales :

* Cryptographie symétrique
* Cryptographie asymétrique

Le projet est structuré de manière modulaire afin que **chaque algorithme soit implémenté dans un fichier séparé**.

---

# Structure du projet

```text
crypto-project/
│
├── main.py
│
├── sym/
│   ├── cesar.py
│   ├── vigenere.py
│   ├── affine.py
│   ├── hill.py
│   ├── playfair.py
│   ├── otp.py
│   ├── substitution.py
│   ├── rc4.py
│   ├── des.py
│   ├── aes.py
│   ├── feistel.py
│   ├── twofish.py
│   ├── serpent.py
│   ├── rc6.py
│   └── mars.py
│
└── asym/
    ├── rsa.py
    ├── elgamal.py
    └── diffie_hellman.py
```

* `main.py` : programme principal et menu utilisateur
* `sym/` : algorithmes de cryptographie symétrique
* `asym/` : algorithmes de cryptographie asymétrique

Chaque algorithme est implémenté dans **un fichier distinct**.

---

# Algorithmes implémentés

## Cryptographie symétrique

* Chiffre de César
* Chiffre de Vigenère
* Chiffre Affine
* Chiffre de Playfair
* Chiffre de Hill
* One-Time Pad
* Substitution aléatoire
* RC4
* DES
* AES
* Structure de Feistel
* Twofish
* Serpent
* RC6
* MARS

## Cryptographie asymétrique

(À implémenter ultérieurement)

* RSA
* ElGamal
* Diffie-Hellman

---

# Interface des algorithmes (IMPORTANT)

Afin d’assurer la cohérence du projet, **tous les algorithmes doivent respecter la même structure de fonctions**.

Chaque fichier d’algorithme doit implémenter les fonctions suivantes :

```python
def encrypt(message, key):
    """
    Chiffre le message donné en utilisant la clé fournie.
    Retourne le texte chiffré.
    """
    pass


def decrypt(ciphertext, key):
    """
    Déchiffre le texte chiffré en utilisant la clé fournie.
    Retourne le message original.
    """
    pass
```

### Paramètres

* `message` : texte en clair à chiffrer
* `ciphertext` : texte chiffré à déchiffrer
* `key` : clé utilisée par l’algorithme (le type dépend de l’algorithme)

### Valeur retournée

Chaque fonction doit **retourner une chaîne de caractères contenant le résultat**.

Exemple d’utilisation depuis `main.py` :

```python
from sym import cesar

cipher = cesar.encrypt("bonjour", 3)
plain = cesar.decrypt(cipher, 3)
```

---

# Exécution du programme

Pour lancer le programme principal :

```bash
python main.py
```

Le programme affichera un menu permettant de :

1. Choisir entre cryptographie symétrique et asymétrique
2. Sélectionner un algorithme
3. Choisir le mode (chiffrement ou déchiffrement)
4. Entrer le message et la clé

---


# Remarques importantes

Tous les algorithmes doivent :

* respecter l’interface commune `encrypt()` / `decrypt()`
* ne pas demander d’entrées utilisateur directement dans les fichiers d’algorithmes
* retourner le résultat au lieu de l’afficher avec `print()`
