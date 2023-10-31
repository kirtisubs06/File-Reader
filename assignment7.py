"""
Assignment 7: "File Processing"

Author: Kirti Subramanian
CWID: 20531478
Date: 11/13/2022

Program Description: This program asks the user for a filename, opens the file, and reads through the file
just once before reporting back to the user the number of characters (including spaces and end-of-line characters),
the number of words, and the number of lines in the file.
"""


def find_file():
    """
    Prompts the user for the file name and returns the file handle if the file exists. It keeps prompting until the
    user enters a valid filename.
    :return: file handle
    """
    while True:
        filename = input("What is the name of the file you would like to process? ")
        try:
            f = open(filename, "r")
            return f
        except IOError:
            print("That is not a valid filename, please try again.")
            print()


def count_values(f):
    """
    Calculates and returns the number of lines, words, and characters in the file.
    :param f: file handle
    :return: a tuple containing the character count, word count, and line count
    """
    line_count = 0
    word_count = 0
    character_count = 0
    for line in f.readlines():
        words = line.split()
        word_count = word_count + len(words)
        character_count = character_count + len(line)
        line_count += 1
    return character_count, word_count, line_count


def main():
    f = find_file()
    character_count, word_count, line_count = count_values(f)
    f.close()
    print("The number of lines in this file:", line_count)
    print("The number of words in this file:", word_count)
    print("The number of characters in this file:", character_count)


if __name__ == "__main__":
    main()


# test output
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment7.py
What is the name of the file you would like to process? data
That is not a valid filename, please try again.

What is the name of the file you would like to process? data.txt
The number of lines in this file: 5
The number of words in this file: 17
The number of characters in this file: 77

Process finished with exit code 0

"""