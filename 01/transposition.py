import itertools

def load_words():
    try:
        with open('words.txt') as word_file:
            return set(word_file.read().split())
    except FileNotFoundError:
        print("Error: 'words.txt' not found. Please download it.")
        return set()

def solve_transposition(ciphertext, key_length):
    english_words = load_words()
    if not english_words:
        return "", None
        
    best_plaintext = ""
    best_key = None
    max_word_count = 0

    key_numbers = range(key_length)
    key_permutations = itertools.permutations(key_numbers)

    for key_perm in key_permutations:
        key = list(key_perm)
        num_columns = key_length
        num_rows = -(-len(ciphertext) // num_columns)
        
        plaintext_columns = [''] * num_columns

        col = 0
        row = 0
        for char in ciphertext:
            plaintext_columns[col] += char
            row += 1
            if row >= num_rows and col in key:
                 if (len(ciphertext) % num_columns != 0 and key.index(col) >= len(ciphertext) % num_columns):
                     row -= 1
            if row >= num_rows:
                 row = 0
                 col += 1
        
        decrypted_columns = [''] * num_columns
        for i, col_index in enumerate(key):
            decrypted_columns[i] = plaintext_columns[col_index]
        
        plaintext = ""
        for r in range(num_rows):
            for c in range(num_columns):
                 if r < len(decrypted_columns[c]):
                     plaintext += decrypted_columns[c][r]

        word_count = 0
        for word in english_words:
            if len(word) > 4 and word in plaintext.lower():
                word_count += 1

        if word_count > max_word_count:
            max_word_count = word_count
            best_plaintext = plaintext
            best_key = [k + 1 for k in key]
            print(f"New best guess with key {best_key} (score: {max_word_count}): {best_plaintext}")


    return best_plaintext, best_key

ciphertext = "MIEUGSSNRHSNKRXCSTLRMENEHSANYERCATIIETOICAPENHUWY"
key_len = 7

plaintext, key = solve_transposition(ciphertext, key_len)

print("\n--- Final Result ---")
print(f"Detected Key: {key}")
print(f"Decrypted Plaintext: {plaintext}")
