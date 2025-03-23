# AoC Day 2
# Friedrich Leez

with open("02/file.txt") as f:
    s = f.read()

possible_games_id_sum = 0
power_sum = 0

#configuration
red_max = 12
green_max = 13
blue_max = 14

for x in s.strip().split("\n"):
    id = int(x.split(":")[0].split(" ")[1])  # ID of the game
    sets = []  #(sub)sets of cubes, that were revealed
    for s in x.split(":")[1].strip().split(";"):
        s = s.strip()
        subset = {"green":0, "red":0, "blue":0}
        for c in s.split(","):
            c = c.strip()
            subset[c.split(" ")[1]] = int(c.split(" ")[0])
        sets.insert(0,subset)
    
    s_green_max, s_blue_max, s_red_max = 0,0,0
    
    is_possible = True
    for subset in sets:
        is_possible = is_possible and subset["green"] <= green_max and subset["red"] <= red_max and subset["blue"] <= blue_max    
        if subset["green"] > s_green_max:
            s_green_max = subset["green"]
        if subset["red"] > s_red_max:
            s_red_max = subset["red"]
        if subset["blue"] > s_blue_max:
            s_blue_max = subset["blue"]
    if(is_possible):
        possible_games_id_sum += id
    
    power_sum += s_green_max * s_blue_max * s_red_max

print(possible_games_id_sum)
print(power_sum)