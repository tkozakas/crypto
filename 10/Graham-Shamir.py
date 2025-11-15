from math import gcd

#######################
# Step 1
####################

v1 = 40310731
p = 111359432

# Calculate the GCD to get the count of solutions
gcd_v1_p = gcd(v1, p)
print(gcd_v1_p)

#######################
# Step 2
#######################

w1n = 790699 // gcd_v1_p
v1n = v1 // gcd_v1_p
pn = p // gcd_v1_p


# Finding s such that v1n * s ≡ w1n (mod pn)
# s = w1n * v1n_inv (mod pn), where v1n_inv is the modular multiplicative inverse of v1n modulo pn

def modinv(a, m):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


v1n_inv = modinv(v1n, pn)
s = (w1n * v1n_inv) % pn
# Displaying the values for verification
print(s, w1n, v1n, pn)

#######################
# Step 3
#######################

# Given values
V = [40310731, 19636629, 104678516, 81836342, 28708722, 22819562, 33220570, 97479027]
C = [157535715, 244613734, 277834304, 221794172, 209063999, 104678516, 228971049, 306543026, 104678516, 147134707, 221794172, 209063999, 255014742, 244613734]

# Scale V and C with s modulo p
W = [(s * v) % p for v in V]
Cn = [(s * c) % p for c in C]

print(W, Cn)


#######################
# Step 4
#######################

def decrypt_knapsack(ciphertext, private_key):
    message = []
    for c in ciphertext:
        binary_number = []
        remaining_value = c
        for w in reversed(private_key):
            if remaining_value >= w:
                remaining_value -= w
                binary_number.insert(0, 1)
            else:
                binary_number.insert(0, 0)
        message.append(binary_number)
    return message


def binary_to_ascii(binary_message):
    return ''.join(chr(int(''.join(str(bit) for bit in bits), 2)) for bits in binary_message)


# Decrypt the modified ciphertext using the scaled private key
binary_message = decrypt_knapsack(Cn, W)
decrypted_message = binary_to_ascii(binary_message)

print(binary_message, '\n', decrypted_message)
