import re
import os




finite_rule = "global_interrupts_wrong_phone"
finite_state = "18"


def print_files_on_dir():
    directory = '.'
    files = os.listdir(directory)
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

print_files_on_dir()  
print ('Select file with test')
input()


