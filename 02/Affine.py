from math import gcd

ciphertext = "UBGLZ WUSFU WONPB SNNBG RSEVL BWISB SFSPE PTWLP FSGQ"
text_start = ""  # leave empty if needed

abc = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = len(abc)


def affine_cipher(text, a, b, mode="encrypt"):
    """
    Encrypts or decrypts a given text using the affine cipher.

    Parameters:
    - text: The text to be encrypted/decrypted.
    - a: The 'a' key for the affine cipher.
    - b: The 'b' key for the affine cipher.
    - mode: Either "encrypt" or "decrypt".

    Returns:
    - The encrypted or decrypted text.
    """
    text_u = text.upper()
    t = u''
    for r in text_u:
        if r in abc:
            t += r
    c = u''

    # Check if 'a' is coprime to length of alphabet
    if gcd(a, n) != 1:
        raise ValueError(f"'a' value {a} is not coprime to {n}.")

    # Encrypt or decrypt based on mode
    for r in t:
        if mode == "encrypt":
            m = (a * abc.index(r) + b) % n
        elif mode == "decrypt":
            a_inv = mod_inverse(a, n)  # Multiplicative inverse of 'a'
            m = (a_inv * (abc.index(r) - b)) % n
        c += abc[m]

    return c


def brute_force_affine_to_find_start(ciphertext, desired_start):
    """
    Brute-forces the affine cipher using all possible combinations of 'a' and 'b'
    until a decryption is found that starts with the desired start text.

    Parameters:
    - ciphertext: The encrypted text.
    - desired_start: The desired starting characters of the decrypted text.

    Returns:
    - The decrypted text, a, and b values if found. Otherwise, None.
    """
    results = []
    possible_a_values = coprime_list(n)
    for a in possible_a_values:
        for b in range(n):
            decrypted_text = affine_cipher(ciphertext, a, b, mode="decrypt")
            if not desired_start or decrypted_text.startswith(desired_start):
                results.append((decrypted_text, a, b))
    return results


def coprime_list(n):
    """Return a list of numbers from 1 to n that are coprime to n."""
    return [i for i in range(1, n + 1) if gcd(i, n) == 1]


def mod_inverse(a, m):
    """
    Calculate the modular inverse of a modulo m.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Modular inverse for {a} mod {m} does not exist")


decrypted_text = brute_force_affine_to_find_start(ciphertext, text_start)
print(decrypted_text)
