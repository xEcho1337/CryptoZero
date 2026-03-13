import urllib.parse

def from_url(s: str) -> bytes:
    # url-unquote restituisce string, lo encodo in utf-8
    return urllib.parse.unquote_to_bytes(s)

def to_url(b: bytes) -> str:
    return urllib.parse.quote_from_bytes(b)