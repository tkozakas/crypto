# This does not work. Idk how to solve it.

ciphertext = [74, 158, 199, 241, 79, 23, 35, 170, 35, 71, 224, 105, 106, 216, 113, 18, 146, 125, 45, 57, 242, 226, 254, 27, 67, 126, 154,
              180, 213, 27, 4, 13, 41, 27, 147, 9, 39, 197, 201, 150, 221, 77, 100, 184, 157, 75, 133, 51, 241, 39, 83, 217, 146, 13, 19,
              241, 90, 18, 255, 166, 116, 237, 210, 221, 187, 230, 213, 252, 145, 110, 78, 195, 113, 120, 3, 154, 238, 64, 219, 166, 42,
              137, 125, 105, 227, 240, 236, 51, 99, 229, 8, 131, 51, 12, 94, 70, 186, 57, 64, 49, 247, 17, 96, 94, 9, 63, 230, 241, 25, 89,
              105, 151, 162, 203]

R1 = 0
R2 = 0
R3 = 0

R1_MASK = (1 << 19) - 1
R2_MASK = (1 << 22) - 1
R3_MASK = (1 << 23) - 1

# Correcting the TAP positions based on the provided information
R1_TAPS = 0x52000  # bits 18, 17, 16, 13
R2_TAPS = 0x300008  # bits 21, 20, 0
R3_TAPS = 0x500000  # bits 22, 21, 0

R1_CLOCK_BIT = 0x000100
R2_CLOCK_BIT = 0x000400
R3_CLOCK_BIT = 0x000400

def majority():
    count = 0
    if R1 & R1_CLOCK_BIT:
        count += 1
    if R2 & R2_CLOCK_BIT:
        count += 1
    if R3 & R3_CLOCK_BIT:
        count += 1
    return count >= 2


def clock():
    global R1, R2, R3
    maj = majority()
    if ((R1 & R1_CLOCK_BIT) != 0) == maj:
        t = bin(R1 & R1_TAPS).count('1') % 2
        R1 = ((R1 >> 1) & R1_MASK) | (t << 18)
    if ((R2 & R2_CLOCK_BIT) != 0) == maj:
        t = bin(R2 & R2_TAPS).count('1') % 2
        R2 = ((R2 >> 1) & R2_MASK) | (t << 21)
    if ((R3 & R3_CLOCK_BIT) != 0) == maj:
        t = bin(R3 & R3_TAPS).count('1') % 2
        R3 = ((R3 >> 1g) & R3_MASK) | (t << 22)


def keysetup(key, frame):
    global R1, R2, R3
    R1 = R2 = R3 = 0

    # Load the key into the registers
    for i in range(64):
        clockallthree()
        keybit = (key[i // 8] >> (i % 8)) & 1
        R1 ^= keybit
        R2 ^= keybit
        R3 ^= keybit

    # Load the frame number into the registers
    for i in range(22):
        clockallthree()
        framebit = (frame >> i) & 1
        R1 ^= framebit
        R2 ^= framebit
        R3 ^= framebit

    # Run the shift registers for 100 clocks for avalanche
    for i in range(100):
        clock()


def clockallthree():
    global R1, R2, R3
    # Clock R1
    t = bin(R1 & R1_TAPS).count('1') % 2
    R1 = ((R1 >> 1) & R1_MASK) | (t << 18)
    # Clock R2
    t = bin(R2 & R2_TAPS).count('1') % 2
    R2 = ((R2 >> 1) & R2_MASK) | (t << 21)
    # Clock R3
    t = bin(R3 & R3_TAPS).count('1') % 2
    R3 = ((R3 >> 1) & R3_MASK) | (t << 22)


def getbit():
    return (R1 ^ R2 ^ R3) & 1


def decrypt(ciphertext, key, frame):
    keysetup(key, frame)
    plaintext = []
    for byte in ciphertext:
        k = 0
        for _ in range(8):
            k = (k << 1) | getbit()
            clock()
        plaintext.append(byte ^ k)
    return plaintext


def generate_possible_keys(coefficient_vector):
    base_key = [coefficient_vector & 0xFF] * 8
    possible_keys = []
    for i in range(16):  # 2^4 = 16 possible keys
        key = base_key.copy()
        for j in range(4):
            key[j] = (key[j] & 0xFE) | ((i >> j) & 1)
        possible_keys.append(key)
    return possible_keys


# initial state from Exercise 1
# c = [0, 1, 1, 1, 0, 1, 1, 1]
# x0 = [0, 1, 1, 1, 0, 1, 1, 1]
c = [0, 1, 1, 1, 0, 1, 1, 1]
x0 = c[:]  # Initial state is the same as the coefficients

binary_string = "".join(map(str, c))
print(hex(int(binary_string, 2)))
coefficient_vector = 0x6CA4EC6D

possible_keys = generate_possible_keys(coefficient_vector)

# Decrypt using each possible key
decrypted_texts = []
for key in possible_keys:
    plaintext_bytes = decrypt(ciphertext, key, coefficient_vector)
    decrypted_texts.append("".join([chr(b) for b in plaintext_bytes]))

print(decrypted_texts)
