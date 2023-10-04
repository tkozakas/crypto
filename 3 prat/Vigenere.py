from collections import defaultdict

abc = u'AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ'
n = len(abc)


def friedm(text, k):
    textn = u""
    for r in text:
        if r in abc:
            textn += r
    l = len(textn)
    s = 0
    for i in range(k, l):
        if textn[i] == textn[i - k]:
            s += 1
    return 1. * s / (l - k)


def freq(text):
    d = defaultdict(int)
    s = ""
    for w in text:
        if w in abc:
            d[w] += 1
    for w in sorted(d, key=d.get, reverse=True):
        s += w
    return s


def prepare(text):
    textn = u''
    for a in text:
        if a in abc:
            textn += a
    return textn.upper()


def split(text, d):
    textn = prepare(text)
    tspl = [''] * d
    n = len(textn)
    for i in range(0, n):
        tspl[i % d] += textn[i]
    return tspl


def guess(test, k, sifr):  # test - dažniausių raidžių eilutė, k - spėjamas šifro raktas
    tst = u''
    for r in test:
        if r in abc:
            tst += r
    tstk = u''
    for r in tst:
        tstk += abc[(abc.index(r) + k) % n]
    d = defaultdict(int)
    sifrn = u''
    for r in sifr:
        if r in abc:
            sifrn += r
    for r in sifrn:
        if r in tstk:
            d[r] += 1
    kiek = len(sifrn)
    s = 0
    for a in d.keys():
        s += d[a]
    return 1. * s / kiek


cipher_text = (
    u'''
    YIŠSŽ CČŠVF YĮVLU JELĖY ARYKH 
    ČGDUY LČŲTL KDFYĖ ULYIS TĮŪTV 
    ĮFHSH COZUF LCMKJ ĮVMZN TŪLBE 
    KŽLĘŠ VKEVČ ĘŠTND GYBMU IBATO 
    ČCĘLY ĖYYVŪ EDJĖL ERŽSC ĘŪENF 
    SYOPT LSČDH NKMZŪ OYUCĄ IĖĮFH 
    LDVTE GVIŪT ĮĘLĄŪ DHCEŠ TMUYE 
    VIDLK ĘASĮJ SĖCAN TĮLČA YEVFD 
    AFORC AKNLR VĖŪĄF SHTŽT ĮVLŠZ 
    FESVŠ ZFAOS BČĮNŠ KAHEŪ LYIAŲ 
    AGDBN KČĮZH ŽDJSĖ CTTOK MYIML 
    LEBEM ULĄIH MUCČM NHUGD ZE  
''')
def decrypt(ciphertext, key):
    decrypted_text = ''
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char in abc:
            new_index = (abc.index(char) - abc.index(key[i % len(key)])) % len(abc)
            decrypted_text += abc[new_index]
        else:
            decrypted_text += char
    return decrypted_text


# Known plaintext and its position
known_plaintext = 'LIE'
position = 0
counter = 0
# Try all possible keys of length 6
for i in range(len(abc)):
    for j in range(len(abc)):
        for k in range(len(abc)):
            for l in range(len(abc)):
                for m in range(len(abc)):
                    for n in range(len(abc)):
                        counter += 1
                        if counter % 10000 == 0:
                            print(f"Keys tried: {counter}")
                        key = abc[i] + abc[j] + abc[k] + abc[l] + abc[m] + abc[n]
                        decrypted_text = decrypt(cipher_text, key)
                        if decrypted_text[position:position + len(known_plaintext)] == known_plaintext:
                            print(f"Possible key: {key}")
                            print(f"Decrypted text: {decrypted_text}\n")


# freq_output = freq(cipher_text)
# print(freq_output)
#
# f = split(cipher_text, 6)
# print(f[0], f[1])
#
# key_guess = guess(f[1], 6, cipher_text)
# print(key_guess)
#
# res = friedm(cipher_text, 6)
# print(res)
