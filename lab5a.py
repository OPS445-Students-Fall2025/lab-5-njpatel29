#!/usr/bin/env python3
# Author ID: [seneca_id]

def read_file_string(file_name):
    """
    Takes file_name as string for a file name, returns its entire contents as a string
    """
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    """
    Takes a file_name as string for a file name, 
    return its entire contents as a list of lines without new-line characters
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    # remove trailing newline from each line
    return [line.rstrip('\n') for line in lines]

if __name__ == '__main__':
    file_name = 'data.txt'
    # Print the file contents as a string (exact multi-line output)
    print(read_file_string(file_name), end='')  # ensure no extra newline
    # Print a blank line then the list form
    print()
    print(read_file_list(file_name))
