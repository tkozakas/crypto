# by artem tretjakov :)
# https://sagecell.sagemath.org/?z=eJxNz-EKwiAQB_DvPsVBDBY7yNMiCHwCH0EkNjIaRpPpPuztuxZryX3xd6f-vYU72DBfU22xxW5_EcCrZ3TaGyMvEKXpFgzPHJZtbZ30Td0ePjNVarp9lbiWoUimjrKxjvyPFBMxqY00k2o-51caQ5nGF7goMRJGhVF7IW7feGs42MEwlTSVDOURIE9dDHOG-zBCX8LYln54ZVjus2T-__U1tRptuD5skdUqL5LRdBbcN6QR6CSscYQKNR450ZbmDePhUrk=&lang=sage&interacts=eJyLjgUAARUAuQ==
def Key_p(K, a, b, p):
    if K[3] == 0:
        k0 = b
    else:
        k0 = (K[0] + (a / K[3] % p + b) % p) % p
    k1 = (k0 + K[1]) % p
    k2 = (k1 + K[2]) % p
    k3 = (k2 + K[3]) % p
    return [k0, k1, k2, k3]


def Key(K, a, b, p):  # outputs the subkeys for iterations
    K1 = Key_p(K, a, b, p)
    K2 = Key_p(K1, a, b, p)
    return [K, K1, K2]


def inv(T, p):
    dt = 1 / (T[0] * T[3] - T[1] * T[2]) % p
    inv_T = [T[3], -T[1], -T[2], T[0]]
    inv_T = [dt * i % p for i in inv_T]
    return inv_T


def aes_decrypt(cipher, keys, t, a, b, p):
    out = []
    t = inv(t, p)
    for piece in cipher:
        for i in range(0, 3)[::-1]:
            key = keys[i]
            m4 = piece
            # IV layer
            m3 = [(m4[i] - key[i]) % p for i in range(0, 4)]
            # III layer
            m2 = [t[0] * m3[0] + t[1] * m3[2], t[0] * m3[1] + t[1] * m3[3], t[2] * m3[0] + t[3] * m3[2],
                  t[2] * m3[1] + t[3] * m3[3]]
            m2 = [m2[i] % p for i in range(0, 4)]
            # II layer
            m1 = [m2[0], m2[1], m2[3], m2[2]]
            # I layer
            piece = [a / (m1[i] - b) % p if m1[i] != b else 0 for i in range(0, 4)]
        out.append(piece)
    return out


def aes_encrypt(cipher, keys, t, a, b, p):
    out = []
    for piece in cipher:
        for i in range(0, 3):
            key = keys[i]
            m = piece
            # I layer
            m1 = [(a / m[i] + b) % p if m[i] != 0 else b for i in range(0, 4)]
            # II layer
            m2 = [m1[0], m1[1], m1[3], m1[2]]
            # III layer
            m3 = [t[0] * m2[0] + t[1] * m2[2], t[0] * m2[1] + t[1] * m2[3], t[2] * m2[0] + t[3] * m2[2],
                  t[2] * m2[1] + t[3] * m2[3]]
            # IV layer
            m4 = [(m3[i] + key[i]) % p for i in range(0, 4)]
            piece = m4
        out.append(piece)
    return out


def first():
    p = 317
    a, b = 13, 15
    T = [1, 11, 31, 4]
    K = [111, 289, 102, 251]
    C = [[28, 115, 243, 168], [91, 93, 210, 15], [13, 146, 279, 289], [141, 122, 114, 103], [275, 158, 152, 113],
         [146, 36, 46, 62], [84, 245, 121, 191], [193, 188, 62, 138], [0, 233, 61, 270], [8, 221, 308, 271],
         [236, 75, 279, 50], [124, 160, 300, 215], [227, 178, 194, 200], [208, 215, 86, 299], [3, 266, 76, 149],
         [89, 292, 84, 126], [138, 203, 48, 261], [87, 157, 225, 302], [49, 239, 138, 221], [90, 207, 26, 199],
         [218, 144, 35, 55], [1, 100, 304, 61], [74, 299, 41, 264], [152, 116, 216, 225], [166, 85, 192, 312],
         [15, 180, 254, 13], [275, 55, 52, 241], [138, 293, 223, 106], [71, 277, 56, 85], [266, 33, 224, 24],
         [42, 211, 162, 173], [28, 115, 243, 168], [288, 291, 12, 260], [113, 25, 183, 69], [257, 109, 287, 35],
         [174, 137, 267, 30], [257, 109, 287, 35]]

    out = aes_decrypt(C, Key(K, a, b, p), T, a, b, p)
    plaintext = ""
    for piece in out:
        for j in range(0, 4):
            plaintext += chr(piece[j])
    print(plaintext)


first()


def second():
    p = 317
    a, b = 13, 15
    T = [1, 11, 31, 4]
    M = [84, 208, 91, 262]
    C = [236, 228, 111, 296]

    guesses = []
    for i in range(0, 317):
        guesses.append(aes_encrypt([M], Key([i, 247, 144, 128], a, b, p), T, a, b, p)[0])
    for i in range(0, 317):
        decrypted = aes_decrypt([C], Key([229, i, 183, 254], a, b, p), T, a, b, p)[0]
        for j in range(0, 317):
            equal = True
            for k in range(0, 4):
                if decrypted[k] != guesses[j][k]:
                    equal = False
            if equal:
                print(j, i, decrypted)


second()
