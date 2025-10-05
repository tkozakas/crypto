function = lambda m, k: (m | k) ^ ((k // 16) & m)
key = [169, 120, 168]
ciphertext = [[15, 189], [21, 173], [10, 172], [26, 183], [13, 176], [31, 183], [12, 183], [26, 189], [29, 182], [23, 175], [24, 182],
              [28, 185], [13, 188], [25, 161], [27, 170], [29, 185], [19, 177], [15, 177], [21, 180], [27, 185], [21, 180], [1, 183],
              [13, 185], [23, 188], [24, 172], [22, 182], [27, 189], [27, 183], [20, 168], [20, 189], [12, 189], [1, 183], [12, 170],
              [13, 170], [24, 182], [10, 190], [22, 170], [21, 185], [12, 177], [22, 182], [16, 182], [12, 183], [25, 181], [24, 170],
              [27, 180], [29, 171], [12, 185], [12, 173], [28, 216]]


class Feistel:
    @staticmethod
    def encrypt(text, keys, function, returnText=True):
        cipher = list()
        for pair in text:
            left, right = pair[0], pair[1]
            for k in keys:
                f_out = function(right, k)
                left = left ^ f_out
                left, right = right, left
            left, right = right, left
            cipher.append([left, right])
        if returnText:
            return Feistel.blocksToString(cipher)
        else:
            return cipher

    @staticmethod
    def decrypt(text, key, function, returnText=True):
        keyrev = key.copy()
        keyrev.reverse()
        return Feistel.encrypt(text, keyrev, function, returnText)

    @staticmethod
    def blocksToString(blocks):
        message = ""
        for ch in blocks:
            for c in ch:
                message += chr(c)
        return message


decrypted_text = Feistel.decrypt(ciphertext, key, function)
print(decrypted_text)
