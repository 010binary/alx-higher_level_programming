#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <value_to_write> <file_name>"
    exit 1
fi

# Assign command line arguments to variables
value_to_write=$1
filename="$2-answer.txt"

echo "$value_to_write" > "$filename"

# Check if the file exists
if [ -f "$filename" ]; then
    # Git operations - add, commit, and push
    git add "$filename"
    git commit -m "Answers to $filename"
    git push 
    echo "File '$filename' with value '$value_to_write' added, committed, and pushed to the repository."
else
    echo "Error: File creation failed."
fi

