import os
import sys
from parse import compile
from atexit import register
from collections import deque
from io import BytesIO
from typing import Generator, List
from typing_extensions import Self

class STDINStream:
    def __init__(self: Self):
        self.input_deque = deque()

    def next(self: Self) -> str:
        """
        Returns the next string token from stdin
        """
        if len(self.input_deque) <= 0:
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
    
def parse_example():
    """
    https://pypi.org/project/parse/
    Reads results: name|numbers|2 chars

    Consider search (looks for it), findall (all occurrences)
    """
    lines: List[str] = []
    with open("filename", "r") as fin:
        lines = fin.readlines()
    
    pattern = compile("{name:w}|{number:d}|{id:2.2w}")

    result: dict = {}
    for line in lines:
        print(line)
        line_result = pattern.parse(line.rstrip('\r\n'))
        result[line_result["name"]] = (line_result["number"], line_result["id"])
    return result

def input_example():
    """
    Reads 5 integers from stdin
    """
    cin = STDINStream()
    for i in cin.next_n_int(5):
        print(i)

if __name__ == "__main__":
    print(parse_example())
    input_example()