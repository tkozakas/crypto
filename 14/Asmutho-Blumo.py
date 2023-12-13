P = [36699211, 73398427, 146796817]
S = [27522574, 27522584, 27522547]

p = 18349601

N = P[0] * P[1] * P[2]

S_0 = S[0] * (N // P[0]) * (1 / (N // P[0]) % P[0])
S_1 = S[1] * (N // P[1]) * (1 / (N // P[1]) % P[1])
S_2 = S[2] * (N // P[2]) * (1 / (N // P[2]) % P[2])

S_atk = (S_0 + S_1 + S_2) % N

print(S_atk % p)
# https://sagecell.sagemath.org/
# 9174800
###################################

S_blum = S_atk % p
print("Asmutho-Blumo paslaptis: ", S_blum)

#Naudojam ta pati p (arba ne idk)
n = 5
t = 3
# t - 1 number taken at random
# pick a1, a2 yourself
a1 = 2277
a2 = 42859

a = S_blum + a1 * x + a2 * x^2

xi = [randint(1,p) for i in range(0,n)]
# xi = [3082453, 19799601, 12117386, 5245308, 10982651]
print("X_i: ", xi)

Si = [int(a(x=u))%p for u in xi]
print("S_i: ", Si)
