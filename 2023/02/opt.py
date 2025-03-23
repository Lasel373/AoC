# AoC Day 2
# Friedrich Leez

with open("02/file.txt") as f:
    s = f.read()

possible_games_id_sum = 0
power_sum = 0

# Configuration
limits = {"red": 12, "green": 13, "blue": 14}

for line in s.strip().split("\n"):
    parts = line.split(":")
    game_id = int(parts[0].split(" ")[1])  # ID of the game
    subsets = []

    for subset_str in parts[1].strip().split(";"):
        subset = {color: int(amount) for amount, color in (c.strip().split(" ") for c in subset_str.split(","))}
        subsets.append(subset)

    s_limits = {color: max(subset[color] for subset in subsets) for color in limits}

    is_possible = all(subset[color] <= limits[color] for subset in subsets for color in limits)
    if is_possible:
        possible_games_id_sum += game_id

    power_sum += s_limits["green"] * s_limits["blue"] * s_limits["red"]

print(possible_games_id_sum)
print(power_sum)
