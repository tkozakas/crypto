L_1 = [5, 3, 2, 0, 17, 10, 8, 24, 20, 11, 1, 12, 9, 22, 16, 6, 25, 4, 18, 21, 7, 13, 15, 23, 19, 14]
L_2 = [20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]
key1 = 8
key2 = 22
s = [2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]

txt = u'''
LBSTV LITZU OHITP QXAVD MTQUI 
PWWMR VPLCM IYROY VNNVP UTFGQ 
FEFIM JQYSS DQOJC XRNKX KOBPR 
D
'''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def theEnigma(key1, key2, L1, L2, s, ciphertext):
    m1 = key1
    m2 = key2
    rIdx = 0

    output = ""

    for i in ciphertext:
        if i in alphabet:  # Ensure that the character is in the alphabet
            letter = alphabet.index(i)

            l1index = L1[(letter + m1) % len(alphabet)]
            l2index = L2[(l1index - m1 + m2) % len(alphabet)]
            temp = s.index((l2index - m2) % len(alphabet))
            l2index = L2.index((temp + m2) % len(alphabet))
            l1index = L1.index((l2index - m2 + m1) % len(alphabet))

            output += alphabet[(l1index - m1) % len(alphabet)]

            m1 += 1
            rIdx += 1
            if (rIdx % len(alphabet)) == 0:
                m2 += 1
        else:
            output += i  # If the character is not in the alphabet, add it to the output as it is.

    return output


print(theEnigma(key1, key2, L_1, L_2, s, txt).replace(' ', '').replace('\n', ''))
