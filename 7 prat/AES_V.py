import struct

import numpy as np

# Initialize Parameters
p = 317
a, b = 13, 15
T = np.array([[1, 11], [31, 4]])
K = [[111, 289], [102, 251]]
C = [[28, 115, 243, 168], [91, 93, 210, 15], [13, 146, 279, 289], [141, 122, 114, 103], [275, 158, 152, 113],
     [146, 36, 46, 62], [84, 245, 121, 191], [193, 188, 62, 138], [0, 233, 61, 270], [8, 221, 308, 271],
     [236, 75, 279, 50], [124, 160, 300, 215], [227, 178, 194, 200], [208, 215, 86, 299], [3, 266, 76, 149],
     [89, 292, 84, 126], [138, 203, 48, 261], [87, 157, 225, 302], [49, 239, 138, 221], [90, 207, 26, 199],
     [218, 144, 35, 55], [1, 100, 304, 61], [74, 299, 41, 264], [152, 116, 216, 225], [166, 85, 192, 312],
     [15, 180, 254, 13], [275, 55, 52, 241], [138, 293, 223, 106], [71, 277, 56, 85], [266, 33, 224, 24],
     [42, 211, 162, 173], [28, 115, 243, 168], [288, 291, 12, 260], [113, 25, 183, 69], [257, 109, 287, 35],
     [174, 137, 267, 30], [257, 109, 287, 35]]


# Calculate determinant modulo p
def det_mod(matrix, mod):
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod


def inverse_matrix(T, p):
    det_t = (T[0][0] * T[1][1] - T[0][1] * T[1][0]) % p

    if det_t == 0:
        raise ValueError("Matrix is singular modulo p.")

    inv_det_t = pow(int(det_t), -1, p)

    adj_matrix = np.array([
        [T[1][1], -T[0][1]],
        [-T[1][0], T[0][0]]
    ])
    return (inv_det_t * adj_matrix) % p


def egcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, p):
    """Modular Inverse using Extended Euclidean Algorithm"""
    g, x, y = egcd(a, p)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % p


def generate_subkey(K, a, b, p):
    K11 = (K[1][1] + (a // K[0][0] + b)) % p
    K12 = (K[0][1] + K11) % p
    K21 = (K[1][0] + K11) % p
    K22 = (K[1][1] + K11) % p
    return [[K11, K12], [K21, K22]]


def I_layer_inv(matrix, a, b, p):
    for i in range(2):
        for j in range(2):
            if matrix[i][j] == 0:
                matrix[i][j] = b
            else:
                m_inv = modinv(matrix[i][j], p)
                matrix[i][j] = (a * m_inv + b) % p

    return matrix


def II_layer_inv(matrix):
    return [[matrix[0][0], matrix[0][1]], [matrix[1][1], matrix[1][0]]]


def III_layer_inv(matrix, T_inv):
    m_layer3 = []
    for i in range(2):
        m1_i = T_inv[0][0] * matrix[0][i] + T_inv[0][1] * matrix[1][i]
        m2_i = T_inv[1][0] * matrix[0][i] + T_inv[1][1] * matrix[1][i]
        m_layer3.append([m1_i, m2_i])
    return m_layer3


def IV_layer_inv(matrix, key):
    m11 = (matrix[0][0] - key[0][0]) % p
    m12 = (matrix[0][1] - key[0][1]) % p
    m21 = (matrix[1][0] - key[1][0]) % p
    m22 = (matrix[1][1] - key[1][1]) % p

    matrix = [[m11, m12], [m21, m22]]
    return matrix


def decrypt_block(cipher_block, subkeys):
    T_inv = inverse_matrix(T, p)
    for key in subkeys:
        # IV layer inverse
        m4 = IV_layer_inv(cipher_block, key)
    # III layer inverse
    m3 = III_layer_inv(m4, T_inv)
    # II layer inverse
    m2 = II_layer_inv(m3)
    # I layer inverse
    m1 = I_layer_inv(m2, a, b, p)

    return m1


def decrypt(cipher_text, subkeys):
    decrypted_text = []
    for cipher_block in cipher_text:
        m_block = decrypt_block(np.array(cipher_block).reshape(2, 2), subkeys)
        decrypted_text.append(m_block)
    return decrypted_text


# Generate all subkeys first
K1 = K
K2 = generate_subkey(K1, a, b, p)
K3 = generate_subkey(K2, a, b, p)
keys = [K1, K2, K3]
keys = [[k_elem[::-1] for k_elem in k] for k in keys]


# Decrypting the cipher text
decrypted_blocks = decrypt(C, keys)
print(decrypted_blocks)

# Convert the numbers to bytes
byte_data = b''.join(struct.pack('>H', num) for sublist in decrypted_blocks for pair in sublist for num in pair)

# Decode the bytes to get the string
# Assuming UTF-8 encoding, but you might need to adjust based on the actual encoding
text = byte_data.decode('utf-8', 'ignore')
print(text)


def encrypt_block(plain_block, subkeys):
    for key in subkeys:
        # I layer
        m1 = I_layer_inv(plain_block, a, b, p)
        # II layer
        m2 = II_layer_inv(m1)
        # III layer
        m3 = III_layer_inv(m2, T)
        # IV layer
        m4 = IV_layer_inv(m3, key)

    return m4


def encrypt(plain_text, subkeys):
    encrypted_text = []
    for plain_block in plain_text:
        c_block = encrypt_block(np.array(plain_block).reshape(2, 2), subkeys)
        encrypted_text.append(c_block)
    return encrypted_text


# Assuming the plain text blocks are the same as the C list for demonstration purposes
plain_blocks = C

# Encrypt the plain text blocks
encrypted_blocks = encrypt(plain_blocks, keys)
print("Encrypted blocks:", encrypted_blocks)

# Decrypt the cipher text blocks
decrypted_blocks = decrypt(encrypted_blocks, keys)
print("Decrypted blocks:", decrypted_blocks)
