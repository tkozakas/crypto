from sympy import Matrix

ciphertext = "BIJPC ĄGCEG ZJĖPL ĄĮDCČ ĖUTŽĮ JRĄČI OKŪBĮ JSČČI BYDCM DĖŠCČ ĖUJČK KĖHĮK ZJNPE GBVĮJ LĮŪME ŲČAKS YTĖGZ YCĄYL ŲJMPU MĮUIM BZĖUY ĄĖUTŽ ĄDRIU NĖGBA GŲĖPJ TČIHV DNDKK RZUJR ĮHUŠS PPLJT JPGĮČ IHVĮJ YŠĮHM KĖPBI JPRUC ĄRUDN OOŠIĖ ŪĖGUM ŽĄĮJJ TYŠĮH MKILĄ ŲDN"
alphabet = u'AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ'
key_matrix = Matrix([[5, 10], [27, 3]])  # don't forget to inverse the matrix first https://www.dcode.fr/matrix-inverse


def decodeHill(letters, matrix, alphabet):
    l1 = alphabet.index(letters[0])
    l2 = alphabet.index(letters[1])
    o1 = matrix[0, 0] * l1 + matrix[0, 1] * l2
    o2 = matrix[1, 0] * l1 + matrix[1, 1] * l2
    return alphabet[o1 % len(alphabet)] + alphabet[o2 % len(alphabet)]


def dcd(text, matrix, alphabet):
    text = ''.join([i for i in text if i.strip() != ''])
    out = ''
    for i in range(0, len(text), 2):
        out += decodeHill(text[i:i + 2], matrix, alphabet)
    return out


decrypted_text = dcd(ciphertext, key_matrix, alphabet);
print(decrypted_text)
