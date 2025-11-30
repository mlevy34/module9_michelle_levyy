'''
PSUEDECODE:
1. Import files and declare all lists and global variables
2. Read the original poem and print it to the screen line by line.
- READ_POEM():
    A. create the path variable that joins the filename you want to open
    B. using try/except, open the file that has variable name path and read
    the file.
    C. for every line in the path file: strip the line, Append the line to
    poem_list, and print the line to the screen.
    D. if file doesn't exist, a file not found error will be raised.
3. Switch the order of the lines in the original poem by manipulating
the poem list. A while loop is used in the process
4. In this new list, change every occurrence of "thy" to "you".
5. Write the new poem into the file "poem_remix.txt"
- WRITE_POEM():
    A. Create the path variable that joins the file
    B. Using try/except, open the file to write in it.
    C. For every line in the modified poem list: strip it
    and write it onto this new file.
    D. if file doesn't exist, a file not found error will be raised.
6. Print blank space to differentiate poems..
7. Use the read_poem function again to read the lines of the modified poem.
8. Put the lines you want to append to the file in a list called statements.
9. To this new file, append the lines to the bottom of the file.
- APPEND_POEM():
    A. Create the path variable that joins the file
    B. Using try/except, open the file to append it.
    C. For every item in the list of statments you want to
    add: strip it and append it onto the file.
    D. if file doesn't exist, a file not found error will be raised.

'''





import os
import random

# Global lists to store poem lines
poem_list1 = []     # Will store original poem lines
poem_list_2 = []    # Will store remixed poem lines

# Directory where text files are stored
DOCS_DIR = "docs"


def read_poem(filename, poem_list):
    """
    Read a poem file line-by-line, strip whitespace,
    append each line to the given poem_list, and print it.

    Parameters:
        filename (str): The name of the file to open (inside docs folder).
        poem_list (list): The list to store each cleaned line.

    Behavior:
        - Opens the file in read mode
        - Strips newline characters
        - Prints each line
        - Appends lines to poem_list
    """
    PATH = os.path.join(DOCS_DIR, filename)
    try:
        with open(PATH, "r") as f:
            for line in f:
                line = line.strip()       # remove trailing newline
                poem_list.append(line)    # store line
                print(line)               # print original/remixed poem
    except FileNotFoundError as ff:
        print(ff)


def write_poem(filename, poem_lines):
    """
    Write a list of poem lines to a file, overwriting any previous contents.

    Parameters:
        filename (str): Name of the output file.
        poem_lines (list): List of strings to write, one per line.

    Behavior:
        - Opens file in write mode
        - Writes each line followed by '\n'
    """
    PATH = os.path.join(DOCS_DIR, filename)
    try:
        with open(PATH, "w") as f:
            for line in poem_lines:
                line = line.strip()   # ensure clean formatting
                f.write(line + "\n")  # write each line to the file
    except FileNotFoundError as ff:
        print(ff)


def append_poem(filename, statements):
    """
    Append additional lines (reflection or bonus lines)
    to the end of an existing poem file.

    Parameters:
        filename (str): File to append to.
        statements (list): Lines of text to add.

    Behavior:
        - Opens file in append mode
        - Writes each new line at the bottom
    """
    PATH = os.path.join(DOCS_DIR, filename)
    try:
        with open(PATH, "a") as f:
            for line in statements:
                f.write(line + "\n")
    except FileNotFoundError as ff:
        print(ff)


def main():
    """
    Orchestrates the entire poem remix program.

    Steps:
        1. Read the original poem into poem_list1 and print it.
        2. Rearrange the poem by moving the last line to the front.
        3. Replace one random word in each line with "Hello".
        4. Store the remixed poem in poem_list_2.
        5. Write the remixed poem to poem_remix.txt.
        6. Print the remixed poem.
        7. Append reflection lines to the remix file.
    """

    # Step 1: Read original poem and print it
    read_poem("poem_original.txt", poem_list1)

    # Step 2: Move the last line to the front
    i = len(poem_list1) - 1
    last = poem_list1[i]

    # Shift other lines down one position
    while i > 0:
        poem_list1[i] = poem_list1[i - 1]
        i -= 1

    poem_list1[0] = last  # Put original last line at the front

    # Step 3: Replace all occurrences of "thy" with "you"

    for r in poem_list1:
        if "thy" in r:
          r =  r.replace("thy", "you")
        poem_list_2.append(r)
    # Step 4: Write remix to file
    write_poem("poem_remix.txt", poem_list_2)

    print()  # blank line to separate poems

    # Step 5: Read and print poem_remix for confirmation
    read_poem("poem_remix.txt", poem_list_2)

    # Step 6: Append reflection lines at bottom of file
    statements = [
                    "Remixed by: Michelle Levy",
                    "I swapped lines and changed words"
                 ]
    append_poem("poem_remix.txt", statements)


# Run the program
if __name__ == "__main__":
    main()