#!/usr/bin/env python3
import os
import sys
from Crypto.Util.number import bytes_to_long, getRandomNBitInteger
import math

flag = open('flag','r').read().strip()
N = 64

def log(*err_messages):
	'''function for debugging purposes'''
	logs = open('err.log','a')
	for msg in err_messages:
		if type(msg) == bytes: msg = hexlify(msg).decode()
		logs.write(msg)
	logs.write('\n=====\n')
	logs.close()

class CRG(object):
	"""Cubic Random Generator"""

	def __init__(self, n):
		'''n - bitlength of state'''
		self.n = n
		self.m = getRandomNBitInteger(n)
		while True:
			self.a = bytes_to_long(os.urandom(n >> 3)) % self.m # n/8 bytes
			if math.gcd(self.a, self.m) == 1: break
		while True:
			self.state = bytes_to_long(os.urandom(n >> 3)) % self.m # n/8 bytes
			if math.gcd(self.state, self.m) == 1: break
		self.buffer = []

	def next(self):
		if self.buffer == []:
			self.buffer = [int(bit) for bit in bin(self.state)[2:].zfill(self.n)]
			self.state = self.a * pow(self.state, 3, self.m) % self.m
			#log('new state: ', self.state)
		return self.buffer.pop(0)

def loop():
	balance = 2
	coin = ['head','tails']
	crg = CRG(N)
	while True:
		if balance == 0:
			print('I do not talk to broke people.')
			return
		if balance >= 1000000000:
			print(f'Wow, here is your flag: {flag}')
			return
		print(f'How much do you want to bet? (you have {balance})')
		sys.stdout.flush()
		amount = int(sys.stdin.buffer.readline().strip())
		if amount > balance or amount <= 0:
			print('Ugh, cheater!')
			return
		print('What is your bet?')
		sys.stdout.flush()
		bet = sys.stdin.buffer.readline().strip().decode()
		if bet == coin[crg.next()]:
			print('you win')
			balance += amount
		else:
			print('you lose')
			balance -= amount

if __name__ == '__main__':
	try:
		loop()
	except Exception as err:
		print('Something went wrong')
		log('ERROR: ', repr(err))
