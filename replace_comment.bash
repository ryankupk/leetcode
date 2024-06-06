#!/bin/bash

# Function to replace '//' with '#' in the first line of a Python file
replace_comment() {
    local file="$1"
    if [[ "$file" == *.py ]]; then
        first_line=$(head -n 1 "$file")
        if [[ "$first_line" == //* ]]; then
            sed -i '1s|//|#|' "$file"
        fi
    fi
}

# Recursively process files in the current directory and subdirectories
process_files() {
    for file in "$1"/*; do
        if [ -f "$file" ]; then
            replace_comment "$file"
        elif [ -d "$file" ]; then
            process_files "$file"
        fi
    done
}

# Start processing from the current directory
process_files "$(pwd)"
