from sympy import factorint, n_order
from sympy.ntheory.modular import crt
from tqdm import tqdm
from cryptozero.utils.cryptomath import baby_step_giant_step

def pohlig_hellman(g: int, h: int, p: int):
    n = n_order(g, p)
    factors = factorint(n)

    residues = []
    moduli = []

    for q, e in tqdm(factors.items(), desc="Searching Discrete Log"):
        x = 0

        for k in range(e):
            exp = n // (q ** (k + 1))

            g_k = pow(g, exp, p)
            gx = pow(g, x, p)
            inv = pow(gx, -1, p)

            t = pow((h * inv) % p, exp, p)

            d = baby_step_giant_step(g_k, t, p, q)

            if d is None:
                raise ValueError("log not found")

            x += d * (q ** k)

        residues.append(x)
        moduli.append(q ** e)

    return crt(moduli, residues)[0]