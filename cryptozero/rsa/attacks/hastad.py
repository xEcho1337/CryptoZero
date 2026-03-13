from utils.cryptomath import ithroot, crt

def hastad(e: int, ciphertexts: list[int], moduli: list[int]) -> int:
    if len(ciphertexts) != len(moduli):
        raise ValueError("Ciphertexts and moduli must have the same length")

    if len(ciphertexts) < e:
        raise ValueError(f"You need at least {e} ciphertexts")

    x, _ = crt(moduli, ciphertexts)
    m, exact = ithroot(x, e)

    if not exact:
        raise ValueError("Message is not an exact e-th power")

    return m