# 1 https://www.dcode.fr/rsa-cipher :)
# RSA keys
n = 1800927138376531785763511974731548192529993897418304343019
d = 939614159152973105615745378042296163324018046115820473927
ciphertext = 1086817976482773165666845201202816048345044212262253850620
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def text(decrypted_message):
    str_decrypted_message = str(decrypted_message)
    decoded_numbers = [int(str_decrypted_message[i:i + 2]) for i in range(0, len(str_decrypted_message), 2)]
    decoded_message = ''.join([alphabet[number - 1] for number in decoded_numbers])
    return decoded_message


def rsa_decrypt(ciphertext, d, n):
    if isinstance(ciphertext, str):
        ciphertext = int(ciphertext)
    message = pow(ciphertext, d, n)
    return message


decrypted_message = rsa_decrypt(ciphertext, d, n)
print('1 ', text(decrypted_message))

# 2
# Calculate D the modular inverse e^-1 mod φ(N)
# p, q = https://www.alpertron.com.ar/ECM.HTM
p = 13109994191499930367061460439
q = 137370551967459378662586974221

n = 1800927138376531785763511974731548192529993897418304343019
e = 91
ciphertext = 961306378227779263829185163505609972462635040223519766263
# ϕ(n) = (p - 1) * (q - 1)
phi = (p - 1) * (q - 1)


def modinv(e, phi):
    d_old = 0
    r_old = phi
    d_new = 1
    r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None


d = modinv(e, phi)
decrypted_message = rsa_decrypt(ciphertext, d, n)
print('2 ', text(decrypted_message))

# 3
# Antano
n1 = 1800927138376531785763511974731548192529993897418304343019
e1 = 47
ciphertext1 = 412548281771198182325018785756136892751961464310158446849
p1 = 13109994191499930367061460439
q1 = 137370551967459378662586974221
phi1 = (p1 - 1) * (q1 - 1)

d1 = modinv(e1, phi1)
decrypted_message1 = rsa_decrypt(ciphertext1, d1, n1)
print('3 ', text(decrypted_message1))

# Birutės
n2 = 1800927138376531785763511974731548192529993897418304343019
e2 = 103
ciphertext2 = 823128164753999564806901782748659675357488851956293047071
p2 = 13109994191499930367061460439
q2 = 137370551967459378662586974221
phi2 = (p2 - 1) * (q2 - 1)

d2 = modinv(e2, phi2)
decrypted_message2 = rsa_decrypt(ciphertext2, d2, n2)
print('3 ', text(decrypted_message2))
