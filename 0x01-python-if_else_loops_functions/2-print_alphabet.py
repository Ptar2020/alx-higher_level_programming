#!/usr/bin/python3
'''
for a in "abcdefghijklmnopqrstuvwxyz":
'''
for letter in range(ord('a'), ord('z') + 1):
    print("{:c}" .format(letter), end="")
