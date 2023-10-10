import Enigma_two_rotors

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
L_1 = [20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]
L_2 = [8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]
cText = '''
VQJMQ ESDKF QKBHM QVNBD LIXXS 
NTEYA AZYST FLSZX HUDMQ WIMZS 
TZSEK ISQCL YLIQK FSVCU SUMHJ 
KRUPW FVCAS EQTTL VFKMH RJOVU 
ZETZW MVRFK RJUUI IEWTQ JKWTA 
CWCJD FXYXS UTDFX RXKKQ FYXQV 
WHNGF IEHAP RXYLG TVEHZ DQXZT 
JQWML FMQZW YTZTH GHTAR ZPAIW 
KAJMO ZLNNC YPVQK JGDWN FDKZS 
MTLJD XZJYL BQXFP ZYIZZ CSXYZ 
GXJKJ BCIHL UTZHW VVALO IUBRB 
EABBL SGZGP AJMTM GGREX QXWDR 
SDRYO JLBFJ IHUZP QSMNH SYXGZ 
UOABC QTYGZ DREOH ODXZH PWHVM 
JEFIN UVUGM XXIKL YPYED USABQ 
ZQJUD GZVWN HHCVP NXRWF JVTRV 
RKNYG OVEQE TJOBQ XTQAX EDLHD 
FZVQT ASGWX XYPTN MFXBJ AUYAT 
NOB
'''
key = 11


def brute_force_second_key(key_part_1, L1, L2, cText_2):
    for key_part_2 in range(26):  # for each possible value of the second part of the key
        decrypted_text = Enigma_two_rotors.deEnigma([key_part_1, key_part_2], L1, L2, cText_2)
        if decrypted_text.startswith('U'):  # if the decryption starts with 'U'
            return decrypted_text, key_part_2


print(brute_force_second_key(11, L_1, L_2, cText))
