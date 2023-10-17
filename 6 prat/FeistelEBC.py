function = lambda m, k: (m | k) ^ ((k // 16) & m)
key = [217, 110, 123]
ciphertext = [[100, 175], [109, 189], [104, 178], [126, 167], [100, 179], [96, 170], [108, 189], [117, 191], [97, 178],
              [116, 171], [107, 190], [112, 173], [122, 164], [97, 174], [103, 170], [124, 161], [111, 182], [97, 170],
              [102, 176], [107, 190], [109, 182], [110, 178], [104, 190], [109, 173], [119, 187], [98, 178], [106, 172],
              [124, 163], [108, 175], [114, 161], [108, 174], [112, 184], [116, 173], [112, 165], [108, 186],
              [122, 164], [103, 186], [103, 170], [98, 178], [106, 172], [127, 163], [117, 186], [110, 182], [98, 178],
              [98, 182], [98, 174], [116, 171], [100, 187], [100, 191], [98, 177], [120, 164]]


class BlockCipher:

    @staticmethod
    def encrypt(text, function, keys: list, returnText=True):
        cipher = list()
        for pair in text:
            left, right = pair[0], pair[1]
            for k in keys:
                f_out = function(right, k)
                left = left ^ f_out
                left, right = right, left

            left, right = right, left  # last iteration does not need to be swapped, so swap back
            cipher.append([left, right])
        if returnText:
            return BlockCipher.blocksToString(cipher)
        else:
            return cipher

    @staticmethod
    def decrypt(text, function, keys, returnText=True):
        keyrev = keys.copy()  # fix the copy method call
        keyrev.reverse()
        return BlockCipher.encrypt(text, function, keyrev, returnText)  # use reversed keys

    @staticmethod
    def blocksToString(blocks):
        message = ""
        for ch in blocks:
            for c in ch:
                message += chr(c)
        return message


decrypted_text = BlockCipher.decrypt(ciphertext, function, key)
print(decrypted_text)
