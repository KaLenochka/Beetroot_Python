# Task 3
# Basics, import, work with os module
#
# Write a program that counts lines and characters in a file
# (similar to `wc` Unix-utility, for additional info about it
# follow the link: https://www.geeksforgeeks.org/wc-command-linux-examples/
# or in case you have macOS or Linux - just call manual for this utility via command: `man wc`).
#
#  Create a Python module called `mymod.py`, which has three functions:
#
# count_lines(name) function that reads an input file and counts the number of lines in it
# (hint: file.readlines() does most of the work for you, and `len` does the rest)
# count_chars(name) function that reads an input file and counts the number of characters in it
# (hint: file.read() returns a single string)
# test(name) function that calls both counting functions with a given input filename.
# Such a filename generally might be passed-in, hard-coded, input with raw_input,
# or pulled from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.
# All three `mymod.py` functions should expect a filename string to be passed in.
#
# Test your module interactively, using import and name qualification to fetch your exports.
# Does your PYTHONPATH need to include the directory where you created mymod.py?
# Try running your module on itself: e.g., test("mymod.py").
# Note that the test opens the file twice; if you’re feeling ambitious,
# you may be able to improve this by passing an open file object into the two count functions
# (hint: file.seek(0) is a file rewind).

def count_lines(file):
    with open(file, 'r') as f:
        a = f.readlines()
        if a[-1] == '\n':
            q_lines = len(a) + 1
        else:
            q_lines = len(a)
    return f'The number of lines in the {file} is {q_lines}.'


def count_chars(file):
    with open(file, 'r') as f:
        a = f.read()
        q_chars = len(a)
    return f'The number of characters in the {file} is {q_chars}.'


def test(file):
    try:
        lines = count_lines(file)
        chars = count_chars(file)
        return lines + '\n' + chars
    except Exception as msg_er:
        print(msg_er)
