def from_hex(s: str) -> bytes:
    s = s.strip().lower()
    if s.startswith("0x"):
        s = s[2:]
    # aggiungo uno zero se lunghezza dispari
    if len(s) % 2:
        s = "0" + s
    return bytes.fromhex(s)

def to_hex(b: bytes, prefix: bool = False) -> str:
    h = b.hex()
    return ("0x" + h) if prefix else h