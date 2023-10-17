function = lambda m, k: (m | k) ^ ((k // 16) & m)
key = [217, 110, 123]
init_v = [156, 38]
ciphertext = [[82, 11], [49, 182], [230, 10], [18, 47], [75, 134], [184, 58], [103, 22], [24, 181], [205, 9], [44, 55],
              [117, 145], [154, 38], [82, 28], [51, 160], [244, 11], [25, 43], [72, 154], [175, 46], [100, 29],
              [10, 172], [204, 28], [56, 57], [126, 158], [145, 42], [92, 15], [51, 160], [230, 9], [1, 51], [72, 155],
              [171, 34], [108, 22], [5, 188], [206, 23], [49, 53], [121, 141], [130, 48], [85, 12], [35, 191],
              [231, 13], [23, 47], [79, 146], [167, 57], [121, 20], [3, 161], [201, 17], [12, 75]]


class BlockCipherCBC:

    @staticmethod
    def blocksToString(blocks):
        message = ""
        for ch in blocks:
            for c in ch:
                message += chr(c)
        return message

    @staticmethod
    def encrypt(text, function, keys, initVector, returnText=True):
        cipher = []
        iv1, iv2 = initVector[0], initVector[1]

        for pair in text:
            left, right = pair[0], pair[1]
            left ^= iv1
            right ^= iv2
            for k in keys:
                f_out = function(right, k)
                left = left ^ f_out
                left, right = right, left

            left, right = right, left  # last iteration does not need to be swapped, so swap back
            iv1, iv2 = left, right
            cipher.append([left, right])
        if returnText:
            return BlockCipherCBC.blocksToString(cipher)
        else:
            return cipher

    @staticmethod
    def decrypt(text, function, keys, initVector, returnText=True):
        keyrev = keys.copy()
        keyrev.reverse()
        plain = []
        iv1, iv2 = initVector[0], initVector[1]

        for pair in text:
            left, right = pair[0], pair[1]
            orig_left, orig_right = left, right  # store original values for later use

            for k in keyrev:
                f_out = function(right, k)
                left = left ^ f_out
                left, right = right, left

            left, right = right, left  # last iteration does not need to be swapped, so swap back

            left ^= iv1
            right ^= iv2
            iv1, iv2 = orig_left, orig_right
            plain.append([left, right])
        if returnText:
            return BlockCipherCBC.blocksToString(plain)
        else:
            return plain


decrypted_text = BlockCipherCBC.decrypt(ciphertext, function, key, init_v, True)
print(decrypted_text)
