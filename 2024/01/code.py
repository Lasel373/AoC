# AoC Day 1
# @author: Friedrich

with open("2024/01/file.txt") as f:
    s = f.read()

leftList = list()
rightList = list()
distance = 0
similarity_score = 0

for pair in s.split("\n"):
    leftList.append(int(pair.split("   ")[0]))
    rightList.append(int(pair.split("   ")[1]))
    
leftList.sort()
rightList.sort()    

for i in range(len(leftList)):
    distance += abs(leftList[i] - rightList[i])

leftListAmountOfNumbers = [0 for _ in range (leftList[len(leftList)-1]+1)]
rightListAmountOfNumbers = [0 for _ in range (rightList[len(rightList)-1]+1)]
#Idee: gleich große Arrays! (das linke Array muss nicht immer weniger unterschiedliche Zahlen enthalten als das rechte)

for i in range(len(leftList)):
    leftListAmountOfNumbers[leftList[i]] += 1 
for i in range(len(rightList)):
    rightListAmountOfNumbers[rightList[i]] += 1 

for i in range(len(leftListAmountOfNumbers)):
     similarity_score += leftListAmountOfNumbers[i] * i * rightListAmountOfNumbers[i]
     #print(similarity_score)

print(distance)
print(similarity_score)


#runtime complexity: O(n)