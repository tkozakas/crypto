from sympy import Matrix

ciphertext = "MČKCA SĘVŠE SLŽŲB ĘMCĄČ REČFA TDŽAO ŪKUZA TĮČAO ĖBČDP ŲAĖĄČ REPČA KLDHĖ SLICŠ EĮCAT EŲGYN DŪAĮT PĘERI BASVJ BFDHŪ ZTZUY ŠMREĮ ŽREČF ZCZČĘ ĮERYK JDŽŲŪ ŽAOIŲ OPNĖB GKRŲM OVZŠĖ CYSŪŽ KCPNA OIŲAT GŠOVY AŽŲMČ KCŠRA SŠROP ĖIIOI ČERŪZ ČSATŪ ŽGŠOV YAJŽK ĮOP".replace('\n', ' ').strip()

alphabet = u'AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ'
key_matrix = Matrix([[27, -17], [-19, 12]])  # don't forget to inverse the matrix first https://www.dcode.fr/matrix-inverse


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
