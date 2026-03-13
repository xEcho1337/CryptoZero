import random
import time

from sympy import primitive_root

from cryptozero.utils.cryptomath import baby_step_giant_step
from utils.cryptomath import smooth_prime

def stress_test():
    p = smooth_prime(7, 40)
    g = primitive_root(p)
    order = p - 1
    x = random.randint(0, order - 1)

    b = pow(g, x, p)
    start = time.time()
    r = baby_step_giant_step(g, b, p, order)
    took = time.time() - start

    print(x)
    print(r)
    assert x == r
    print("Took:", (took * 1000), "ms")

if __name__ == "__main__":
    stress_test()