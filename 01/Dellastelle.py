def create_bifid_square(key, alphabet):
    cleaned_key = ''.join(sorted(set(key), key=key.index)).upper()
    for letter in cleaned_key:
        alphabet = alphabet.replace(letter, '')
    square_string = cleaned_key + alphabet
    square = {}
    k = 0
    for i in range(1, 6):
        for j in range(1, 6):
            square[(i, j)] = square_string[k]
            k += 1
    return square


def create_coords_lookup(square):
    return {v: k for k, v in square.items()}


def bifid_decrypt(ciphertext, period, square, coords_lookup):
    plaintext = ""
    for i in range(0, len(ciphertext), period):
        chunk = ciphertext[i:i + period]
        chunk_len = len(chunk)
        if chunk_len == 0:
            break

        coordinates = [coords_lookup[char] for char in chunk]

        numbers = []
        for r, c in coordinates:
            numbers.extend([r, c])

        rows = numbers[:chunk_len]
        cols = numbers[chunk_len:]

        for j in range(chunk_len):
            plaintext += square[(rows[j], cols[j])]

    return plaintext

ciphertext = "HKCXV YUDLL RKCKF LGMIR CNYMT RKHCT NTZAB TPCFV"
ciphertext = ciphertext.replace(" ", "")
key = "TRAVEL"
period = 5
bifid_alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

bifid_square = create_bifid_square(key, bifid_alphabet)
bifid_coords_lookup = create_coords_lookup(bifid_square)

decrypted_bifid_message = bifid_decrypt(ciphertext, period, bifid_square, bifid_coords_lookup)

print(f"Decrypted Message: {decrypted_bifid_message}")
