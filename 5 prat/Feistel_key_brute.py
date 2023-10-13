import Feistel as f

# # one key unknown
# ciphertext = [[164, 164], [168, 167], [184, 187], [166, 170], [161, 187], [173, 162], [166, 189], [173, 174],
#               [171, 164], [186, 190], [172, 174], [191, 191], [167, 170], [173, 170], [161, 181], [160, 168],
#               [160, 167], [175, 170], [162, 183], [183, 167], [161, 179], [169, 162], [185, 190], [164, 185],
#               [170, 162], [177, 176], [162, 173], [171, 174], [191, 190], [177, 160], [166, 179], [166, 170],
#               [183, 161], [166, 170], [177, 161], [166, 179], [166, 170], [180, 176], [166, 170], [187, 189]]
# function = lambda m, k: (m | k) ^ ((m // 16) & k)
# brute_force_results_feistel = {}
# for potential_key1 in range(0, 256):
#     current_key = [potential_key1, 201]
#     decrypted = f.Feistel.decrypt(ciphertext, current_key, function)
#     brute_force_results_feistel[potential_key1] = decrypted.upper()
#
# print(brute_force_results_feistel)

# two keys
ciphertext = [[83, 19], [84, 8], [82, 22], [66, 1], [66, 30], [87, 25], [67, 13], [85, 31], [73, 3], [87, 25], [75, 29],
              [64, 6], [73, 18], [78, 5], [70, 28], [64, 6], [70, 28], [87, 17], [76, 23], [72, 12], [70, 0], [87, 8],
              [70, 29], [84, 13], [66, 4], [67, 30], [72, 3], [78, 18], [76, 10], [83, 19], [84, 15], [72, 12],
              [78, 14], [84, 8], [74, 16], [75, 15], [78, 14], [84, 16], [70, 0], [87, 28], [82, 17], [76, 6], [75, 1],
              [84, 18], [84, 8], [78, 18], [76, 15], [70, 0], [67, 9], [87, 23], [81, 23], [84, 26], [87, 25], [84, 26],
              [82, 17], [78, 8], [85, 17], [70, 4], [87, 25], [83, 25], [76, 12], [78, 0], [76, 10], [83, 25], [73, 15],
              [85, 10], [70, 5], [78, 10], [104, 71]]
function = lambda m, k: (m & k) ^ ((k % 16) | m)

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
