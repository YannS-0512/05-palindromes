#### Fonction secondaire
"""palindrome code"""


def ispalindrome(p):
    """return boolean if string is palindrome or not"""
    p = p.lower()
    table = str.maketrans("àâäéèêëîïôöùûüç", "aaaeeeeiioouuuc",  " !$%&'()*+,-./:;<=>?@[]^_`{|}~ ")

    result = p.translate(table)
    return bool(result == result[::-1])

#### Fonction principale


def main():
    """methode main"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
