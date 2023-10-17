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
    det_t = int(round(np.linalg.det(T)))
    inv_det_t = pow(det_t, -1, p)
    sus_matrix = np.array(
        [
            [T[1][1], -T[0][1]],
            [-T[1][0], T[0][0]],
        ]
    )
    return (inv_det_t * sus_matrix) % p


# Generate Subkeys from initial key K
def generate_subkey(K, a, b, p):
    K00 = (K[1][1] + (a // K[0][0] + b)) % p
    K01 = (K[0][1] + K00) % p
    K10 = (K[1][0] + K00) % p
    K11 = (K[1][1] + K00) % p
    return [[K00, K01], [K10, K11]]


subkeys = generate_subkey(K, a, b, p)
print(subkeys)


def I_layer_inv(matrix, a, b, p):
    transformed_matrix = []
    for row in matrix:
        transformed_row = []
        for m in row:
            if m == 0:
                m_prime = b
            else:
                m_prime = (a * (1 / m) + b) % p
            transformed_row.append(m_prime)
        transformed_matrix.append(transformed_row)

    return transformed_matrix


def II_layer_inv(matrix):
    return [[matrix[0][0], matrix[0][1]], [matrix[1][1], matrix[1][0]]]


def III_layer_inv(matrix, T, i):



def IV_layer_inv(matrix, key, i):
    m11_new = (matrix[0][0] ** 3 + key[0][0] ** i) % p
    m12_new = (matrix[0][1] ** 3 + key[0][1] ** i) % p
    m21_new = (matrix[1][0] ** 3 + key[1][0] ** i) % p
    m22_new = (matrix[1][1] ** 3 + key[1][1] ** i) % p

    return [[m11_new, m12_new], [m21_new, m22_new]]


def decrypt_block(cipher_block, subkeys, T, i):
    m11 = T_inv[0][0]
    # IV layer inverse
    m = IV_layer_inv(cipher_block, subkeys, i)
    # III layer inverse
    m = III_layer_inv(m, T, i)
    # II layer inverse
    m = II_layer_inv(m)
    # I layer inverse
    m = I_layer_inv(m, a, b, p)
    return m


def decrypt(cipher_text, subkeys, T_inv):
    decrypted_text = []
    for i, cipher_block in enumerate(cipher_text):
        m_block = decrypt_block(np.array(cipher_block).reshape(2, 2), subkeys, T, i)
        decrypted_text.append(m_block)
    return decrypted_text


# Calculate inverse modulo p
def inverse_mod(num, mod):
    for i in range(1, mod):
        if (num * i) % mod == 1:
            return i
    return -1


# Calculating Inverse of T
T_inv = inverse_matrix(T, p)

# Decrypting the cipher text
decrypted_blocks = decrypt(C, subkeys, T_inv)
print(decrypted_blocks)
