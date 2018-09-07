import re
import os

directory = '.'
files = os.listdir(directory)

condition_list = []

initial_condition = ""
finite_condition = ""


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

    
def find_conditions(file_path):
    f = open(file_path, 'r', encoding='utf-8')

    for line in f:
        pattern_for_state = re.findall(r'^\w+',line)

        n = 0
        equal_file = False
        while n < len(condition_list):
            if condition_list[n] == pattern_for_state:
                equal_file = True
            n += 1
        if equal_file == False:
            condition_list.append(pattern_for_state)
        else:
            equal_file = False

    n = 0
    print ('')
    print ('')
    print ('===List of conditions===')
    print ('')
    print ('')
    while n < len(condition_list):
        condition = condition_list[n]
        result_string = "[" + str(n) + "]" + " - " + str(condition)
        print (result_string)
        n += 1
    print ('')
    print ('')
    print ('========================')
    print ('')
    print ('Select condition from file. Enter the number:')
        

#def copy_rules(initial,finite):
#    f = open(file_number, 'r', encoding='utf-8')
    
#    for line in f:
#        pattern_for_input_rules = re.findall(r''initial'',line)


print_files_on_dir()
 
file_number = int(input())
find_conditions(str(files[file_number]))

initial_condition = int(input())
find_conditions(str(files[file_number]))
finite_condition = int(input())

print (initial_condition)
print (finite_condition)

#copy_rules(initial_condition,finite_condition)
