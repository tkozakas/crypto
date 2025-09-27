from collections import defaultdict

abc = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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


def Vigenere(text, key):  # Vigenere cipher
    textn = prepare(text)
    keyn = prepare(key)
    textc = u""
    keys = []
    lk = len(keyn)
    for i in range(0, lk):
        keys.append(abc.index(keyn[i]))
    lt = len(textn)
    for i in range(0, lt):
        textc += abc[(abc.index(textn[i]) + keys[i % lk]) % n]
    return textc


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
cipher_text = (
    u'''
VYTZR ZLLGJ THDMU YRTNE NFJYA 
GGIWT KWKJX XVXJV NTHEP VWXEM 
NZXTJ CYZXA USFVE GVGKG LXJHG 
MIEGT OVRME EVYIF SXKTE EEIVY 
SWKTT FPBXI TRXXV MPKLX HITZS 
WHVKF VMGAQ IPWOE TZMGG XCSPR 
ARYZP EAEOW JKAIF DEGKE RGPBU 
EVZSG GJUKE MAWVZ GTDXG TLGAU 
WVWMG GTPTM SRCCC LAWCE HVATJ 
VVWWZ GCSIE IPKEG VMPDE KAEPI 
ICWAU BMLAR KKMTD FTVED ARVFX 
AWKGI QTFET DCLNI TJMHF SHKLX 
WRKXQ TKCUK IFARW EXBDX JVWLW 
GWIIV JCRKS ZJERY CPSWN RVZWP 
AKLXH VGJIK NIQWK HNITE QXFXU 
KAHWZ GEXLZ EXVWB FGGSV HMKJK 
MMKUW RVXDC KEXHL LGGYU DMEUS 
FSMPK LXUVG RXBGR QWEIM FNZGX 
FGTPT MASPJ XTFHC IHWWW CEHMZ 
IKEZX FXKFR HXTWS PBUOG PGKQT 
VFKKS TJPEE LLQLK AUVAG XHYVC 
GLRZE URPHF KCEHV GQRCI QZMUK 
SKQMV NELFX WEXBD XJVXA UIPKY 
KQXJR XBLHG MIEGT GUEGQ XJZRZ 
ESTVX ASRCU LHUER GVHSG JVWMG 
IKKLX JIPTV RHXKF RHJGT PTMSR 
CCCLA WVYIL UMGEG XGJHZ RWARI 
NITCR GJWXK MPTVR HXQJC LLIOJ 
MGHET KMVMP CILXH PCTIW SRQKM 
VWSHY MLSFK CMMAI UZRMZ IRYME 
SHGCT AAERR TXJEN VBTFH GIWPW 
IMCCX PTTVW LEIUJ IGYIT ZROAX 
KEKLM FOZWL ASPJS YUMRY IKKSH 
NLBUL JVTKG GGVHX VXQJS ENICC 
QHKXC CPAAW ULGVW WUTVX SXGUE 
IMFNZ GLLMT WSKKS OVQHF XJJLX 
DEVVV PJSVV EGWWU RCHFQ GKLHV 
WQWGK QTVFK KSTJP AAAGJ GVHNI 
FLWXX YNRWT FMPKV HVYEK MHFJQ 
IRHNM EVFKA XKJLV JCRKE GSPAJ 
XLSXV VQILM PXXHT VGROZ WVORR 
VGHGJ EGVGK GLXJW FLVBF KYFVE 
VACIM TFHCW EFGYU JXHJC VYIZG 
PFSYZ ARYYM VZGTP TMSRC CCLAW 
YRWTH VQDMG WRVVP XEIPK GKQTV 
FKKST JPEGV MVJQB KYUVA XJIKE 
ZHDZG UMGLL GVBXU YVZSG GJORX 
TZETZ EGVMP KLXVV GPJNK GQEZB 
UXKFR TFHKD TKAWQ EQXFX DFXAA 
RVYIX SVNPX AUIPK YKQ
    '''
)

freq_output = freq(cipher_text)
print(freq_output)

f = split(cipher_text, 6)
print(f[0], f[1])

key_guess = guess(f[0], 6, cipher_text)
print(key_guess)

res = friedm(cipher_text, 6)
print(res)
