import Feistel as f

ciphertext = [[164, 164], [168, 167], [184, 187], [166, 170], [161, 187], [173, 162], [166, 189], [173, 174],
              [171, 164], [186, 190], [172, 174], [191, 191], [167, 170], [173, 170], [161, 181], [160, 168],
              [160, 167], [175, 170], [162, 183], [183, 167], [161, 179], [169, 162], [185, 190], [164, 185],
              [170, 162], [177, 176], [162, 173], [171, 174], [191, 190], [177, 160], [166, 179], [166, 170],
              [183, 161], [166, 170], [177, 161], [166, 179], [166, 170], [180, 176], [166, 170], [187, 189]]
function = lambda m, k: (m | k) ^ ((m // 16) & k)

brute_force_results_feistel = {}
for potential_key1 in range(0, 256):
    current_key = [potential_key1, 201]
    decrypted = f.Feistel.decrypt(ciphertext, current_key, function)
    brute_force_results_feistel[potential_key1] = decrypted

print(brute_force_results_feistel)
