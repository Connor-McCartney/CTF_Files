import os
from pwn import xor
from speck import SpeckCipher

def F(block : bytes):
	return SpeckCipher(0x0123456789abcdef, key_size = 64, block_size = 32).encrypt(int.from_bytes(block, byteorder = 'big')).to_bytes(4, byteorder = 'big')

def encrypt(msg : bytes, k1 : bytes, k2 : bytes):
	msg += b'0' * ((4 - (len(msg) % 4)) % 4)
	return (b''.join(xor(k2, F(xor(msg[4*i:4*i+4], k1))) for i in range(len(msg) // 4))).hex()

if __name__ == '__main__':
	N = 1024
	k1 = os.urandom(4)
	k2 = os.urandom(4)
	flag = open('flag.txt','r').read().strip().encode()
	print(encrypt(flag, k1, k2))
	for _ in range(N):
		print('Please enter your chosen plaintext')
		try:
			user_input = input('> ')
			if user_input == 'exit': break
			assert len(user_input) == 8
			msg = bytes.fromhex(user_input)
			print(encrypt(msg, k1, k2))
		except:
			print('Could not get message')
