#!/usr/bin/env python3
for a in range(8):
    for b in range(a + 1, 10):
        print("{}{}".format(a, b), end=", ")
print("{}{}".format(8, 9))
