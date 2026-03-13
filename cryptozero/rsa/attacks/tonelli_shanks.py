from itertools import product
from math import prod
from sympy import sqrt_mod
from utils.cryptomath import crt

def roots_2k_mod(c: int, p: int, e: int) -> set[int]:
    if e <= 0 or (e & (e - 1)) != 0:
        raise ValueError("Exponent must be a power of 2")

    k = e.bit_length() - 1
    roots = {c}

    for _ in range(k):
        new = set()

        for r in roots:
            for s in sqrt_mod(r, p, all_roots=True):
                new.add(s)

        roots = new
    return roots

def tonelli_shanks_2k(c: int, primes: list[int], e: int) -> list[int]:
    roots = []
    results = []

    for p in primes:
        root = roots_2k_mod(c, p, e)
        roots.append(root)

    n = prod(primes)

    for residues in product(*roots):
        m, _ = crt(primes, residues)
        results.append(int(m) % n)

    return list(set(results))