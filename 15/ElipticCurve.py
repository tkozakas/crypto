from sage.all import *

"""
4 assignment 
1. Given the elliptic curve G = EllipticCurve(GF(3001),[-7,2]) and the point P[21 : 2819] of prime order p=509.

The private key of Menezes-Vanstone cryptosystem is r=158.
Decrypt the cipher 

[[[966, 617], 406, 41], [[1123, 210], 245, 483], [[1783, 2805], 259, 355], [[1304, 675], 409, 27], [[2268, 1310], 228, 333], [[681, 2922], 266, 201], [[536, 803], 400, 288]]
 2. Sign the message m=100 using El Gamal signature with the elliptic curve and the private key given.
"""
r = 158
E = EllipticCurve(GF(3001), [-7, 2])
P = E([21, 2819])
p = 509

C = [[[966, 617], 406, 41], [[1123, 210], 245, 483], [[1783, 2805], 259, 355], [[1304, 675], 409, 27],
     [[2268, 1310], 228, 333], [[681, 2922], 266, 201], [[536, 803], 400, 288]]
answer = ""

for (C_0, C_1, C_2) in C:
    out = E(C_0) * r
    [x, y] = [int(out[0]), int(out[1])]
    Md = [(C_1 / x) % p, (C_2 / y) % p]
    answer += chr(Md[0])
    answer += chr(Md[1])

print(answer)


def f(t):
    return int(t[0])


M = 100
N = P.order()
# N = 509
k = 23
# gcd(k, N) == 1
R = k * P


def f(t):
    return int(t[0])


Sig = [R, (int(M - r * f(R)) / k) % N]
print(Sig)

# Patikrinimui
# K_v = r * P
# Rd=Sig[0]
# sd=Sig[1]
# V1=f(Rd) * K_v + sd * Rd
# V2=M*P
# V1==V2, V1
