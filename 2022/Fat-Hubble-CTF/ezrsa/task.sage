import os
from Crypto.Util.number import *
from secret import flag

p = getPrime(1024)
q = getPrime(512)
e = 0x10001
n = p * q
E = EllipticCurve(Zmod(n), [p+q, p^2+(q-1)//2])

def gen_point():
    while 1:
        pad_m = flag + os.urandom(20)
        m = bytes_to_long(pad_m)
        x = Integer(m)
        Ep = E.change_ring(GF(p))
        Eq = E.change_ring(GF(q))
        try:
            y = crt([Integer(Ep.lift_x(x)[1]), Integer(Eq.lift_x(x)[1])], [p, q])
            return (x, y)
        except:
            pass

m_point = E(gen_point())
cipher_point = e * m_point
print(f'cipher_point = {cipher_point.xy()}')
print(f'n = {n}')