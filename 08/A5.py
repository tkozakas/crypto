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

ciphertext = [190, 132, 241, 115, 226, 220, 120, 141, 162, 196, 28, 227, 162, 112, 238, 28, 138, 0, 56, 228, 197, 195,
              190, 1, 80, 87, 137, 203, 126, 66, 251, 123, 37, 94, 37, 42, 137, 105, 149, 164, 212, 28, 231, 160, 105,
              250, 0, 156, 8, 57, 234, 201, 204, 164, 28, 84, 76, 150, 196, 123, 69, 252, 111, 47, 86, 57, 57, 152, 120,
              149, 189, 209, 20, 231, 162, 115, 242, 0, 149, 17, 36, 232, 203, 215, 190, 6, 88, 86, 155, 213, 123, 88,
              251, 121, 40, 78, 45, 49, 141, 122, 157, 188, 217, 14, 249, 162, 115, 242, 0, 143, 0, 35, 244, 217, 209,
              164, 26, 73, 64, 150, 219, 121, 94, 254, 121, 48, 82, 56, 57, 155, 120, 157, 162, 209, 16, 224, 177, 115,
              239, 18, 136, 2, 63, 242, 198, 215, 166, 14, 75, 76, 143, 209, 127, 78, 251, 121, 35, 82, 36, 57, 133,
              111, 149, 165, 215, 15, 232, 176, 97, 238, 0, 129, 4, 63, 244, 193, 205, 183, 26, 93, 92, 142, 215, 123,
              89, 254, 121, 54, 68, 51, 44, 129, 126, 129, 190, 220, 28, 249, 162, 114, 255, 18, 144, 4, 60, 230, 197,
              208, 185, 14, 88, 78, 147, 211, 123, 89, 254, 125, 47, 86, 35, 63, 132, 97, 128, 191, 197, 14, 243, 162,
              108, 232, 5, 143, 17, 63, 235, 199, 195, 164, 29, 76, 86, 140, 215, 123, 89, 247, 125, 40, 67, 43, 40,
              129, 98, 130, 184, 209, 20, 243, 182, 118, 238, 24, 147, 15, 55, 238, 218, 203, 190, 14, 80, 79, 155, 206,
              115, 71, 244, 117, 32, 88, 32, 57, 140, 111, 134, 186, 209, 15, 253, 162, 115, 235, 26, 129, 20, 37, 237,
              195, 209, 191, 6, 82, 86, 151, 223, 97, 88, 225, 125, 48, 90, 47, 54, 137, 103, 132, 176, 219, 4, 229,
              162, 105, 255, 18, 136, 6, 35, 241, 197, 208, 190, 26, 84, 81, 143, 205, 113, 66, 250, 111, 52, 69, 47,
              51, 145, 120, 157, 180, 196, 24, 250]


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
        R3 = ((R3 >> 1) & R3_MASK) | (t << 22)


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


coefficient_vector = 0x6CA4EC6D

possible_keys = generate_possible_keys(coefficient_vector)

# Decrypt using each possible key
decrypted_texts = []
for key in possible_keys:
    plaintext_bytes = decrypt(ciphertext, key, coefficient_vector)
    decrypted_texts.append("".join([chr(b) for b in plaintext_bytes]))

print(decrypted_texts)
