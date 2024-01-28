# rng 3
from random import Random,shuffle
import os

class Rng:
    def __init__(self):
        self.r1=Random()
        self.mask_bin=[1]*16+[0]*16
        self.flag=os.environ.get('FLAG', 'FLAG{REDIRECT}').encode()
    def rng(self):
        shuffle(self.mask_bin)
        mask=int("".join(str(i) for i in self.mask_bin),2)
        return self.r1.getrandbits(32)& mask,mask
    def xor(self,a,b):
        return bytearray([i^j for i,j in zip(a,b)])
    def encrypt(self):
        return self.xor(self.flag,bytes.fromhex(hex(self.r1.getrandbits(256))[2:])).hex()
Rng3=Rng()
while True:
        option=input("You can either encrypt the flag or get a leak")
        if option == "Leak":
            leak,mask=Rng3.rng()
            print(f"{leak=},{mask=}")
        elif option == "Encrypt":
            enc_flag=Rng3.encrypt()
            print(f"{enc_flag=}")
        elif option== "Exit":
            break
        else:
            print("Follow the order")


    
