# AoC Day 3
# @author: Friedrich Leez

with open("03/file.txt") as f:
    s = f.read()

schema = []
for x in s.strip().split("\n"):
    schema.append(list(x))

#symbols = {"*", "&", "@", "/", "+", "#", "$", "%", "="}
symbols = {"*", "&", "@", "/", "+", "#", "$", "%", "=", "-", "~", "'", ";", ":", "\\", "!", "?", "{", "}", "(", ")", "°", "^", "<", ">", "|", "_"}
digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

numbers = []
y_len,  x_len = len(schema[0]), len(schema)

def determine_number(x,y):
    """gibt ein Array der Positionen der einzelnen Ziffer zurück
    """
    num_array = [(x,y)]
    for i in range(y-1, -1, -1):
        if schema[x][i] in digits:
            num_array.append((x,i))
        else:
            break
    for i in range(y+1,y_len-1):
        if schema[x][i] in digits:
            num_array.append((x,i))
        else:
            break
    num_array.sort()
    return num_array

for x in range(x_len):
    for y in range(y_len):
        if schema[x][y] in symbols: 
            coordinates_changes = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, -1), (1, 1), (-1, 1)] #de-Moore-Nachbarschaft
            for (dx,dy) in coordinates_changes:
                pos = schema[x+dx][y+dy]
                if pos is not None:
                    if pos in digits:
                        num_array = determine_number(x+dx,y+dy)
                        if frozenset(num_array) not in numbers: #Verhinderung von Duplikaten
                            numbers.append(frozenset(num_array))

sum = 0
for numa in numbers:
    print("Ziffernpositionen der Zahl:" + str(numa))
    num = ""
    for (x,y) in numa:
        num += schema[x][y]
    print("Zahl:" + num)
    sum += int(num)
    
print(sum)

#Vielleicht hab ich die Aufgabenstellung falsch verstanden???