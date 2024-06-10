#!/usr/bin/env sage

import sys
from Crypto.Util.number import *
from hashlib import sha256
from flag import flag

def die(*args):
	pr(*args)
	quit()

def pr(*args):
	s = " ".join(map(str, args))
	sys.stdout.write(s + "\n")
	sys.stdout.flush()

def sc():
	return sys.stdin.buffer.readline()

def find_gen(p):
	while True:
		g = getRandomRange(2, p - 1)
		if pow(g, (p-1)//2 , p) != 1:
			return g

def main():
	border = "┃"
	pr(        "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
	pr(border, "Hi all, now it's time to solve a strange and unusual RSA and DLP    ", border)
	pr(border, "challenge about encryption! Follow the questions and find the secret", border)
	pr(border, "flag! :)                                                            ", border)
	pr(        "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
	nbit, b = 256, False
	while True:
		pr(f"| Options: \n|\t[G]et encrypted flag \n|\t[P]ublic parameters \n|\t[S]ubmit {nbit} primes \n|\t[Q]uit")
		ans = sc().decode().lower().strip()
		if ans == 'g':
			if b == True:
				l, n = len(flag), (p**2 - 1) * (q**2 - 1)
				gp, gq = find_gen(p), find_gen(q)
				sp, sq = getRandomRange(1, p), getRandomRange(1, q)
				flagp, flagq = flag[:l // 2], flag[l // 2:]
				yp, yq = pow(gp, sp, p), pow(gq, sq, q)
				cp, cq = pow(bytes_to_long(flagp), yp, n), pow(bytes_to_long(flagq), yq, n)
				pr(border, f'cp = {cp}')
				pr(border, f'cq = {cq}')
			else: pr(border, 'Please first send your primes! :P')
		elif ans == 's':
			pr(border, 'Send your desired prime numbers separated by comma: ')
			P = sc()
			try:
				p, q = P.split(b',')
				p, q = int(p), int(q)
			except: die(border, 'Your input are not integer! Bye!!')
			if p != q and isPrime(p) and isPrime(q) and p.bit_length() == q.bit_length() == nbit:
				b = True
				pr(border, 'Now you can get the encrypted flag in main menu!')
			else: die(border, 'Sorry, your integers are not valid :/')
		elif ans == 'p':
			if b == True:
				pr(border, f' gp = {gp}')
				pr(border, f' gq = {gq}')
				pr(border, f' yp = {yp}')
				pr(border, f' yq = {yq}')
			else: pr(border, 'Please first send your primes! :P')
		elif ans == 'q':
			die(border, 'Quitting...')
		else:
			die(border, 'You should select valid choice!')

if __name__ == '__main__':
	main()
