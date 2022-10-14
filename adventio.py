from parse import compile
from collections import deque
from typing import Generator, List, Optional
from typing_extensions import Self

class IStream:
    def __init__(self: Self, filename: Optional[str] = None):
        self.input_deque = deque()
        self.finlines = None
        if filename is not None:
            with open(filename, "r") as fin:
                self.finlines = iter(fin.readlines())

    def next(self: Self) -> str:
        """
        Returns the next string token from stdin
        """
        if len(self.input_deque) <= 0:
            if self.finlines is not None:
                self.input_deque.extend(next(self.finlines).split())
            else:
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
        if self.finlines is not None:
            return next(self.finlines)
        return input()

    def all_lines(self: Self) -> List[str]:
        return list(self.finlines)

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
    lines: List[str] = IStream("filename").all_lines()
    
    pattern = compile("{name:w}|{number:d}|{id:2.2w}")

    result: dict = {}
    for line in lines:
        line_result = pattern.parse(line.rstrip('\r\n'))
        result[line_result["name"]] = (line_result["number"], line_result["id"])
    return result

def stdinput_example():
    """
    Reads 5 integers from stdin
    """
    cin = IStream()
    for i in cin.next_n_int(5):
        print(i)

def finput_example():
    """
    Reads 5 integers from a file
    """
    fin = IStream("integers")
    for i in fin.next_n_int(5):
        print(i)

if __name__ == "__main__":
    print(parse_example())
    finput_example()
    stdinput_example()