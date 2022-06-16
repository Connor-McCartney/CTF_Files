from Crypto.Util.number import *
from random import randint, random
from secret import flag

l = len(flag)

m1 = bytes_to_long(flag[:l // 2])
m2 = bytes_to_long(flag[l // 2:])

n = 60
m = 330
p = getPrime(512)

G = random_matrix(GF(2), n, m)
bin_m1 = list(map(int, bin(m1)[2:]))
assert len(bin_m1) == 167
pad_m1 = bin_m1 + [randint(0,1) for i in range(m - len(bin_m1))]
G[randint(0, n-1)] = pad_m1
v = random_matrix(GF(p), 1, n)
G = G.change_ring(ZZ)
w = v * G


e = 0x10001
bin_m2 = list(map(int, bin(m2)[2:]))
assert len(bin_m2) == 167
pad_m2 = bin_m2 + [randint(0,1) for i in range(m - len(bin_m2))]
while 1:
    M = random_matrix(GF(2), m, m)
    M[randint(0, n-1)] = pad_m2
    if M.determinant() != 0:
        break
MM = M^e

print(f'p = {p}')
print(f'w = {list(w[0])}')
print(f'MM = {list(MM)}')