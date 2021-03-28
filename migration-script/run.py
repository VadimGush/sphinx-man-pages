# Python script for migrating man-pages to the new RST format
#!/bin/python3

from operations.transform import transform
import os

# Path to directory with man-pages
input_directory = "input"
# Path to directory with sphinx docs
output_directory = "output"

def __main__():
    print("=> Migration script started.")

    files = get_files(input_directory)
    for file in files:
        print(file)

    # On ever man-page file transform to RST format

    # Safe file to output directory

    print("=> Done!")

def get_files(path):
    files = []
    for file in os.listdir(path):
        file_path= path + "/" + file
        if not os.path.isdir(file_path):
            files.append(file_path)
        else:
            for dir_files in get_files(file_path):
                files.append(dir_files)
    return files

__main__()
