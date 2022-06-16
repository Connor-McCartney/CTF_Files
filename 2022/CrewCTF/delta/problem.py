from Crypto.Util.number import bytes_to_long, getRandomNBitInteger
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from flag import FLAG

key = RSA.generate(1024)
p = key.p
q = key.q
n = key.n
if p > q:
    p, q = q, p

e = key.e
cipher = PKCS1_OAEP.new(key=key,hashAlgo=SHA256)
c = bytes_to_long(cipher.encrypt(FLAG))

delta = getRandomNBitInteger(64)
x = p**2 + 1337*p + delta

val = (pow(2,e,n)*(x**3) + pow(3,e,n)*(x**2) + pow(5,e,n)*x + pow(7,e,n)) % n

print('n=' + str(n))
print('e=' + str(e))
print('c=' + str(c))
print('val=' + str(val))
