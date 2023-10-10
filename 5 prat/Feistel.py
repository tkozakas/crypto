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

            left, right = right, left  # last iteration does not need to be swapped, so swap back
            cipher.append([left, right])
        if returnText:
            return Feistel.blocksToString(cipher)
        else:
            return cipher

    @staticmethod
    def decrypt(text, key, function, returnText=True):
        keyrev = key.copy()
        keyrev.reverse()
        return Feistel.encrypt(text, keyrev, function, returnText)  # just reverse the key for decryption

    @staticmethod
    def blocksToString(blocks):
        message = ""
        for ch in blocks:
            for c in ch:
                message += chr(c)
        return message


function = lambda m, k: (m | k) ^ ((k // 16) & m)
key = [132, 235, 165]
ciphertext = [[42, 164], [56, 167], [43, 170], [42, 188], [45, 164], [37, 178], [48, 175], [37, 162], [36, 170],
              [36, 180], [43, 166], [32, 167], [38, 184], [41, 172], [43, 168], [35, 174], [54, 171], [33, 162],
              [32, 176], [40, 175], [46, 168], [45, 170], [63, 165], [59, 162], [52, 190], [44, 169], [38, 188],
              [40, 167], [51, 170], [59, 162], [35, 176], [56, 161], [37, 162], [33, 191], [50, 175], [47, 168],
              [49, 177], [42, 191], [59, 178], [58, 164], [45, 168], [55, 170], [40, 167], [42, 184], [49, 174],
              [38, 173], [33, 166], [51, 170], [59, 162], [35, 184], [36, 180], [46, 164], [32, 186], [51, 187],
              [51, 170], [52, 190], [59, 162], [34, 184], [36, 162], [61, 166]]
decrypted_text = Feistel.decrypt(ciphertext, key, function)
print(decrypted_text)
