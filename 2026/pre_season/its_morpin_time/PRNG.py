from Crypto.Util.number import bytes_to_long as b2l
from math import sqrt

# Helper function to convert bytes to binary array (1 extended)
def bytes2bin(b, n):
    b = b2l(b)
    bitN = lambda x, n: (x >> n) % 2 if x >> n != 0 else 1

    binArray = [bitN(b, i) for i in range(n)[::-1]]

    return binArray

# Used to generate next internal state from previous and the secret
def genNext(secret, n, prev):
    next = [0] * n

    for i in range(n):
        for j in range(n):
            next[i] ^= secret[i * n + j] & prev[j]

    return next


# Used to generate a number of size-bits
def genNumber(secret, seed, n, size):
    prng = []
    internalState = seed
    for _ in range(size):
        internalState = genNext(secret, n, internalState)
        prng.append(internalState[-1])

    return prng #sum([b << i for i, b in enumerate(prng)])


def main():

    # import the bytestring flag from flag
    from flag import flag
    from math import ceil
    n = ceil(sqrt(len(flag) * 8))
    secret = bytes2bin(flag, n ** 2)

    # Seeding
    from Crypto.Util.number import long_to_bytes as l2b
    from time import time
    from hashlib import sha512
    from math import ceil

    t = time()
    seed = b"redacted computation"
    seed = bytes2bin(seed, n)

    # Generating and printing a 1000-bit PRNG
    prng = genNumber(secret, seed, n, 1000)
    #print(f"{t}: {prng}")
    print(prng)

    exit(0)

if __name__=="__main__":
    main()
