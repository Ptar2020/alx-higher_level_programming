#!/usr/bin/python3
import sys
items = sys.argv[1:]
count = 0
if len(items) > 1:
    print(f"{len(items)} arguments:")
    for item in items:
        count += 1
        print(f"{count}: {item}")
elif len(items) == 1:
    print(f"1 argument:\n1: {sys.argv[1]}" )
else:
    print(f"{len(items)} arguments.")
