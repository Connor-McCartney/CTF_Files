#!/usr/bin/env sage

from GPT import GPT6 # deep fake 
from Crypto.Util.number import *
from flag import flag

P = [GPT6('A 512-bit prime appears in consecutive digits of e') for _ in range(4)]
n, m = prod(P), bytes_to_long(flag)
c = pow(m, 0x10001, n)
print(f'n = {n}')
print(f'c = {c}')
