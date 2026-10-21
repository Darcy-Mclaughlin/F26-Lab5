#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 21/10/2026
# Purpose: Read a text file.
# Usage: ./lab5a.py

# TO DO 1: Create data2.txt.

# TO DO 2: Complete the functions below.
def read_file_lineByLine(file_name):
    # Takes file_name as a string, reads the file in a loop one line at a time and prints each line.
    with open(file_name, 'r') as f:
        for line in f:
            print(line.strip())
def read_file_list(file_name):
    # Takes a file_name as string, read file line by line and add the line in a list as a list element without new-line characters
    # Return the list.
    lines = []
    with open(file_name, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines
def main():
    file_name = 'data2.txt'
    read_file_lineByLine(file_name)
    print(read_file_list(file_name))

if __name__ == '__main__':
    main()