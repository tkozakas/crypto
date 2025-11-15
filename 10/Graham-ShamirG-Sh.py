from math import gcd

# --- Provided values ---
v1 = 20176917094
p = 196299717268
w1 = 14161281118
V = [20176917094, 43017251388, 148335234986, 10070431054, 158867258548, 84641041942, 161989297456, 58406967673]
C = [437982825772, 408626712595, 434860786864, 434860786864, 334400495989, 275993528316, 148335234986, 506460224499, 408626712595, 286063959370, 350219744922, 148335234986, 286063959370, 350219744922, 334400495989, 148335234986, 363412214884, 334400495989, 353341783830, 334400495989, 434860786864, 421819182557]

##########
# Step 1: Handle the non-coprime case
##########
g = gcd(v1, p)
print(f"GCD(v1, p) = {g}")

# Scale down the numbers to work in a space where the modular inverse exists
v1n = v1 // g
w1n = w1 // g
pn = p // g

##########
# Step 2: Calculate the secret multiplier 's'
##########
def modinv(a, m):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y

    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# Find the modular inverse in the scaled-down space
v1n_inv = modinv(v1n, pn)
s = (w1n * v1n_inv) % pn
print(f"Secret multiplier s = {s}")

##########
# Step 3: Recover the private key and scale the ciphertext
##########
W = [(val * s) % p for val in V]
Cn = [(val * s) % p for val in C]

print(f"Recovered private key W = {W}")
print(f"Scaled ciphertext Cn = {Cn}")

##########
# Step 4: Extract the hidden message from the specified bits
##########
message = ""
for val in Cn:
    # Convert the number to a binary string, removing the '0b' prefix
    binary_val = bin(val)[2:]
    
    # Pad with leading zeros to ensure it's at least 19 bits long
    padded_binary = binary_val.zfill(19)
    
    # Extract the 8 bits from the 12th to 19th position from the end
    # This corresponds to the slice [-19:-11]
    message_bits = padded_binary[-19:-11]
    
    # Convert the 8 bits to an integer, then to an ASCII character
    message += chr(int(message_bits, 2))

print(f"Decrypted message: {message}")
