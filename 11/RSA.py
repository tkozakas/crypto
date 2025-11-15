# Extended Euclidean Algorithm for modular inverse and common modulus attack
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Modular inverse function
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

alphabet = 'abcdefghijklmnopqrstuvwxyz '

def text(decrypted_message):
    str_decrypted_message = str(decrypted_message)
    if len(str_decrypted_message) % 2 != 0:
        str_decrypted_message = '0' + str_decrypted_message
    decoded_numbers = [int(str_decrypted_message[i:i + 2]) for i in range(0, len(str_decrypted_message), 2)]
    decoded_message = ''.join([alphabet[number - 1] for number in decoded_numbers])
    return decoded_message

def rsa_decrypt(ciphertext, d, n):
    return pow(int(ciphertext), d, n)

# 1. Decrypt with your private key
n1 = 2427260695686584206173045201794179672098358307
d1 = 1255479670182715968710144672116451937106750229
c1 = 445838532830798612980980393957017822611506108

decrypted_message_1 = rsa_decrypt(c1, d1, n1)
print('1 ', text(decrypted_message_1))

# 2. Decrypt Alice's ciphertext
n2 = 2427260695686584206173045201794179672098358307
e2 = 103
c2 = 1316309421024997507597486442712938157136125176

# Calculate D the modular inverse e^-1 mod φ(N)
# p, q = https://www.alpertron.com.ar/ECM.HTM
p2 = 45562553508503809203409
q2 = 53273148864089882771123
phi2 = (p2 - 1) * (q2 - 1)

d2 = modinv(e2, phi2)
decrypted_message_2 = rsa_decrypt(c2, d2, n2)
print('2 ', text(decrypted_message_2))

# 3. Common Modulus Attack
n3 = 255017358220791952773507389921
e_bob = 25
c_bob = 96843450711780239488117557578
e_oscar = 49
c_oscar = 175983282686899042148162504713

g, a, b = egcd(e_bob, e_oscar)
c_oscar_inv = modinv(c_oscar, n3)
term1 = pow(c_bob, a, n3)
term2 = pow(c_oscar_inv, -b, n3)
decrypted_message_3 = (term1 * term2) % n3
print('3 ', text(decrypted_message_3))
