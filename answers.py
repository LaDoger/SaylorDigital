import os

# Define the directory paths
answers_dir = "/answers"
output_file = "answers.txt"

# Ensure the script's directory is in the path for relative file operations
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Path to the answers directory relative to the script
answers_path = os.path.join(script_dir, answers_dir.strip('/'))

# Check if the answers directory exists
if not os.path.exists(answers_path):
    os.makedirs(answers_path)

# Function to get existing filenames from answers.txt
def get_existing_files():
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            return set(line.strip() for line in f if line.strip())
    return set()

# Function to write filenames to answers.txt
def write_filenames_to_file():
    existing_files = get_existing_files()
    with open(output_file, 'a') as out_file:
        for file in os.listdir(answers_path):
            if file.endswith('.txt') and file not in existing_files:
                out_file.write(f"{file}\n")
                existing_files.add(file)  # Add to set to ensure no duplicates even in this run

# Main execution
if __name__ == "__main__":
    write_filenames_to_file()
    print(f"Filenames have been written to {output_file}")