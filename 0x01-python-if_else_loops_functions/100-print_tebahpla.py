#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c)) if c % 2 == 0
          else "{}".format(chr(c).upper()), end="")
