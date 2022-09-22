#!/usr/bin/python3
import sys
items = sys.argv[1:]
count = 0
if len(items) == 0:
    print(f"0 arguments.")
else:
    for item in items:  
        count += 1
        if len(items) > 1:
            print(f"{len(items)} arguments:")
        else:
            print(f"{len(items)} argument:")
        print(f"{count}: {item}")

# if __name__ == "__main__":
#     sys.argv