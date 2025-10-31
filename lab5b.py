#!/usr/bin/env python3
# Author ID: [seneca_id]

def read_file_string(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return [line.rstrip('\n') for line in lines]

def append_file_string(file_name, string_of_lines):
    """
    Takes two strings, appends the string to the end of the file
    """
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    """
    Takes a string (file_name) and list (list_of_lines), writes all items from list to file where each item is one line
    """
    f = open(file_name, 'w')
    for item in list_of_lines:
        f.write(str(item) + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """
    Reads data from first file, writes data to new file adding line numbers to the beginning of each line
    """
    f_read = open(file_name_read, 'r')
    lines = f_read.readlines()
    f_read.close()
    f_write = open(file_name_write, 'w')
    lineno = 1
    for line in lines:
        text = line.rstrip('\n')
        f_write.write(f"{lineno}:{text}\n")
        lineno += 1
    f_write.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    # Print file1 contents (may show appended content on subsequent runs)
    print(read_file_string(file1), end='\n')
    write_file_list(file2, list1)
    # Print file2 contents
    print(read_file_string(file2), end='\n')
    copy_file_add_line_numbers(file2, file3)
    # Print file3 contents
    print(read_file_string(file3), end='')
