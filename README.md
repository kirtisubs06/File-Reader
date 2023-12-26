# File Processing in Python

## Overview
This Python program is designed to process text files. It reads a file provided by the user and reports the number of characters (including spaces and end-of-line characters), words, and lines in the file.

### Author
- **Author:** Kirti Subramanian
- **CWID:** 20531478
- **Date:** 11/13/2022

## Description
The program consists of functions to prompt the user for a filename, open the file, and calculate the number of characters, words, and lines. It is designed to handle errors gracefully, such as incorrect file names, and continues to prompt the user until a valid file name is provided.

## Features
- **File Opening:** Prompts the user for a filename and opens the file.
- **Error Handling:** Continuously prompts for a filename until a valid file is entered.
- **File Processing:** Counts the number of characters, words, and lines in the file.
- **Reporting:** Displays the counts to the user.

## Usage
### Running the Program
The program is executed by running the `main()` function. The user will be prompted to enter a file name. If the file is found, it processes the file and displays the counts. If the file is not found, it prompts again.

### Example Interaction
```python
if __name__ == "__main__":
    main()

# Output:
# What is the name of the file you would like to process? data
# That is not a valid filename, please try again.
#
# What is the name of the file you would like to process? data.txt
# The number of lines in this file: 5
# The number of words in this file: 17
# The number of characters in this file: 77
#
# Process finished with exit code 0
