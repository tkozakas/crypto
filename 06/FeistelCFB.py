function = lambda r, k: (r & k) ^ ((k % 16) | r)
key = [97, 104, 245]
init_v = [233, 121]
ciphertext = [[186, 175], [101, 249], [181, 47], [249, 254], [38, 163], [251, 125], [165, 166], [100, 228], [166, 33], [232, 233],
              [37, 178], [235, 120], [186, 182], [99, 250], [164, 58], [248, 254], [55, 176], [227, 122], [163, 162], [106, 228], [176, 44],
              [228, 250], [54, 163], [234, 121], [181, 175], [126, 243], [168, 49], [253, 239], [54, 179], [235, 107], [181, 175],
              [115, 239], [186, 63], [230, 147]]

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
