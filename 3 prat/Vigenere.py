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


# Given cipher text
cipher_text = (u'YIŠSŽ CČŠVF YĮVLU JELĖY ARYKH ČGDUY LČŲTL KDFYĖ ULYIS TĮŪTV ĮFHSH COZUF LCMKJ ĮVMZN TŪLBE KŽLĘŠ VKEVČ '
               u'ĘŠTND GYBMU IBATO ČCĘLY ĖYYVŪ EDJĖL ERŽSC ĘŪENF SYOPT LSČDH NKMZŪ OYUCĄ IĖĮFH LDVTE GVIŪT ĮĘLĄŪ '
               u'DHCEŠ TMUYE VIDLK ĘASĮJ SĖCAN TĮLČA YEVFD AFORC AKNLR VĖŪĄF SHTŽT ĮVLŠZ FESVŠ ZFAOS BČĮNŠ KAHEŪ '
               u'LYIAŲ AGDBN KČĮZH ŽDJSĖ CTTOK MYIML LEBEM ULĄIH MUCČM NHUGD ZE')

freq_output = freq(cipher_text)
print(freq_output)

f = split(cipher_text, 6)
print(f[0], f[1])

key_guess = guess(f[0], 6, cipher_text)
print(key_guess)

res = friedm(cipher_text, 6)
print(res)
