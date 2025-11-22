# use https://sagecell.sagemath.org/
### 12.1
# Rabin cryptosystem decryption
p = 7588748953220563890867587
q = 7588748953220563890867991
n = p * q
c = 45928015850449628491166953201561651272471678808679
# Extended euclidean algorithm
# (y_p * p + y_q * q) = 1
# Calculated using https://www.dcode.fr/extended-gcd
y_p = -2798820777301643613216165
y_q = 2798820777301643613216016
m_p = power_mod(c, (p + 1) / 4, p)
m_q = power_mod(c, (q + 1) / 4, q)
r1 = ((y_p * p * m_q) + (y_q * q * m_p)) % n
r2 = n - r1
r3 = ((y_p * p * m_q) - (y_q * q * m_p)) % n
r4 = n - r3
# Convert to text
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
# wrinkled?in?deep?thought

### 12.2

"""
2. Privatusis Blumo-Goldwasserio  kriptosistemos raktas [p,q]=  [67807, 67819],h=8
Iššifruokite šifrą  
[178, 202, 247, 151, 157, 249, 254, 35, 95, 23, 112, 42, 16, 227, 246, 11, 1042529926]

Raidės keičiamos ASCII kodais. 
"""

p = 68659
q = 68683
n = p * q

h = 8

c = [88, 56, 96, 28, 129, 123, 106, 222, 97, 81, 230, 253, 24, 241, 253, 85, 18, 79, 73, 169, 71, 82, 24, 108, 27, 165, 166, 39]
x = 773789567
t = len(c)

# Calculate the extended GCD coefficients
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

gcd, r_p, r_q = extended_gcd(p, q)
print(f"r_p = {r_p}, r_q = {r_q}")

# For Blum-Goldwasser: compute x_0 from x_t
a = (p + 1) // 4
b = (q + 1) // 4
d_p = int(power_mod(a, t + 1, p - 1))
d_q = int(power_mod(b, t + 1, q - 1))

print(f"d_p = {d_p}, d_q = {d_q}")

u_p = power_mod(x, d_p, p)
u_q = power_mod(x, d_q, q)

print(f"u_p = {u_p}, u_q = {u_q}")

x_0 = (u_q * r_p * p + u_p * r_q * q) % n

print(f"x_0 = {x_0}")

X = [0] * (t + 1)
X[0] = x_0

M = [0] * t

for i in range(1, t + 1):
    X[i] = power_mod(X[i - 1], 2, n)
    p_i = X[i] % (2^h)  # Take the least significant h bits
    M[i - 1] = c[i - 1] ^^ p_i
    
print(f"M values: {M}")

decrypted = ""
for j in range(len(M)):
    if 0 <= M[j] <= 127:  # Valid ASCII range
        decrypted += chr(M[j])
    else:
        decrypted += f"[{M[j]}]"

print(decrypted)
# not a rebel barred their way
