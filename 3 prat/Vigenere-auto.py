abc = u'AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ'
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
REEIA ĮRŽEŠ DCRTK ZŪVET GYČJM 
KUYEC ĄČUĄŽ ŠĄOAM ŠIŠDO JICŠZ 
GJZSJ ŲREŠĮ IĘŪZĮ ĮDĘTM EĄPZY 
MŽUPO DZOUI ČŽAĖI ITŠVĖ BŪĘLV 
ŽDĘĘD OŽŪOA ŲOTIA APĖJA IRJĘF 
OLPŲĘ CHVEK UČYĖI BESUC BĖEĄA 
RŲCRZ AHŪCJ PIKRS OPŽFC ĘOOJC 
SĘIĮD JLĘBS LĖLNČ NGCOZ PĘACH 
LŲRUĘ SLKRE ĮJĄČD EĘJLK SMZČL 
ĄLOEŲ ĄĘĘĮY MĘČĮA ĘZŠKĮ CNĮIĘ 
STĘEM ŠCOŪŪ ZFJFĄ GSVEZ SRVIĄ 
OŽĖCV ĮJOŪŠ FNDAŪ MABŽO NHENĘ 
HŽCSŲ AŽOOV ŠEMĖG LVOSĖ ŪDOČS 
ĮITET ĮNCĮŪ DĮŽAN ĖPTŽP NTPDJ 
CŠTĘL BSYHĘ BYŠBĄ ŲDUYM ŲILUL 
ZGĮ  
'''

print(Vigenere(text, u'LIESAS'))
