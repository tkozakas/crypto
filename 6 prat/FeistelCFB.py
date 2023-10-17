function = lambda m, k: (m | k) ^ ((k // 16) & m)
key = [217, 110, 123]
init_v = [156, 38]
ciphertext = [[80, 27], [59, 164], [227, 17], [14, 53], [95, 143], [179, 35], [115, 0], [30, 168], [207, 8], [36, 37],
              [99, 154], [152, 45], [94, 6], [43, 167], [255, 23], [21, 61], [85, 133], [164, 34], [126, 8], [26, 177],
              [215, 18], [37, 57], [127, 137], [134, 33], [77, 29], [33, 162], [226, 11], [13, 44], [71, 147],
              [181, 60], [104, 5], [29, 176], [216, 22], [50, 46], [107, 128], [130, 48], [64, 24], [58, 190],
              [248, 24], [28, 60], [84, 132], [180, 59], [109, 26], [19, 171], [209, 11]]


class BlockCipherCFB:
    def __init__(self, keys: list, initializationVector: list, s: int = 1):
        self.keys = keys
        self.initVector = initializationVector
        self.byteShift = s

    @staticmethod
    def xorfirst(bits: int, b1: list, b2: list):
        index = 0
        newBits = list()
        while index < bits and index < len(b1) and index < len(b2):
            n1 = b1[index]
            n2 = b2[index]
            newBits.append((n1 + n2) % 2)
            index += 1
        return newBits

    def iteration(self, initVector, keys, function):
        left, right = initVector
        for k in keys:
            f_out = function(right, k)
            left ^= f_out
            left, right = right, left
        left, right = right, left
        return [left, right]

    @staticmethod
    def blocksToString(blocks: list):
        return ''.join([chr(item[0]) + chr(item[1]) for item in blocks])

    def decrypt(self, text, function, keys, returnText=True):
        cipher = list()
        initVector = self.initVector.copy()
        for pair in text:
            c = self.iteration(initVector, keys, function)
            c = [c[0] ^ pair[0], c[1] ^ pair[1]]
            initVector = pair
            cipher.append(c)
        if returnText:
            return self.blocksToString(cipher)
        else:
            return cipher


cipher = BlockCipherCFB(key, init_v)
decrypted_text = cipher.decrypt(ciphertext, function, key)
print(decrypted_text)
