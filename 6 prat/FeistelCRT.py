function = lambda m, k: (m | k) ^ ((k // 16) & m)
key = [217, 110, 123]
ciphertext = [[191, 244], [164, 225], [189, 248], [178, 247], [177, 255], [184, 228], [179, 248], [184, 240],
              [163, 247], [163, 242], [183, 251], [188, 252], [162, 245], [189, 246], [183, 242], [178, 246],
              [177, 242], [161, 226], [190, 231], [186, 230], [187, 228], [164, 250], [167, 255], [166, 249],
              [185, 255], [184, 236], [162, 249], [161, 238], [185, 232], [180, 237], [166, 249], [163, 248],
              [162, 219], [176, 217], [189, 199], [184, 199], [165, 204], [181, 210], [161, 196], [188, 222],
              [163, 202], [182, 222], [190, 202], [178, 215], [160, 203], [162, 214], [187, 206], [186, 206],
              [163, 223], [165, 222], [183, 199], [182, 219], [181, 209], [168, 193], [179, 199], [186, 198],
              [185, 200], [180, 205], [177, 213], [178, 200], [185, 200], [180, 197], [187, 209], [178, 211],
              [165, 250], [164, 231], [161, 253], [190, 240], [187, 247], [184, 251], [187, 246], [166, 230],
              [181, 228], [180, 243], [187, 233], [186, 238], [165, 251], [171, 246], [183, 242], [182, 237],
              [177, 229], [184, 227], [187, 241], [160, 225], [185, 230], [163, 254], [183, 248], [188, 227],
              [191, 237]]


class BlockCipherCRT:
    def __init__(self, keys: list):
        self.keys = keys
        self.counter = 0

    @staticmethod
    def counterIteration(m, k, function):
        F = (m | k) ^ ((k // 16) & m)
        return [F, F]

    def iteration(self, block, keys, function):
        left, right = block
        for k in keys:
            f_out = function(right, k)
            left ^= f_out
            left, right = right, left
        left, right = right, left
        return [left, right]

    @staticmethod
    def blocksToString(blocks: list):
        return ''.join([chr(item[0]) + chr(item[1]) for item in blocks])

    def decrypt(self, text, function, startingValue=0, returnText=True):
        keys = self.keys
        cipher = list()
        i = startingValue
        for pair in text:
            s = self.counterIteration(i, keys[0], function)
            c = self.iteration(s, keys, function)
            c = [c[0] ^ pair[0], c[1] ^ pair[1]]
            i += 1
            cipher.append(c)
        if returnText:
            return self.blocksToString(cipher)
        else:
            return cipher


cipher = BlockCipherCRT(key)
decrypted_text = cipher.decrypt(ciphertext, function)
print(decrypted_text)
