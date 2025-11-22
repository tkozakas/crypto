import itertools

# =============== INPUTS ===============

CIPHERTEXT = [74, 158, 199, 241, 79, 23, 35, 170, 35, 71, 224, 105, 106, 216, 113, 18, 146, 125, 45, 57, 242, 226, 254, 27, 67, 126, 154, 180, 213, 27, 4, 13, 41, 27, 147, 9, 39, 197, 201, 150, 221, 77, 100, 184, 157, 75, 133, 51, 241, 39, 83, 217, 146, 13, 19, 241, 90, 18, 255, 166, 116, 237, 210, 221, 187, 230, 213, 252, 145, 110, 78, 195, 113, 120, 3, 154, 238, 64, 219, 166, 42, 137, 125, 105, 227, 240, 236, 51, 99, 229, 8, 131, 51, 12, 94, 70, 186, 57, 64, 49, 247, 17, 96, 94, 9, 63, 230, 241, 25, 89, 105, 151, 162, 203]

CONTROLS = [1, 2, 3]
# all valid coefficients you got from first exercise
COEFFS = [[0, 1, 1, 1, 0, 1, 1, 1]]

# ================ CODE ================

# converts a number d to the corresponding Unicode character
def number2letter (d):
    return chr (d)

# converts a letter c to the number representing the Unicode code of c
def letter2number (c):
    return ord (c)

# XORs two vectors a and b. Used in add_to_rows ()
def xor (a, b):
    m = min (len(a), len(b))
    return [(a[i] + b[i]) % 2 for i in range (m)] 	

# XORs the i-th row of M to the rows whose indices are specified in the list rows
def add_to_rows (M, i, rows):
    for j in rows:
        M[j] = xor (M[i], M[j])
    #for j in range(len(M)):
    #    print (M[j])
    return M  

# exchanges i-th and j-th rows of the matrix M
def exchange (M, i, j): 
    tmp = M[i]
    M[i] = M[j]
    M[j] = tmp
    return M

# shifts the LFSR with coefficients c and initial state x, where len(c) = len(x). Used in stream ()
def shift (c, x): 
    bt = 0
    n = len (x)
    xf = [0] * n
    for j in range (n):
        bt += c[j] * x[j]
    for j in range (1, n):
        xf[n-j] = x[n-1-j]
    xf[0] = bt % 2
    return xf 

def majority(b1, b2, b3):
    return (b1 & b2) | (b1 & b3) | (b2 & b3)

def decrypt(c, x0, control, cipher):
    x1 = [0] * 8
    x2 = [0] * 8
    x3 = [0] * 8
    for i in range (8):
        x1[i] = x0[i]
        x2[i] = x0[i]
        x3[i] = x0[i]

    s=''
    for ci in cipher:
        v = 0
        for j in range(8):
            key_bit = x1[0] ^ x2[0] ^ x3[0]
            
            v = v << 1
            v = v | key_bit
            
            m = majority(x1[control[0]], x2[control[1]], x3[control[2]])
            
            if x1[control[0]] == m:
                x1 = shift(c, x1)
            if x2[control[1]] == m:
                x2 = shift(c, x2)
            if x3[control[2]] == m:
                x3 = shift(c, x3)
        s += chr(ci ^ v)
    return s

def is_readable(text):
    """Check if text is readable ASCII"""
    return all(32 <= ord(c) <= 126 for c in text)

for p in COEFFS:
    decrypted = decrypt(p, p, CONTROLS, CIPHERTEXT)
    print(decrypted)
