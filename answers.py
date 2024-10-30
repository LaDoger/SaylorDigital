'''
This script lists all `.txt` files in `/answers`
and put in the `answers.txt` for the website to grab.
'''

import os

# Define the directory paths
answers_dir = "/answers"
output_file = "answers.txt"

# Ensure the script's directory is in the path for relative file operations
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Path to the answers directory relative to the script
answers_path = os.path.join(script_dir, answers_dir.strip('/'))

# Check if the answers directory exists, if not, create it
if not os.path.exists(answers_path):
    os.makedirs(answers_path)

# Function to write filenames to answers.txt, overwriting existing content
def write_filenames_to_file():
    # Get all .txt files from the directory, sorted by name
    txt_files = sorted([f for f in os.listdir(answers_path) if f.endswith('.txt')])
    
    # Write filenames to the output file, one per line, overwriting any previous content
    with open(output_file, 'w') as out_file:
        for file in txt_files:
            out_file.write(f"{file}\n")

# Main execution
if __name__ == "__main__":
    write_filenames_to_file()
    print(f"Filenames have been written to {output_file}")