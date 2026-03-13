def from_int(i: int, length: int = None, byteorder: str = "big") -> bytes:
    # if length is not provided, compute the minimum required
    if length is None:
        length = (i.bit_length() + 7) // 8 or 1
    return i.to_bytes(length, byteorder)

def to_int(b: bytes, byteorder: str = "big", signed: bool = False) -> int:
    return int.from_bytes(b, byteorder, signed=signed)
