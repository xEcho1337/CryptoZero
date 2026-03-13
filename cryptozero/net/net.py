import socket
import sys
import threading
from typing import Optional

# TODO: improve this
class Netcat:
    """
    Simple wrapper for netcat-like connections.

    Methods:
    - `receive_until(delimiter: bytes) -> bytes`: read from the socket until the delimiter is found.
    - `send(data: bytes) -> None`: send data over the socket.
    """
    def __init__(self, host: str, port: int, timeout: float = 10.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock: Optional[socket.socket] = None

    def _connect(self) -> None:
        if self.sock is None:
            self.sock = socket.create_connection((self.host, self.port), self.timeout)
            assert self.sock is not None

    def send(self, data: bytes) -> None:
        """Send data to the remote service."""
        self._connect()
        self.sock.sendall(data)

    def send_line(self, data: bytes) -> None:
        self.send(data + b"\n")

    def send_after(self, delimiter: bytes, data: bytes) -> None:
        self.recv_until(delimiter)
        self.send(data)

    def send_line_after(self, delimiter: bytes, data: bytes) -> None:
        self.recv_until(delimiter)
        self.send_line(data)

    def recv_line(self) -> bytes:
        return self.recv_until(b"\n")

    def recv_all(self) -> bytes:
        self._connect()
        assert self.sock is not None

        data = b""
        while True:
            chunk = self.sock.recv(4096)
            if not chunk:
                break
            data += chunk
        return data

    def recv(self, n: int = 4096) -> bytes:
        self._connect()
        assert self.sock is not None
        return self.sock.recv(n)

    def recv_until(self, delimiter: bytes) -> bytes:
        self._connect()
        assert self.sock is not None

        buffer = b""
        while delimiter not in buffer:
            chunk = self.sock.recv(4096)
            if not chunk:
                break
            buffer += chunk

        return buffer

    def interactive(self):
        self._connect()
        assert self.sock is not None

        def recv_thread():
            assert self.sock is not None
            while True:
                data = self.sock.recv(4096)
                if not data:
                    break
                sys.stdout.buffer.write(data)
                sys.stdout.flush()

        t = threading.Thread(target=recv_thread, daemon=True)
        t.start()

        while True:
            data = sys.stdin.buffer.readline()
            if not data:
                break
            self.sock.sendall(data)

    def close(self) -> None:
        """Close the connection."""
        if self.sock:
            self.sock.close()
            self.sock = None
