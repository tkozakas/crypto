def create_bifid_square(key, alphabet):
    """Create a 5x5 Bifid square based on the given key and alphabet."""
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
    """Create a reverse lookup for the Bifid square."""
    return {v: k for k, v in square.items()}


def bifid_decrypt(ciphertext, period, square, coords_lookup):
    """Decrypt a ciphertext using the Bifid cipher."""
    coordinates = [coords_lookup[char] for char in ciphertext]
    flattened = []
    for coord in coordinates:
        flattened.extend(coord)
    half_length = len(flattened) // 2
    rows = flattened[:half_length]
    cols = flattened[half_length:]
    pairs = list(zip(rows, cols))
    plaintext = "".join([square[pair] for pair in pairs])
    return plaintext


# Initialize variables
ciphertext = "PVPVX BQAZE SBLDY SNAAP SIIEO PNOYQ TNOSU KAAWW TNGKX VEPBD UBAXH TSSKH HKMDZ NPPED SRINV PSHVC SHIQG PBGVD VSHCI SFILO NVWHZ NHQZG NSOPD HSOEI STOBA SINVE "
ciphertext = ciphertext.replace(" ", "")
key = "siena"
bifid_alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

# Prepare the Bifid square and lookup
bifid_square = create_bifid_square(key, bifid_alphabet)
bifid_coords_lookup = create_coords_lookup(bifid_square)

# Decrypt the ciphertext
decrypted_bifid_message = bifid_decrypt(ciphertext, 5, bifid_square, bifid_coords_lookup)
print(decrypted_bifid_message)
