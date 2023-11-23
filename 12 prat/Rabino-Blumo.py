### 12.1
# use https://sagecell.sagemath.org/
"""
 15 užduotis
1. Rabin kriptosistemos privatusis raktas [p,q]=  [26623333280885244011, 26623333280885244047].
Iššifruokite  šifrą
409305196723890912810290354005744475541. Tekstas keičiamas skaičiumi kaip RSA užduotyje.
"""

p = 26623333280885244011
q = 26623333280885244047
n = p * q

c = 409305196723890912810290354005744475541

# Extended euclidean algorithm
# (y_p * p + y_q * q) = 1
# https://www.dcode.fr/extended-gcd
y_p = -739537035580145668
y_q = 739537035580145667

m_p = power_mod(c, (p + 1) / 4, p)
m_q = power_mod(c, (q + 1) / 4, q)

r1 = ((y_p * p * m_q) + (y_q * q * m_p)) % n
r2 = n - r1
r3 = ((y_p * p * m_q) - (y_q * q * m_p)) % n
r4 = n - r3

# Destytojo kodas
A = 'abcdefghijklmnopqrstuvwxyz'


def i_teksta(M):
    n = M
    text = ''
    while n > 0:
        ind = n % 100
        ind = ind - 1
        if (ind >= 0) & (ind < len(A)):
            text += A[ind]
            n = (n - ind + 1) // 100
        else:
            text += '?'
            n = (n - ind + 1) // 100
    return text[::-1]


print(i_teksta(r1))
print(i_teksta(r2))
print(i_teksta(r3))
print(i_teksta(r4))
# smagus?darbas

### 12.2

"""
2. Privatusis Blumo-Goldwasserio  kriptosistemos raktas [p,q]=  [67807, 67819],h=8
Iššifruokite šifrą  
[178, 202, 247, 151, 157, 249, 254, 35, 95, 23, 112, 42, 16, 227, 246, 11, 1042529926]

Raidės keičiamos ASCII kodais. 
"""

p = 67807
q = 67819
n = p * q

h = 8

c = [178, 202, 247, 151, 157, 249, 254, 35, 95, 23, 112, 42, 16, 227, 246, 11]
x = 1042529926
t = len(c)

d_p = ((p + 1) / 4) ^ (t + 1) % (p - 1)
d_q = ((q + 1) / 4) ^ (t + 1) % (q - 1)

u_p = x ^ d_p % p
u_q = x ^ d_q % q

# Extended euclidean algorithm
# r_p * p + r_q * q = 1
# https://www.dcode.fr/extended-gcd
r_p = -28258
r_q = 28253

x_0 = (u_q * r_p * p + u_p * r_q * q) % n

X = [0] * (t + 1)
X[0] = x_0

xorBits = "0b" + "1" * h

M = [0] * t

for i in range(1, t + 1):
    X[i] = (X[i - 1] ^ 2) % n
    p_i = bin(X[i] & int(xorBits, 2))
    M[i - 1] = int(c[i - 1]) ^^ int(p_i, 2)

decrypted = ""
for x in range(len(M)):
    decrypted += chr(M[x])

print(decrypted)
# rupesciai baigti