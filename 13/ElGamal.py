# use https://sagecell.sagemath.org/
"""
Viešasis Algio ElGamalio schemos raktas parašų tikrinimui ir šifravimui:
[p,g,bt]=[4640650289117164100520051333566036654627, 2, 1992693858923651376328054503824000834941]
Algis pasirašė žinutę = reikalingas daiktas. Parašas:
[gamma, delta_1]=[2352678260890874438719533506720608205335, 3188028735963742252053276011648452325785]
Algis pasirašė žinutę = smagus darbas. Parašas:
[gamma, delta_2]=[2352678260890874438719533506720608205335, 4618608875897618257755710558749765290245]
"""
# Abecelej pabaigoj turi buti tarpas
A = 'abcdefghijklmnopqrstuvwxyz '


def i_skaiciu(text):
    t = ''
    for r in text:
        if r in A:
            ind = A.index(r) + 1
            if ind < 10:
                t = t + '0' + str(ind)
            else:
                t = t + str(ind)
    return int(t, 10)


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


M_1 = i_skaiciu('reikalingas daiktas')
M_2 = i_skaiciu('smagus darbas')

PubKey = [4640650289117164100520051333566036654627, 2, 1992693858923651376328054503824000834941]

p = PubKey[0]
g = PubKey[1]
beta = PubKey[2]

gamma = 2352678260890874438719533506720608205335
delta_1 = 3188028735963742252053276011648452325785
delta_2 = 4618608875897618257755710558749765290245

# Patikrinti ar parasas yra teisingas
print(power_mod(beta, gamma, p) * power_mod(gamma, delta_1, p) % p == power_mod(g, M_1, p))

# k(delta1 - delta2) = (m1 - m2) mod p

gcdNum = gcd(delta_1 - delta_2, p - 1)
print(gcdNum)
# gcd = 2

k_0 = ((M_1 - M_2) / (delta_1 - delta_2)) % ((p - 1) / gcdNum)
k_1 = k_0 + (p - 1) / 2

# Patikrinti kuris k tinka
print(power_mod(g, k_0, p) == gamma)

a = ((M_1 - k_0 * delta_1) / gamma) % (p - 1)
print(a)
# a = 490

# Patikrinti ar gautas private key a yra teisingas
print(power_mod(g, a, p) == beta)
