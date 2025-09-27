from collections import Counter

abc = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = len(abc)

english_freqs = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228,
    'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025,
    'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 'P': 0.01929, 'Q': 0.00095, 'R': 0.05987,
    'S': 0.06327, 'T': 0.09056, 'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150,
    'Y': 0.01974, 'Z': 0.00074
}


def prepare(text):
    textn = u''
    for a in text:
        if a in abc:
            textn += a
    return textn.upper()


def vigenere_decrypt(ciphertext, key):
    ciphertext_clean = prepare(ciphertext)
    key_clean = prepare(key)
    plaintext = ""
    key_length = len(key_clean)
    key_shifts = [abc.index(k) for k in key_clean]

    for i, char in enumerate(ciphertext_clean):
        shift = key_shifts[i % key_length]
        char_index = abc.index(char)
        decrypted_char_index = (char_index - shift + n) % n
        plaintext += abc[decrypted_char_index]
    return plaintext


def get_index_of_coincidence(text):
    N = len(text)
    if N <= 1:
        return 0.0

    counts = Counter(text)
    numerator = sum(n * (n - 1) for n in counts.values())
    denominator = N * (N - 1)
    return numerator / denominator


def find_key_length(ciphertext, max_key_len=20):
    clean_text = prepare(ciphertext)
    best_len = 0
    closest_ic = 0.0

    print("--- Finding Key Length using Index of Coincidence ---")
    for length in range(1, max_key_len + 1):
        total_ic = 0.0
        for i in range(length):
            sub_text = clean_text[i::length]
            total_ic += get_index_of_coincidence(sub_text)

        avg_ic = total_ic / length
        print(f"Length {length:2d}: Average IC = {avg_ic:.4f}")

        if avg_ic > closest_ic:
            closest_ic = avg_ic
            best_len = length

    return best_len


def find_best_shift(column_text):
    best_shift = 0
    min_chi_squared = float('inf')

    for shift in range(n):
        shifted_text = ""
        for char in column_text:
            shifted_index = (abc.index(char) - shift + n) % n
            shifted_text += abc[shifted_index]

        counts = Counter(shifted_text)
        text_len = len(shifted_text)

        chi_squared = 0.0
        for char in abc:
            observed = counts.get(char, 0)
            expected = text_len * english_freqs[char]
            chi_squared += ((observed - expected) ** 2) / expected

        if chi_squared < min_chi_squared:
            min_chi_squared = chi_squared
            best_shift = shift

    return best_shift


cipher_text = u'''
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

probable_length = find_key_length(cipher_text)
print(f"\nMost probable key length is: {probable_length}\n")

clean_cipher = prepare(cipher_text)
columns = [clean_cipher[i::probable_length] for i in range(probable_length)]

key_start = ""
found_key = key_start

print("--- Finding Full Key ---")
for i in range(len(key_start), probable_length):
    best_shift = find_best_shift(columns[i])
    found_letter = abc[best_shift]
    found_key += found_letter
    print(f"Key letter for column {i + 1} is '{found_letter}' (shift {best_shift})")

print(f"\nThe full key is: {found_key}\n")

decrypted_message = vigenere_decrypt(cipher_text, found_key)
print("--- Decrypted Message ---")
print(decrypted_message)
