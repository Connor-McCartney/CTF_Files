from Crypto.Util.number import getPrime, bytes_to_long, inverse, isPrime
from secret import flag

m = bytes_to_long(flag)

def getSpecialPrime():
    a = 2
    for i in range(40):
        a*=getPrime(20)
    while True:
        b = getPrime(20)
        if isPrime(a*b+1):
            return a*b+1


p = getSpecialPrime()
e1 = getPrime(128)
e2 = getPrime(128)
e3 = getPrime(128)

e = pow(e1,pow(e2,e3))
c = pow(m,e,p)

assert pow(c,inverse(e,p-1),p) == m

print(f'p = {p}')
print(f'e1 = {e1}')
print(f'e2 = {e2}')
print(f'e3 = {e3}')
print(f'c = {c}')