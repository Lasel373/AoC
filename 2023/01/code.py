# AoC Day 1
# @author: Friedrich Leez

import re

file = open("01/file.txt",'r')

def text_to_number(line:str):
    #eliminate overlaces
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    spans = []
    for number in ones:
        copy = line
        for _ in range(re.findall(number, line).__len__()):
            print(number)
            spans.append(re.search(number,line).span())
            copy = copy.replace(number, "", 1)
            print(copy)
    spans.sort()
    print(spans)
    line_trv = ""
    prev = (0,0)
    for span in spans:
        if prev[1] < span[0]: # keine Überlappung
            line_trv += line[prev[1]:span[0]]
            print(line_trv)
        line_trv += line[span[0]:span[1]]
        print(line_trv)
        prev = span
    line_trv += line[prev[1]:line.__len__()-1]
    
    #replacing the words with numbers
    substring = line_trv[:2]
    for char in line_trv[2:]:
        substring += char
        # print(substring)
        substring = substring.replace("one","1", 1).replace("two","2", 1).replace("three","3", 1).replace("four","4", 1).replace("five","5", 1).replace("six","6", 1).replace("seven","7", 1).replace("eight","8", 1).replace("nine","9", 1)
    
    substring_rv = ""
    for char in line[::-1]:
        substring_rv = char + substring_rv
        # print(substring_rv)
        substring_rv = substring_rv.replace("one","1", 1).replace("two","2", 1).replace("three","3", 1).replace("four","4", 1).replace("five","5", 1).replace("six","6", 1).replace("seven","7", 1).replace("eight","8", 1).replace("nine","9", 1)
    
    if substring == substring_rv:
        return substring
    else:
        print("Why???")
        return ""
        
    
sum = 0
for line in file:
    line_val = 0
    digit_line = text_to_number(line)
    for char in digit_line[::-1]:
        if char.isdigit() and char != '\n':
            line_val += int(char)
            break
    for char in digit_line:
        if char.isdigit() and char != '\n':
            if line_val == 0:
                line_val += int(char)
            line_val += 10 * int(char)
            break
    sum += line_val
        
print(sum)