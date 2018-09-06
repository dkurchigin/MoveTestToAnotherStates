import re
import os

directory = '.'
files = os.listdir(directory)

finite_rule = "global_interrupts_wrong_phone"
finite_state = "18"


def print_files_on_dir():
    n = 0
    
    print ('')
    print ('')
    print ('===List of files===')
    print ('')
    print ('')
    while n < len(files):
        name_of_file = files[n]
        result_string = "[" + str(n) + "]" + " - " + name_of_file
        print (result_string)
        n += 1
    print ('')
    print ('')
    print ('===================')
    print ('')
    print ('Select file with test. Enter the number:')

    
def find_finite_state(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    for line in f:
        print (line)


print_files_on_dir() 
file_number = int(input())
find_finite_state(str(files[file_number]))


