import hashlib
from sage.all import *
"""
38 assignment 
1. Solve the congruence x^2=c mod p and publish the non-interactive proof, that you know the solution.
 
 [c,p]=[56623, 100003]
"""
[c, p] = [56623, 100003]

# p = 4k + 3
k = (p - 3) / 4
u = power_mod(c, k + 1, p)
# u = 58041

r_i = []
# while True:
#    randomNum = randint(2, p-1)
#    if gcd(randomNum, p) == 1:
#        r_i.append(randomNum)
#
#    if len(r_i) == 5:
#        break
r_i = [10484, 71082, 22059, 30311, 42059]

C = [c / power_mod(t, 2, p) % p for t in r_i]
U = [u * t % p for t in r_i]
print("C = ", C)
# C =  [21568, 286, 10025, 96915, 76235]

# i hr ideti C values be tarpu ir kabeliu
hr = b'21568286100259691576235'
h = hashlib.md5()
h.update(hr)
h_value = h.hexdigest()
print(bin(int(h_value[-2::], 16))[-5::])  # 5 least significant bits

bt = '01010'
Proof = [C, [r_i[0], U[1], r_i[2], U[3], r_i[4]]]
ats = [c, p, Proof]
print(ats)

# 11010
# [56623, 100003, [[21568, 286, 10025, 96915, 76235], [10484, 46597, 22059, 27975, 42059]]]
