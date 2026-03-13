from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot
from cryptozero.encoding_utils.int import to_int

def small_expo_attack(e: int, ciphertext: bytes) -> bytes | None:
    c = to_int(ciphertext)
    m, exact = iroot(c, e)

    if not exact:
        return None

    return long_to_bytes(m)
