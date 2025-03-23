# AoC Day 3
# @author: Friedrich Leez

import re

def extract_and_multiply_from_file(file_path):
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()

    mul_pattern = r"mul\((-?\d+),(-?\d+)\)"

    valid_instructions = re.findall(mul_pattern, corrupted_memory)

    total = 0
    for x, y in valid_instructions:
        total += int(x) * int(y)

    return total

def extract_and_multiply_with_conditions(file_path):
    # Read the content from the file
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()

    # Regular expression to find valid mul instructions (mul(X,Y))
    mul_pattern = r"mul\((-?\d+),(-?\d+)\)"

    # Regular expressions to find do() and don't() instructions
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Track whether mul instructions are enabled or disabled
    mul_enabled = True
    total = 0

    # Log initial state
    print("Initial state: mul_enabled =", mul_enabled)

    # Process each section of the corrupted memory
    index = 0
    while index < len(corrupted_memory):
        # Look for the next mul instruction
        mul_match = re.search(mul_pattern, corrupted_memory[index:])
        do_match = re.search(do_pattern, corrupted_memory[index:])
        dont_match = re.search(dont_pattern, corrupted_memory[index:])

        # If there are no more mul, do, or don't instructions, break the loop
        if not mul_match and not do_match and not dont_match:
            print("No more instructions to process. Exiting loop.")
            break

        # Check for do() or don't() instructions first
        if do_match:
            print(f"do() found at index {index}. mul_enabled = {mul_enabled}. Skipping.")
            index += do_match.end()
        elif dont_match:
            print(f"don't() found at index {index}. mul_enabled set to False.")
            mul_enabled = False
            index += dont_match.end()
        elif mul_match:
            # If mul is enabled, perform the multiplication
            if mul_enabled:
                x = int(mul_match.group(1))
                y = int(mul_match.group(2))
                total += x * y
                print(f"mul({x},{y}) found at index {index}. Result: {x * y}. Total: {total}.")
            else:
                print(f"mul instruction found at index {index}, but mul is disabled. Skipping.")
            index += mul_match.end()

    return total


# Test with the provided file
file_path = '2024/03/file.txt'
result = extract_and_multiply_from_file(file_path)

print(f"The sum of all valid multiplications is: {result}")