#!/usr/bin/env sage

import sys
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

def rand_utm(F, n):
	M = matrix(F, n, n)
	for i in range(n):
		for j in range(i, n):
			M[i,j] = F.random_element()
	return M

def upper(F, M):
	r, c = M.nrows(), M.ncols()
	_U = matrix(F, r, c)
	for i in range(r):
		_U[i, i] = M[i, i]
		for j in range(i + 1, c):
			_U[i, j] = M[i, j] + M[j, i]
	return _U

def genkey(q, m, d, u):
	n = m + d + u
	F = GF(q)
	O = random_matrix(F, u, m + d)
	c = O.ncols()
	I = identity_matrix(F, c)
	OI = block_matrix([[O], [I]])
	P = []
	for _ in range(m):
		A = rand_utm(F, u)
		B = random_matrix(F, u, m + d)
		C = O.transpose() * A * O + O.transpose() * B
		C = upper(F, C)
		D = matrix(F, m + d, u)
		Q = block_matrix([[A, B], [D, C]])
		P.append(Q)		
	return (O, OI), P

def iszero(M):
	F, r, c = M.base_ring(), M.nrows(), M.ncols()
	return matrix(F, r, c) == M

def n2F(n):
	z = GF(256).gen()
	G, g = bin(n)[2:].zfill(8), GF(256)(0)
	for i in range(8):
		g += int(G[i]) * z ^ (7 - i)
	return g

def compress(M):
	r, c = M.nrows(), M.ncols()
	_M = matrix(r, c)
	for i in range(r):
		for j in range(c):
			_M[i, j] = M[i][j].to_integer()
	return _M

def oracle(O) :
	F = O.base_ring()
	r, c = O.nrows(), O.ncols()
	n = r + c
	I = identity_matrix(F, c)
	OI = block_matrix([[O], [I]])
	U = matrix(F, n, 1)
	while(iszero(U)):
		V = random_matrix(F, c, 1)
		U = OI * V
	return U

def isequal(F, A, B):
	l, k = len(A), len(B)
	if l != k: return False
	n = A[0].nrows()
	for _ in range(l):
		V = random_matrix(F, n, 1)
		for _ in range(l):
			r = V.transpose() * A[_] * V
			s = V.transpose() * B[_] * V
			if r != s: return False
	return True

def verify(P, OI):
	r, c, F = P[0].nrows(), OI.ncols(), OI.base_ring()
	B, Z = [], []
	for _ in P:
		Z.append(matrix(F, c, c))
		B.append(OI.transpose() * _ * OI)
	return isequal(F, B, Z)

def main():
	border = "┃"
	pr(        "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
	pr(border, "  .: Welcome to VOROP oracle! Try to break this cryptosystem :.   ", border)
	pr(        "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
	q, m, d, u = 2**8, 38, 8, 86
	params = (q, m, d, u)
	F = GF(q)
	(O, OI), P = genkey(q, m, d, u)
	U = oracle(O)

	while verify(P, OI):	
		pr("| Options: \n|\t[G]et the parameters \n|\t[O]racle output \n|\t[P]ublic key \n|\t[V]erify \n|\t[Q]uit")
		ans = sc().decode().lower().strip()
		if ans == 'g':
			pr(border, f"The parameters are q, m, d, u = {q, m, d, u}")
		elif ans == 'o':
			pr(border, f"The oracle output U = {compress(U.transpose())}")
		elif ans == 'p':
			pr(border, f"Public key P is very large matrix, I will print row by row!")
			for p in P:
				_p = compress(p)
				for _r in _p:
					pr(border, f"{_r}")
				pr(border, "━" * 40)
			pr(border, "Done!")
		elif ans == 'v':
			pr(border, f"You should send a matrix with the appropriate size!")
			pr(border, f"So please send it row by row separated by comma ','")
			B = []
			for _ in range(m + d):
				pr(border, f"Send the row {_}:")
				_r = sc().decode().split(',')
				try:
					_r = [n2F(int(_)) for _ in _r]
					B.append(_r)
				except:
					die(border, f"The input you provided is is not valid!")
			_b, B = False, matrix(F, B)
			if B.ncols() == m + d + u:
				_b = verify(P, B.transpose()) and not B.is_zero()
				if _b:
					die(border, f'Congrats, you got the flag: {flag}')
				else:
					die(border, f'The provided matrix is not correct! Bye!!')
		elif ans == 'q':
			die(border, 'Quitting...')
		else:
			die(border, f"Your input does not meet the requirements!!!")

if __name__ == '__main__':
	main()
