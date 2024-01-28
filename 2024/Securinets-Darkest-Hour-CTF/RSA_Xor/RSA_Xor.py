from Crypto.Util.number import *
import os
#Idea from mapna CTF but much simpler


def shift(s, B):
	assert s < len(B)
	return B[s:] + B[:s]

def gen_key(nbit):
	while True:
		p = getPrime(nbit)
		B = bin(p)[2:]
		for s in range(1, nbit):
			q = int(shift(s, B), 2)
			if isPrime(q):
				n = p * q
				return n, p, s
			
flag=os.environ.get('FLAG', 'FLAG{REDIRECT}').encode()
n,p,s=gen_key(1024)
q=n//p
e=0x10001
hint=p^q
c=pow(bytes_to_long(flag),e,n)
with open("output.txt",'w') as f:
    f.write(f"{c =}\n")
    f.write(f"{hint =}\n")
    f.write(f"{n =}\n")
    f.write(f"{e =}")
