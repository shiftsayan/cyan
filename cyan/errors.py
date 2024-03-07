import sys


class CyanError(Exception):
    def __init__(self, message):
        print(f"CyanError: {message}", file=sys.stderr)
        super().__init__(message)
