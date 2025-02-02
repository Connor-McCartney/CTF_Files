from Crypto.Util import number

def nextprime(n):
	p = n
	while True:
		if number.isPrime(p := p+1): return p

p = number.getPrime(512)
q = nextprime(p)
r = nextprime(q)
n = p*q*r
e = 0x10001
flag = int.from_bytes(open('flag.txt','r').read().encode())
c = pow(flag,e,n)
print(n)
print(c)
