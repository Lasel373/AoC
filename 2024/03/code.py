# AoC Day 3
# @author: Friedrich Leez

import re

with open("2024/03/file.txt") as f:
    corruptedMemory = f.read()

def getTotalSumForAllValidMulOperands():
    #idea: define regex for all mul(X,Y) appearances with -999 to 999 for X and Y and add them up
    listOfValidMulOperands = [(int(x), int(y)) for x, y in re.findall(r"mul\((-?\d+),(-?\d+)\)", corruptedMemory) if -999 <= int(x) <= 999 and -999 <= int(y) <= 999]

    totalSum = 0
    for (a,b) in listOfValidMulOperands:
        totalSum += a * b
    return totalSum

def getTotalSumForAllValidMulOperandsDoAndDont():
    listOfRelevantOperators = re.findall(r"mul\((-?\d+),(-?\d+)\)|(do\(\))|(don't\(\))", corruptedMemory)

    totalSum = 0
    allowMul = True
    for (mul1, mul2, do, dont) in listOfRelevantOperators:
        if do:
            allowMul = True
        elif dont:
            allowMul = False
        elif allowMul:
            totalSum += int(mul1) * int(mul2)
    return totalSum

print(getTotalSumForAllValidMulOperands())
print(getTotalSumForAllValidMulOperandsDoAndDont())