from math import gcd

V = [47326013, 37958645, 2924510, 18411947, 26285773, 38443000, 19303439, 36724401]
p = 59423977

C = [16506041, 3457322, 57617564, 18183579, 55898965, 2924510, 16506041, 18183579, 19174564, 55898965, 18183579,
     55898965]

w1 = 388663
v1 = V[0]

if gcd(v1, p) == 1:
    s = (w1 * pow(v1, -1, p)) % p
else:
    s = w1 // v1 % p

W = [388663, 482536, 924725, 1852147, 3719254, 7388907, 14794987, 29576581]

Cn = [s * c % p for c in C]


def decrypt_knapsack(ciphertext, weights):
    message = []
    for c in ciphertext:
        binary_number = []
        for weight in reversed(weights):
            if c >= weight:
                c -= weight
                binary_number.append(1)
            else:
                binary_number.append(0)
        binary_number.reverse()
        message.append(binary_number)
    return message


def binary_to_ascii(binary_message):
    return ''.join(chr(int(''.join(str(bit) for bit in bits), 2)) for bits in binary_message)


binary_message = decrypt_knapsack(Cn, W)
decrypted_message = binary_to_ascii(binary_message)

print(decrypted_message)
# gyvas garsas
