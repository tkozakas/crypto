function = lambda r, k: (r & k) ^ ((k % 16) | r)
key = [97, 104, 245]
init_v = [233, 121]
ciphertext = [[172, 183], [98, 252], [189, 36], [246, 240], [57, 177], [228, 127], [161, 164], [104, 237], [163, 51], [235, 248], [41, 178],
              [250, 105], [160, 183], [106, 224], [171, 34], [250, 246], [58, 161], [243, 126], [166, 183], [110, 225], [180, 52],
              [250, 248], [49, 186], [243, 121], [171, 179], [126, 140]]


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
