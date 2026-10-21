#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 21/10/2026
# Purpose: Catch ZeroDivisionError
# Usage: ./lab5f.py

# TO DO 1: Complete the given functions.

def safe_divide(a,b):
  # divide a by b
  # Add an exception block to raise the error if error occurs because of a zero denominator.
  # Except block should display the appropriate error messages
  try:
    result = a / b
    print(f"{a} / {b} = {result}")
    return result
  except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    return None

def main():
  safe_divide(10,5)  # works
  safe_divide(10,0)  # exception : Zero Division Error

if __name__ == '__main__':
  main()
  
