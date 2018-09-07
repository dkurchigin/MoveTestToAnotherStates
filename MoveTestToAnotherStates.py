import re
import os

directory = '.'
files = os.listdir(directory)

rule_list = []

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
        pattern_for_state = re.findall(r'^\w+',line)
        
        if len(rule_list) == 0:
            rule_list.append(pattern_for_state)
        else:
            #print (len(rule_list))
            if len(rule_list) == 1:
                if rule_list[0] != pattern_for_state:
                    rule_list.append(pattern_for_state)
                else:
                    n = 0
                    while n < 1:
                        if rule_list[n] != pattern_for_state:
                            rule_list.append(pattern_for_state)
                        n += 1
        #print (pattern_for_state)
        


print_files_on_dir() 
file_number = int(input())
find_finite_state(str(files[file_number]))
print ('')
print ('')
print ('===================')
print (rule_list[0])
print (rule_list[1])
#print (rule_list[2])
print (len(rule_list))

first = ["one", "two", "three"]
second = []
 
for element in first:
    print (element)
    if len(second) == 0:
        second.append(element)
    else:
        n = 0
        while n < len(second):
            print ("there")
            if second[n] != element:
                second.append(element)
            n += 1    
    
        
print (second)
#n = 0
#while n < len(second):
    #if second[n] != "boo":
        #second.append("boo")
    #n += 1
