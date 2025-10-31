#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    """
    Add two numbers together, return the result.
    If error return string 'error: could not add numbers'
    Accepts ints/floats or strings containing numeric values.
    """
    try:
        # Try integer addition first (for exact int results)
        n1 = int(number1)
        n2 = int(number2)
        return n1 + n2
    except Exception:
        try:
            n1 = float(number1)
            n2 = float(number2)
            return n1 + n2
        except Exception:
            return 'error: could not add numbers'

def read_file(filename):
    """
    Read a file, return a list of all lines (with newline characters).
    If error return string 'error: could not read file'
    """
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
