#!/usr/bin/python3
print("".join(["{}".format(chr(i) if i % 2 == 1 else chr(i).upper()) for i in range(122, 96, -1)]), end="")
