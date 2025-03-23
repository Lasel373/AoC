# AoC Day 2
# @author: Friedrich Leez

def is_safe_report(report):
    is_increasing = all(report[i] < report[i+1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i+1] for i in range(len(report) - 1))

    valid_differences = all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))

    return (is_increasing or is_decreasing) and valid_differences

def count_safe_reports_with_dampener(file_path):
    with open(file_path, 'r') as file:
        reports = [list(map(int, line.split())) for line in file.readlines()]

    safe_count = 0

    #safe_count = sum(1 for report in reports if is_safe_report(report))
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if is_safe_report(modified_report):
                    safe_count += 1
                    break

    return safe_count

file_path = 'file.txt'

result = count_safe_reports_with_dampener(file_path)
print(f"Number of safe reports (with dampener): {result}")