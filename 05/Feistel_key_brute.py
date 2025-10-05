import Feistel as f

# # one key unknown
# ciphertext = [[11, 76], [16, 83], [16, 67], [1, 80], [23, 83], [12, 74], [10, 69], [3, 74], [15, 72], [16, 82], [3, 78], [20, 91], [20, 72],
#               [13, 74], [16, 84], [11, 68], [2, 78], [5, 72], [1, 68], [14, 71], [1, 68], [17, 66], [0, 65], [7, 84], [13, 76], [3, 76],
#               [16, 80], [10, 76], [9, 81], [8, 70], [20, 70], [15, 80], [18, 81], [5, 72], [17, 79], [16, 67]]
# function = lambda r, k: (r ^ k) & ((k // 16) | r)
# for potential_key1 in range(0, 256):
#     current_key = [potential_key1, 56]
#     decrypted = f.Feistel.decrypt(ciphertext, current_key, function)
#     print(f"Key Found: {potential_key1}, Decrypted Text: {decrypted}")

# two keys
ciphertext = [[89, 21], [90, 23], [90, 23], [75, 30], [65, 13], [64, 17], [65, 2], [70, 10], [93, 19], [64, 12], [72, 8], [70, 6], [67, 7],
              [74, 10], [90, 8], [65, 22], [65, 17], [64, 1], [75, 23], [75, 29], [79, 30], [70, 17], [75, 11], [77, 7], [92, 23], [75, 28],
              [75, 10], [64, 10], [93, 29], [79, 4], [74, 14], [67, 9], [91, 10], [70, 16], [70, 2], [94, 30], [74, 3], [71, 9], [75, 15],
              [64, 0], [89, 17], [65, 11], [0, 101]]
function = lambda r, k: ((r & k) ^ ((k % 16) | r))

unwanted_symbols = ['!', '@', '/', '\\', '^', '_', ',', '.', '#', '+', '{', '}', '\n', '\r']
brute_force_results_feistel = {}
for potential_key1 in range(0, 256):
    for potential_key2 in range(0, 256):
        current_key = [potential_key1, potential_key2]
        decrypted = f.Feistel.decrypt(ciphertext, current_key, function)

        if not any(sym in decrypted for sym in unwanted_symbols):
            brute_force_results_feistel[(potential_key1, potential_key2)] = decrypted.upper()

for key, sentence in brute_force_results_feistel.items():
    print(f"Key: {key}, Decrypted Text: {sentence}")
