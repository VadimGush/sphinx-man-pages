#!/bin/python3
# Python script for migrating man-pages to the new RST format

import os
import re

from parser.parse import parse

# Path to directory with man-pages
input_directory = "input"
# Path to directory with sphinx docs
output_directory = "output"

# File with documentation is any file that has
# a dot with a digit at the end of the filename
man_file_pattern = re.compile(r".*\.\d$")

def __main__():
    print("=> Migration script started\n")

    files = get_files(input_directory)
    for file in files:
        process_file(file)
        # Remove this break that I use for testing
        break

    print("\n=> Done!")

def process_file(file_path):
    # is it file with documentation
    if man_file_pattern.match(file_path) is not None:
        print(file_path)
        file = open(file_path)
        parse(file.readlines())

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
