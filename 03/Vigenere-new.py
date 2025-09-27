abc = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = len(abc)


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


cipher_text = u'''
WPKIY PGVTI STRAZ DTSPB GGHAG 
SNIPE WPXEE QKTHR FKRWU WELAC 
FGZIB IUPYC FGTAE SFOEL YGTTB 
BREPR FVEPR WUGOZ PKREQ QJERN 
QVIRO MELAE OEXEE KKXHG VGTLN 
WPXEK HOISF OIITB DTSDH QGXHR 
QATHR FVIXG HJMSY SFXOG VGHEI 
SNSPZ SPXOS SNICG FQQEP VCRIP 
ONHEI WEISN GEMPU STQAP VKREF 
OPHTB HJIOA ZAYNO FGEKN PNICV 
DJIRG VGSNR HKQEC OFFYJ CTPDJ 
OTMIZ SELAA WEELN BFILR QVVOZ 
SELAA WEELP WRLEE ACGHV BGWWR 
FGMNJ WFIUF SCPTU CWKHJ VGVEF 
IELMN QJMNR GYIRR WOTRN QVMCN 
ZOENH ONWYF HGQSP CPXIA IGHIA 
IUIGE SCXAQ JCRCR GYIRR ACHEV 
BDSTU QKTHR FFISV UPENQ QTCPG 
OPELL GKWAY ZKRSR QTICL WPJOE 
ACXIB BCFOH HVLIF DGVIB RJESO 
SIYNG CDIDR QNESF WHMEQ OUXHR 
CHJIP WCPBE WVMSU MGERF SEVEP 
MRIRV CFLAF QQQEG CCREA RCWUF 
OTGHV JGWHN JGWLB KNCOC SPIDN 
BFESN GUSRG SFQEZ CKVSN BFERG 
WEPEF VCZEN DRIAE SF
'''

key = "OCE"

decrypted_message = vigenere_decrypt(cipher_text, key)

print(decrypted_message)
