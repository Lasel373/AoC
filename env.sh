#!/bin/bash
# env.sh
#
# Usage:
#   ./env.sh               -> Regular mode (December only, current day)
#   ./env.sh --test        -> Test mode (current year, days 01-24)
#   ./env.sh 2024          -> Specified Year mode (for year 2024, creates missing day folders)
#
# Note: Set the SESSION environment variable to your AoC session cookie.
# Example: export SESSION="your_session_cookie_here"

# Get current date info
current_year=$(date +%Y)
current_month=$(date +%m)
current_day=$(date +%d)

# Default mode is "regular" and year is the current year
mode="regular"
year="$current_year"

# Parse input argument, if any
if [ -n "$1" ]; then
    if [ "$1" = "--test" ]; then
        mode="test"
    elif echo "$1" | grep -Eq '^[0-9]{4}$'; then
        mode="year"
        year="$1"
    else
        echo "Unrecognized argument: $1"
        echo "Usage: ./env.sh [--test | <year>]"
        exit 1
    fi
fi

# Function to create day folder, code.py, and fetch puzzle input into file.txt
create_day_folder() {
    # Format folder name with two digits (e.g., 01, 02, …)
    day_folder=$(printf "%02d" "$1")
    target_folder="$year/$day_folder"

    if [ ! -d "$target_folder" ]; then
        mkdir -p "$target_folder"
        echo "Created folder: $target_folder"
    else
        echo "Folder already exists: $target_folder"
    fi

    # Prepare the AoC input URL; remove any leading zero for the day
    day_no_zero=$(echo "$1" | sed 's/^0*//')
    input_url="https://adventofcode.com/$year/day/$day_no_zero/input"

    # Create or update code.py with header if it doesn't exist or is empty
    if [ ! -s "$target_folder/code.py" ]; then
        echo -e "# AoC Day $day_no_zero\n# @author: Friedrich Leez" > "$target_folder/code.py"
        echo "Created code.py with header in $target_folder"
    else
        echo "code.py already exists and is not empty in $target_folder"
    fi

    # If SESSION is provided, use curl to fetch the input; otherwise, create an empty file.txt
    if [ -n "$SESSION" ]; then
        curl -s -b "session=$SESSION" "$input_url" | sed -z '$s/\n$//' > "$target_folder/file.txt"
        echo "Downloaded puzzle input from $input_url into $target_folder/file.txt"
    else
        touch "$target_folder/file.txt"
        echo "SESSION cookie not provided. Created blank file.txt in $target_folder"
    fi
}

# Mode: Specified Year Mode
if [ "$mode" = "year" ]; then
    echo "Running in Specified Year mode for year: $year"
    # Create year folder if it doesn't exist
    if [ ! -d "$year" ]; then
        mkdir "$year"
        echo "Created folder: $year"
    fi
    # Create day folders 01 to 24 only if they don't already exist.
    for i in $(seq 1 24); do
        create_day_folder "$i"
    done

# Mode: Test Mode (all days for current year)
elif [ "$mode" = "test" ]; then
    echo "Running in Test mode for current year: $year"
    # Create year folder if it doesn't exist
    if [ ! -d "$year" ]; then
        mkdir "$year"
        echo "Created folder: $year"
    fi
    # Create day folders 01 to 24
    for i in $(seq 1 24); do
        create_day_folder "$i"
    done

# Mode: Regular mode (only runs in December)
elif [ "$mode" = "regular" ]; then
    if [ "$current_month" -eq 12 ]; then
        # On December 1, create the year folder if it doesn't exist
        if [ "$current_day" -eq 1 ] && [ ! -d "$year" ]; then
            mkdir "$year"
            echo "Created folder: $year"
        fi
        # For days 1 to 24, create the corresponding day folder if it doesn't exist
        if [ "$current_day" -ge 1 ] && [ "$current_day" -le 24 ]; then
            create_day_folder "$current_day"
        else
            echo "No action: Today is December $current_day, outside the 1-24 range."
        fi
    else
        echo "Regular mode runs only in December. Use --test or specify a year to override."
    fi
fi