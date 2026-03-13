import base64

def from_base64(s: str) -> bytes:
    return base64.b64decode(s)

def to_base64(b: bytes) -> str:
    return base64.b64encode(b).decode()