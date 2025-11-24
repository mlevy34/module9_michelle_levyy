import os

# Directory where the poem files are stored
DOCS_STIR = "docs"

# Lists to hold the poem lines and reversed poem lines
poem = []
reversed_poem = []

def read_func(filename):
    """
    Reads a text file line by line, strips whitespace, appends each line
    to the global 'poem' list, and prints each line.

    Args:
        filename (str): Name of the file to read from the DOCS_STIR directory.
    """
    PATH = os.path.join(DOCS_STIR, filename)  # Build full path to file
    try:
        with open(PATH, "r") as f:
            for line in f:
                line = line.strip()  # Remove leading/trailing whitespace
                poem.append(line)    # Store the line in the global list
                print(line)          # Print the line
    except FileNotFoundError as ff:
        print(ff)  # Print error if file is not found

def write_poem(filename, poem_lines):
    """
    Writes a list of lines to a text file. Each line is written on a new line.

    Args:
        filename (str): Name of the file to write to in DOCS_STIR directory.
        poem_lines (list): List of strings to write to the file.
    """
    PATH = os.path.join(DOCS_STIR, filename)  # Build full path to file
    try:
        with open(PATH, "w") as f:
            for line in poem_lines:
                f.write(line + "\n")  # Write each line followed by newline
    except FileNotFoundError as ff:
        print(ff)  # Print error if file path is invalid

def append_func(filename):
    """
    Appends two specific lines to the end of the file.

    Args:
        filename (str): Name of the file to append to in DOCS_STIR directory.
    """
    PATH = os.path.join(DOCS_STIR, filename)  # Build full path to file
    try:
        with open(PATH, "a") as f:  # Open file in append mode
            f.write("I like this poem because it inspires me \n")  # Add first line
            f.write("Michelle Levy \n")                             # Add signature line
    except FileNotFoundError as ff:
        print(ff)  # Print error if file not found

def main():
    """
    Main function to perform the following steps:
    1. Read 'poem.txt' and store lines in 'poem' list.
    2. Reverse the order of lines and store in 'reversed_poem'.
    3. Write the reversed poem to 'poem2.txt'.
    4. Read and print the reversed poem from 'poem2.txt'.
    5. Append custom lines to 'poem2.txt'.
    """
    # Read original poem into 'poem' list
    read_func("poem.txt")

    # Reverse the poem lines
    index = len(poem) - 1
    while index >= 0:
        reversed_poem.append(poem[index])
        index -= 1

    # Write the reversed poem to a new file
    write_poem("poem2.txt", reversed_poem)

    # Read and print the reversed poem
    read_func("poem2.txt")

    # Append extra lines to the reversed poem file
    append_func("poem2.txt")

# Entry point of the program
if __name__ == "__main__":
    main()