from random import choices
from Crypto.Util.number import getPrime,bytes_to_long
from math import gcd
class RSA:
    def __init__(self):
        self.primes=[getPrime(512) for i in range(20)]
        self.last_pub=1

    def encrypt(self,data):
        while True:
            p,q=choices(self.primes,k=2)
            n=p*q
            if gcd(n,self.last_pub)==1:
                break
                #No recycling
        self.last_pub=n
        return {"enc_data":pow(data,0x10001,n),"n":n}
flag=b"Securinets{REDIRECT}"
cipher=RSA()
with open("output.txt",'w') as f:
    for i in range(20):
        f.write(str(cipher.encrypt(bytes_to_long(flag)))+"\n")
