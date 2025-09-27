abc = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = len(abc)


def prepare(text):
    text = text.upper()
    textn = u''
    for a in text:
        if a in abc:
            textn += a
    return textn


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
        if i < len(key):
            textc += abc[(abc.index(textn[i]) - keys[i]) % n]
        else:
            textc += abc[(abc.index(textn[i]) - abc.index(textn[i - len(key)])) % n]
    return textc


text = u'''
XEXIX LEIPA BNYZT CSLNS HIJLC 
ZFEJD NZWKN OLSDO CFPKH FXJDP 
NTSNU CZXFG MVVLJ BQIOD QBLMG 
LDDPN XZXJW GFSPZ QGWWA XYTPK 
TECIJ LEMEL XXEUR EEBGL VEXJU 
YJJXY OZURZ CBBLP OVJPY HHVWS 
YYKYA KYLNR HOGYI VUHOM VJZWI 
NGRBG MLIIZ VFZOZ ZKMXO KSRAR 
URUIY GNFAZ YVUDH ZQVFR UFQII 
TIRFT MQPZX MAHNH QIAZA AKVTH 
LTRZM ONXES GFLQL SZNET PNDYS 
ITQDL QBAYQ RCPRC JYCCR FQMEC 
GUHAE ENYZT SIVRG XJMIT XVYFQ 
HKJPH HFZCP UHQXU XMAXB MZUEK 
DQNZJ SQTVM POUTF ZTGMX XHGID 
VMAUA BNFEG S 
'''

print(Vigenere(text, u'DREAMS'))
