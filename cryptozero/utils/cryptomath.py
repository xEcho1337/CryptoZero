import sympy.ntheory.modular
from gmpy2 import is_prime, next_prime
from sympy import factorint, integer_nthroot

def egcd(a: int, b: int) -> tuple[int,int,int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def inverse(a: int, m: int) -> int:
    return pow(a, -1, m)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def ithroot(a: int, b: int) -> int:
    return integer_nthroot(a, b)

def crt(moduli: list[int], residues: list[int]) -> tuple[int, int] | None:
    return sympy.ntheory.modular.crt(moduli, residues)

def compute_phi(factors: list[int]):
    # TODO: add support for repeated factors
    x = 1
    for factor in factors:
        x *= factor - 1
    return x

def smooth_prime(starting: int, bits: int) -> int:
    if not is_prime(starting):
        raise ValueError("Starting value is not prime")

    pm1 = starting - 1
    factors = factorint(pm1)
    last = max(factors)

    while pm1.bit_length() < bits:
        last = next_prime(last)
        pm1 *= last

    k = 0
    while True:
        k += 1
        test = k * pm1 + 1
        if is_prime(test):
            return test