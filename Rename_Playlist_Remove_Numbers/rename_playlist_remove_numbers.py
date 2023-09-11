import os
import re

def remove_pattern_from_filenames(directory):
    # Define the regular expression pattern to match "01 - " at the beginning of the file names
    pattern = re.compile(r'^\d{2} - ')

    # List all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file name matches the pattern
        if pattern.match(filename):
            new_filename = pattern.sub('', filename)  # Remove the pattern
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)  # Rename the file

if __name__ == "__main__":
    directory = input("Enter the directory path where the files are located: ")
    if os.path.isdir(directory):
        remove_pattern_from_filenames(directory)
        print("Pattern removed from file names.")
    else:
        print("Invalid directory path. Please provide a valid directory path.")
