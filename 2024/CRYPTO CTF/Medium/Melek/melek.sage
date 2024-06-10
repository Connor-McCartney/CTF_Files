#!/usr/bin/env sage

from Crypto.Util.number import *
from flag import flag

def encrypt(msg, nbit):
	m, p = bytes_to_long(msg), getPrime(nbit)
	assert m < p
	e, t = randint(1, p - 1), randint(1, nbit - 1)
	C = [randint(0, p - 1) for _ in range(t - 1)] + [pow(m, e, p)]
	R.<x> = GF(p)[]
	f = R(0)
	for i in range(t): f += x**(t - i - 1) * C[i]
	P = [list(range(nbit))]
	shuffle(P)
	P = P[:t]
	PT = [(a, f(a)) for a in [randint(1, p - 1) for _ in range(t)]]
	return e, p, PT

nbit = 512
enc = encrypt(flag, nbit)
print(f'enc = {enc}')
