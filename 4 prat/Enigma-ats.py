L_1 = [8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]
L_2 = [10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
key1 = 2
key2 = 10
s = [2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]

txt = u'''
PKAWF PKRPI JXCTE XNRFE TBNZB 
UDTDD QUPCY DRZWD OOCVS IAZCY 
QAOOW YQLOW COTZU XASON GJONS 
GBIJR TILIX KEUUD PFNNQ ZCLLO 
OFOIS YOJRX UNIFE QEGQY TACUU 
XDXWH WFRBL HPHTY PVDUY NHXEO 
OVATA UUHHO JYDJC XCMFF YSYSE 
QZR 
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


print(theEnigma(key1, key2, L_1, L_2, s, txt))



# 3
# GILTI NEPAK ELENU OSTAL OGALV
# KOKIS TEBUK LABUT UPAZA DEJES
# ASARO SSUZV ILGOJ AIAKY SEULE
# NSPYG ELISI SVYDE SGILT INEVE
# RKIAN TSUKR ESTAS PRABI LOTYL
# IUIRR AMINA MUBAL SUZVE LGDAM
# ASIGE LESAU GANCI ASANT PALAN
# GES
