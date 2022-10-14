import os
import sys
import parse
from atexit import register
from collections import deque
from io import BytesIO
from typing import Generator
from typing_extensions import Self

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')

class STDINStream:
    def __init__(self: Self):
        self.input_deque = deque()

    def next(self: Self) -> str:
        """
        Returns the next string token from stdin
        """
        if self.input_deque.empty():
            self.input_deque.extend(input().split())
        return self.input_deque.popleft()     

    def next_int(self: Self) -> str:
        """
        Returns the next integer from stdin
        """
        return int(self.next())

    def next_float(self: Self) -> float:
        """
        Returns the next float from stdin
        """
        return float(self.next())

    def next_line(self: Self) -> str:
        """
        Discards progress on the current line, then consumes and returns the next line
        """
        self.input_deque.clear()
        return input()

    def next_n(self: Self, n: int) -> Generator[str, None, None]:
        """
        Reads the next n tokens from input and returns them in a generator
        """
        for _ in range(n):
            yield self.next()

    def next_n_int(self: Self, n: int) -> Generator[int, None, None]:
        """
        Reads the next n integers from input and returns them in a generator
        """
        for _ in range(n):
            yield self.next_int()
    
def _parse_example():
    pass