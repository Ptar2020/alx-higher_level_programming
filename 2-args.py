
m sys import argv





items = argv[1:]

count = 0

if len(items) > 1:

    print(f"{len(items)} arguments:")

    for item in items:

        count += 1

        print(f"{count}: {item}")

elif len(items) == 1:

    print(f"1 argument:\n1: {argv[1]}")

else:

    print(f"{len(items)} arguments.")





if __name__ == "__main__":

    argv


