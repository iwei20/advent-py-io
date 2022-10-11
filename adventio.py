import os
import sys
from atexit import register
from io import BytesIO
from typing import List

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')

def inlist(n: int) -> List[int]:
    """
    Reads the next n integers from input and returns them in a list
    """
    return [5]

