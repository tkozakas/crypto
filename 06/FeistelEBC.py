function = lambda r, k: (r & k) ^ ((k % 16) | r)
key = [97, 104, 245]
ciphertext = [[78, 70], [76, 74], [84, 90], [67, 70], [65, 72], [84, 69], [85, 90], [90, 76], [88, 70], [73, 69], [95, 77], [90, 72],
              [72, 71], [95, 72], [85, 93], [78, 76], [67, 72], [65, 77], [76, 76], [73, 71], [88, 91], [73, 72], [95, 79], [64, 70],
              [84, 72], [65, 76], [66, 69], [77, 94], [93, 72], [95, 76], [85, 93], [95, 76], [78, 76], [93, 64], [66, 76], [89, 79],
              [72, 65], [72, 68], [78, 90], [85, 90], [90, 76], [94, 72], [66, 74], [78, 71], [78, 70], [84, 93], [74, 71]]



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
