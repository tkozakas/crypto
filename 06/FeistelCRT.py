function = lambda r, k: (r & k) ^ ((k % 16) | r)
key = [97, 104, 245]
ciphertext = [[69, 95], [66, 71], [74, 79], [93, 66], [64, 77], [95, 72], [68, 90], [95, 71], [75, 85], [66, 73], [82, 77], [65, 87],
              [72, 69], [85, 71], [71, 64], [76, 85], [73, 65], [66, 76], [88, 95], [77, 94], [77, 82], [72, 95], [69, 74], [67, 90],
              [86, 68], [74, 92], [67, 84], [72, 65], [89, 81], [64, 71], [81, 54]]



class BlockCipherCRT:
    def __init__(self, keys: list):
        self.keys = keys
        self.counter = 0

    @staticmethod
    def counterIteration(r, k):
        F = (r & k) ^ ((k % 16) | r)
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
            s = self.counterIteration(i, keys[0])
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
