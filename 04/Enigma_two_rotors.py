alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
L_1 = [8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]
L_2 = [10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
cText = '''
WPRSQ WWWJL NYEMM IMLGO CFGBS
UZHCM RVVQV SNTNB SVJBR CSLVW
WTIUH KKQOV EQCPV KSLPZ EREPR
OFEQT DZYKX SOUZV FHEOE EMXGU
VCQGR HFBOE SETOP ZJJRH MZMYW
HSFYH VYVGB KNZBJ HWSKG FHAUD
HZGJK PFEPO IQZEU XEFUF BYDLW
VLNAB ZKXSH XVRVW CLCRZ WZFNR
RALMX JZEZO ZEALO TKTRQ PHBAX
NFPNG NSVXA SCJTZ LLXZI UJNIX
CDZYF ILWXD ESTWM ULUJT LBEVP
QVZJN XJIKU OEVXJ VPLYP VESOV
BRRCU KFWFN UGSNM ORWYD FZSFR
LCMWB MRHVR NAPDG WGKAH IWMOQ
BOYNF OJCPE CXPYE ZVJPO IYGDP
DUXQZ VHJNZ QKEIP IVIVP POKOJ
CJVXK CXXDX LNJHF IBWHC WUB 
'''
key = [3, 3]


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
