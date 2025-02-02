import sys
import pwn
import pickle
import base64
import hashlib
import random
import numpy as np
from numpy._typing import NDArray
from gmpy2 import mpz
from typing import Any
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def mpow(a: NDArray[Any], e: int, p: mpz):
    n = a.shape[0]
    c: NDArray[Any] = np.identity(n, dtype=object) // mpz(1)
    for i in range(e.bit_length(), -1, -1):
        c = (c @ c) % p
        if e & (1 << i):
            c = (c @ a) % p
    return c


def dec(key: bytes, iv: bytes, ciphertext: bytes) -> str:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext.decode()


def main():
    r = pwn.remote(sys.argv[1], int(sys.argv[2]))
    r.send(base64.b64encode(b"g"))
    r.send(b"\r\n")

    msg = r.recv()
    p, g, gorder = pickle.loads(base64.b64decode(msg))
    print(gorder)
    a = random.randint(0, gorder)
    A = mpow(g, a, p)
    r.send(base64.b64encode(pickle.dumps(A)))
    r.send(b"\r\n")

    msg = r.recv()
    B, iv, cipher = pickle.loads(base64.b64decode(msg))

    K = mpow(B, a, p)
    h = hashlib.sha256()
    h.update(str(K).encode())
    digest = h.digest()
    print(dec(digest, iv, cipher))

    r.send(base64.b64encode(b"kthxbye"))
    r.send(b"\r\n")
    print(r.recv().decode("utf-8").strip()[::-1])


if __name__ == "__main__":
    main()
