import numpy as np

code = [93, 238, 181, 138, 154, 213, 188, 5, 165, 252, 236, 220, 19, 250, 98, 46, 122, 41, 83, 9, 213, 129, 231, 121, 244, 48, 173, 186,
        130, 127, 168, 186, 109, 20, 175, 196, 198]

known_plaintext = "OF"


def shift(c, x1):
    bt = 0
    n = len(x1)
    x = [0] * n
    for j in range(0, n):
        bt += c[j] * x1[j]
    for j in range(1, n):
        x[j] = x1[j - 1]
    x[0] = bt % 2
    return x


def key(c, x, n):
    rk_bits = []
    for i in range(n):
        rk_bits.append(x[0])
        x = shift(c, x)
    return rk_bits


def enc(t, c, x):
    n = len(t)
    keystream_bits = key(c, x, 8 * n)
    decrypted_bytes = []
    for i in range(n):
        byte_keystream_bits = keystream_bits[i * 8:(i + 1) * 8]
        keystream_byte_val = int("".join(map(str, byte_keystream_bits)), 2)
        decrypted_bytes.append(t[i] ^ keystream_byte_val)
    return decrypted_bytes


def solve_linear_system(A, b):
    try:
        A_inv = np.linalg.inv(A)
        A_inv = (np.round(A_inv)).astype(int) % 2
        x = np.dot(A_inv, b) % 2
        return list(x)
    except np.linalg.LinAlgError:
        print("Error: The matrix is singular. Cannot solve the system.")
        return None


def find_lfsr_params(known_plaintext, ciphertext):
    pt_bytes = [ord(p) for p in known_plaintext]
    ct_bytes = ciphertext[:len(pt_bytes)]
    keystream_bytes = [p ^ c for p, c in zip(pt_bytes, ct_bytes)]
    keystream_bits = []
    for byte in keystream_bytes:
        keystream_bits.extend([int(bit) for bit in f'{byte:08b}'])

    print(f"Recovered first {len(keystream_bits)} keystream bits: {''.join(map(str, keystream_bits))}")

    L = 8
    A = []
    b = []
    for i in range(L):
        A.append(list(reversed(keystream_bits[i:i + L])))
        b.append(keystream_bits[i + L])

    A_matrix = np.array(A)
    b_vector = np.array(b)

    c_found = solve_linear_system(A_matrix, b_vector)

    if c_found is None:
        return None, None

    print(f"Found c = {c_found}")

    for i in range(256):
        x0_candidate = [int(bit) for bit in f'{i:08b}']
        test_keystream = key(c_found, x0_candidate, len(keystream_bits))

        if test_keystream == keystream_bits:
            x0_found = x0_candidate
            print(f"Found x0 = {x0_found}")
            return c_found, x0_found

    return c_found, None


if __name__ == "__main__":
    c_final, x0_final = find_lfsr_params(known_plaintext, code)

    if c_final and x0_final:
        decrypted_code = enc(code, c_final, x0_final)
        plaintext = "".join([chr(b) for b in decrypted_code])
        print(f"\nDecrypted Plaintext:\n{plaintext}")
