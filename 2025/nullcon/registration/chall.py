#!/bin/python3
from hashlib import sha256
from secret import flag
from Crypto.Util import number
import math
import os

BITS = 1024

class Pubkey(object):
	def __init__(self, n, e, a):
		self.n = n
		self.a = a
		self.e = e

	def verify(self, msg, s):
		if type(msg) == str: msg = msg.encode()
		h = number.bytes_to_long(sha256(msg).digest())
		return pow(s,self.e,self.n) == pow(self.a, h, self.n)

	def __str__(self):
		return f'n = {self.n}\na = {self.a}\ne = {self.e}'

class Key(Pubkey):
	def __init__(self, bits):
		self.p = number.getPrime(bits >> 1)
		self.q = number.getPrime(bits >> 1)
		self.n = self.p * self.q
		phi = (self.p - 1) * (self.q - 1)
		while True:
			e = number.getRandomInteger(bits)
			if math.gcd(e, phi) == 1: break
		self.e = e
		self.d = number.inverse(e, phi)
		while True:
			a = number.getRandomInteger(bits)
			if math.gcd(a, self.n) == 1: break
		self.a = a

	def sign(self, msg):
		if type(msg) == str: msg = msg.encode()
		h = number.bytes_to_long(sha256(msg).digest())
		return pow(self.a, h * self.d, self.n)

	def public(self):
		return Pubkey(self.n, self.e, self.a)

	def __str__(self):
		return f'n = {self.n}\na = {self.a}\ne = {self.e}\np = {self.p}'

if __name__ == '__main__':
	key = Key(BITS)
	print(key.public())
	while True:
		print('''Welcome to our conference reception. Can you provide a valid signature to confirm that you are alowed to participate? If not, please be patient and let the next person in the queue go fist.
		1) wait
		2) sign''')
		option = int(input('> '))
		if option == 1:
			challenge = os.urandom(BITS >> 3)
			signature = key.sign(challenge)
			print(f'Challenge: {challenge.hex()}')
			print(f'Signature: {signature}')
		elif option == 2:
			challenge = os.urandom(BITS >> 3)
			print(f'Challenge: {challenge.hex()}')
			signature = int(input('Signature: '))
			if key.verify(challenge, signature):
				print(flag)
			else:
				print('YOU SHALL NOT PASS!')
				break
		else:
			print('Invalid answer')
			break

