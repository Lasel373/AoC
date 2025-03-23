schema = []
with open("03/file.txt") as f:
    s = f.read()
for x in s.strip().split("\n"):
    schema.append(list(x))

symbols = {"*", "&", "@", "/", "+", "#", "$", "%", "="}
digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

numbers = []
y_len, x_len = len(schema[0]), len(schema)

def determine_number(x,y):
    num_array = [(x,y)]
    print(num_array)
    for i in range(y-1, -1, -1):
        print(i)
        if schema[x][i] in digits:
            num_array.append((x,i))
        else:
            break
    for i in range(y+1,y_len-1):
        print(i)
        if schema[x][i] in digits:
            num_array.append((x,i))
        else:
            break
    num_array.sort()
    return num_array

print(determine_number(9,5))