#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 21/10/2026
# Purpose: Write data to a file.
# Usage: ./lab5b.py

# TO DO 1: Paste the code provided in readme.md file.
f = open('fruits.txt', 'w')
f.write('1. Apples are crunchy.\n2. Oranges are sweet, sour and juicy.\n3. Strawberries are sweet.\n4. Which fruit do you like?')
f.close()
print("file fruits.txt has been created")
# TO DO 2: Run the script.

# TO DO 3: Run the 'ls' command.

# TO DO 4: Print the contents of fruits.txt in a loop.

f = open('fruits.txt', 'r')
for line in f:
    print(line.strip())
f.close()