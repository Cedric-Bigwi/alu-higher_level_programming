#!/usr/bin/python3
print(*[chr(c).lower() if i % 2 == 0 else chr(c).upper() for i, c in enumerate(range(122, 96, -1))], sep="", end="")
