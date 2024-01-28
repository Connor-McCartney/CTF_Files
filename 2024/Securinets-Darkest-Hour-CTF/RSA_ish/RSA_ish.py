from Crypto.Util.number import  getPrime,bytes_to_long
import os
from random import  getrandbits

flag=os.environ.get('FLAG', 'FLAG{REDIRECT}').encode()
p=getPrime(1024)
q=getPrime(1024)
n=p*q
e=0x10001
hint=sum(p**i*2**(1024*i*2) for i in range(1,5))+getrandbits(1024)
c=pow(bytes_to_long(flag),e,n)
with open("output.txt",'w') as f:
    f.write(f"{c =}\n")
    f.write(f"{hint =}\n")
    f.write(f"{n =}\n")
    f.write(f"{e =}")
