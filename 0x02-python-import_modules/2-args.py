#!/usr/bin/python3
import sys
items = sys.argv[1:]
if len(items) > 1:
    print(f"{len(items)} arguments.")
    count = 0
    for item in items:
        count += 1
        print(f"{count}: {item}")
elif len(items) == 1:
    print(f"{len(items)} argument.")

if __name__ == "__main__":
    sys.argv