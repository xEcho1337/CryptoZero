from sympy import factorint
from utils.cryptomath import smooth_prime

if __name__ == '__main__':
    p = 7 # a small starting prime
    bits = 512 # we want a 512 bit bsmooth prime
    smooth = smooth_prime(p, bits)
    print("Smooth:", smooth)
    print("Bits:", smooth.bit_length())

    # check the small factors
    pm1 = factorint(smooth - 1)
    print("P-1 Factors:")
    for (x, e) in pm1.items():
        print(f"factor: {x}^{e}")