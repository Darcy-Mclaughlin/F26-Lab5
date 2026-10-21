#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 21/10/2026
# Purpose: Process File data.
# Usage: ./lab5d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.


# TO DO 2: Follow the instructions from the readme.me file to create the exact output.

# In a loop read each line from pythonStatements.txt and machineCode.txt. Remember the lines in both files correspond to each other.
# Remove all leading and trailing spaces from the line that you read from pythonStatements.txt, also remove the comments, so that all the is left is pure python code. The strip() method can be used to do this.
# Write this pure python statement with its corresponding machine code statement in a new file "output.txt".
# Add a tab between the python statement and its corresponding machine code when writing the lines.
# Run the script from command line using the command: python ./lab5d.py
# The output should be like this:

with open("pythonStatements.txt", "r") as pythonFile, open("machineCode.txt", "r") as machineFile, open("output.txt", "w") as outputFile:

    lines_python = pythonFile.readlines()
    lines_machine = machineFile.readlines()
    listMachine = []
    listPython = []

    for line in lines_machine:
        listMachine.append(line.strip())

    for line in lines_python:
        purePython = line.split('#')[0].strip()
        listPython.append(purePython)

    for i in range(len(listPython)):
        outputFile.write(f"{listPython[i]}\t{listMachine[i]}\n")

        