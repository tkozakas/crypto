alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
L_1 = [5, 3, 2, 0, 17, 10, 8, 24, 20, 11, 1, 12, 9, 22, 16, 6, 25, 4, 18, 21, 7, 13, 15, 23, 19, 14]
L_2 = [20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]
cText = '''
SFXWC WGAZS EOQJE JJQRK UWZDU 
SULLJ IPJLZ KNBST GVRTL DWPNM 
PFRXQ YQUE
'''
key = [9, 24]


def numerify(text):
    res = []
    for letter in text:
        if letter in alphabet:
            num = alphabet.index(letter)
            res.append(num)
    return res


def stringify(numbers):
    res = ''
    for number in numbers:
        letter = alphabet[number]
        res += letter
    return res


def rot(m, a):
    return (a + m) % len(alphabet)


def rsubst(rot, a):
    return rot.index(a)


def deEnigma(key, L1, L2, ciphertext):
    cipherVals = numerify(ciphertext)
    messageVals = []
    m1 = key[0]
    m2 = key[1]
    rIdx = 0

    for cipherVal in cipherVals:
        val = cipherVal
        val = rot(m2, val)
        val = rsubst(L2, val)
        val = rot(-m2, val)
        val = rot(m1, val)
        val = rsubst(L1, val)
        val = rot(-m1, val)

        m1 += 1
        rIdx += 1
        if (rIdx % len(alphabet)) == 0:
            m2 += 1

        messageVals.append(val)

    return stringify(messageVals)


print(deEnigma(key, L_1, L_2, cText))
