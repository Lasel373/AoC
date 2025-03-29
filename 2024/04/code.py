# AoC Day 4
# @author: Friedrich Leez

#first ideas: regex pattern matching for horizontal occurences, transposing the file or iterating over columns for vertical occurences

vectorPairs = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (1, -1), (1, 1), (-1, 1)] #mayba change order

with open("2024/04/file.txt") as f:
    lines = [line.strip() for line in f.readlines()]

#Idea: treat the file as a 2d matrix, apply seach algorithm
file_as_matrix = [list(line) for line in lines]

sum = 0  

def find_adjacent_characters(i, j):
    charAndDirectionList = []
    for pair in vectorPairs:
        if 0 <= i + pair[0] < len(file_as_matrix) and 0 <= j + pair[1]< len(file_as_matrix[0]):
            charAndDirectionList.append((file_as_matrix[i+pair[0]][j+pair[1]], pair))
    return charAndDirectionList 

#X, M has to be up, down, right or left; -> then check next position for A, then check for S; von-Neumann-Adjacency
#X; M has to be up-left, up-right, down-left or down-right; we have to diagonal; Moore - vonNeumann

for i in range(len(file_as_matrix)):
    for j in range(len(file_as_matrix[0])):
        if file_as_matrix[i][j] == "X":
            adjacent_characters = find_adjacent_characters(i,j)
            print(adjacent_characters)
            for (char, direction) in adjacent_characters:
                if char == "M":
                    next_i, next_j = i + direction[0], j + direction[1]
                    if 0 <= next_i < len(file_as_matrix) and 0 <= next_j < len(file_as_matrix[0]):
                        if file_as_matrix[next_i][next_j] == "A":
                            next_i, next_j = next_i + direction[0], next_j + direction[1]
                            if 0 <= next_i < len(file_as_matrix) and 0 <= next_j < len(file_as_matrix[0]):
                                if file_as_matrix[next_i][next_j] == "S":
                                    sum += 1

#X-MAS

print(sum)