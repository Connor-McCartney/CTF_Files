# rng 5
from random import Random,shuffle
import os

class Rng:
    def __init__(self):
        self.r1=Random()
        self.flag=os.environ.get('FLAG', 'FLAG{REDIRECT}').encode()
    def rng(self):
        return "".join([str(self.r1.getrandbits(1)) for i in range(128)]) 
    def xor(self,a,b):
        return bytearray([i^j for i,j in zip(a,b)])
    def encrypt(self):
        return self.xor(self.flag,bytes.fromhex(hex(self.r1.getrandbits(256))[2:])).hex()

Rng5=Rng()
while True:
        option=input("You can either encrypt the flag or get a leak")
        if option == "Leak":
            leak=Rng5.rng()
            print(f"{leak=}")
        elif option == "Encrypt":
            enc_flag=Rng5.encrypt()
            print(f"{enc_flag=}")
        elif option== "Exit":
            break
        else:
            print("Follow the order")
