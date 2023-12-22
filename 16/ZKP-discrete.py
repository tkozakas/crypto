import hashlib

"""
38 assignment 
2. Find the discrete logarithm log_gy and publish the non-interactive proof, that you know the solution.

[g,y,p]=[2, 31945, 100003]
"""
[g,y,p]=[2, 80138, 100003]

# find x in discrete logarithm
# for i in range(p):
#    if power_mod(g,i,p)==y:
#        print(i)
x = 96389

v = 2288
t = power_mod(g, v, p)
# t = 87571

# 2 80138 77340
hr = b'280138100003'
h = hashlib.md5()
h.update(hr)
c=int(h.hexdigest(), 16) % (p - 1)
r = (v-c*x) % (p - 1)
Ats = [y,p, [c, r]]
print(Ats)

# [80138, 100003, [33576, 9950]]
