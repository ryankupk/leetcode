#!/bin/bash

update_file() {
    local file="$1"
    local dir=$(dirname "$file")
    local filename=$(basename "$file")
    local extension="${filename##*.}"
    local newext=""
    local comment_symbol=""

    case "$extension" in
        bash)
            newext="sh"
            comment_symbol="#"
            ;;
        csharp)
            newext="cs"
            comment_symbol="//"
            ;;
        golang)
            newext="go"
            comment_symbol="//"
            ;;
        javascript)
            newext="js"
            comment_symbol="//"
            ;;
        mysql|postgresql)
            newext="sql"
            comment_symbol="--"
            ;;
        python|python3)
            newext="py"
            comment_symbol="#"
            ;;
        ruby)
            newext="rb"
            comment_symbol="#"
            ;;
        *)
            echo "Unknown extension: $extension"
            return
            ;;
    esac

    # Rename the file
    local newname="${filename%.*}.$newext"
    mv "$file" "$dir/$newname"

    # Update the comment
    if [ "$comment_symbol" != "//" ]; then
        sed -i "s|^//|$comment_symbol|" "$dir/$newname"
    fi

    echo "Updated $file to $dir/$newname and adjusted comments"
}

# Create the submissions directory if it doesn't exist
mkdir -p ../submissions

# Loop through all directories in the current directory
for dir in */; do
    # Remove trailing slash from directory name
    dir=${dir%/}
    
    # Check if there's an "Accepted" subdirectory
    if [ -d "$dir/Accepted" ]; then
        # Find the solution file (assuming there's only one)
        solution_file=$(find "$dir/Accepted" -type f -not -name "info.txt" | head -n 1)
        
        if [ -n "$solution_file" ]; then
            # Extract the file extension
            extension="${solution_file##*.}"
            
            # Move and rename the file
            new_file="../submissions/${dir}.${extension}"
            mv "$solution_file" "$new_file"
            
            echo "Moved solution for $dir to $new_file"
            
            # Update the file extension and comments
            update_file "$new_file"
        else
            echo "No solution file found for $dir"
        fi
    else
        echo "No Accepted subdirectory found for $dir"
    fi
done
