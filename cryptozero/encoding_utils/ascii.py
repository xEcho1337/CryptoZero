def from_ascii(s: str, encoding: str = "utf-8") -> bytes:
    return s.encode(encoding)

def to_ascii(b: bytes, encoding: str = "utf-8") -> str:
    return b.decode(encoding, errors="replace")