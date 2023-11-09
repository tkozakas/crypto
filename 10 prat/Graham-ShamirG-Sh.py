from math import gcd

v1 = 81065661547
p = 96425213419
w1 = 11987976261
C = [60745877538, 17643778756, 31549010127, 2621429432, 31549010127, 76999285834, 74651108909, 33897187052, 90031265371, 7647628245, 60745877538, 18001585894, 46929166589, 90031265371]


##########
# Step 1
##########

# Calculate the GCD to find out if we need to adjust v1, w1, and p
gcd_value = gcd(v1, p)
print(gcd_value)


##########
# Step 2
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


# Calculate the scale factor s
s = modinv(v1, p) * w1 % p
print(s)

##########
# Step 3
##########
cn = [(c * s) % p for c in C]
print(cn)

##########
# Step 4
##########
ascii_characters = [chr(int(bin(c)[-18:-10], 2)) for c in cn]
print(ascii_characters)


