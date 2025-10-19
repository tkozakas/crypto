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
    K = [184, 262, 165, 125]
    C = [[179, 205, 179, 10], [189, 81, 17, 231], [16, 237, 300, 113], [167, 138, 88, 160], [16, 257, 282, 120], [78, 16, 129, 77],
         [181, 71, 19, 303], [96, 178, 80, 200], [102, 263, 71, 58], [119, 13, 2, 242], [148, 312, 302, 277], [16, 240, 315, 177],
         [4, 125, 161, 29], [313, 13, 257, 208], [32, 35, 65, 104], [58, 94, 112, 244], [209, 154, 36, 60], [78, 16, 129, 77],
         [181, 71, 19, 303], [260, 272, 45, 242]]

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
    M = [104, 107, 113, 146]
    C = [32, 88, 73, 22]

    guesses = []
    for i in range(0, 317):
        guesses.append(aes_encrypt([M], Key([i, 220, 199, 281], a, b, p), T, a, b, p)[0])
    for i in range(0, 317):
        decrypted = aes_decrypt([C], Key([165, i, 187, 286], a, b, p), T, a, b, p)[0]
        for j in range(0, 317):
            equal = True
            for k in range(0, 4):
                if decrypted[k] != guesses[j][k]:
                    equal = False
            if equal:
                print(j, i, decrypted)


second()

p = 317
a, b = 13, 15
T = [1, 11, 31, 4]
C = [32, 88, 73, 22]
K2 = [165, 258, 187, 286]

round_keys_K2 = Key(K2, a, b, p)
intermediate_block = aes_decrypt([C], round_keys_K2, T, a, b, p)

print("Intermediate Block (Decrypted with K2):")
print(intermediate_block)

cipher_to_decrypt_with_K1 = intermediate_block[0]
K1 = [243, 220, 199, 281]

round_keys_K1 = Key(K1, a, b, p)
original_message_M = aes_decrypt([cipher_to_decrypt_with_K1], round_keys_K1, t, a, b, p)

print("\nOriginal Message (Decrypted with K1):")
print(original_message_M)