"""
Functions for task 3 of the 2017 - Kont exam from NTNU
"""

from math import ceil, floor
from time import sleep
from sys import stdout

def show_display(content: list):
    """
    Task 3 hidden 'show_display' function
    """
    board = []
    if isinstance(content, list) and len(content) == 6:
        board.append("#"*40)
        board.append("#" + " "*38 + "#")
        for string in content:
            if isinstance(string, str) and len(string) == 30:
                board.append("#    {}    #".format(string.upper()))
            else:
                raise ValueError("Content contains an element which is either not a string or not of length 30!")
        board.append("#" + " "*38 + "#")
        board.append("#"*40)
        stdout.write('\r')
        stdout.write("\n".join(board))
        stdout.flush()

    else:
        raise ValueError("Content is either not a list or not of length 6!")

def enter_line(prompt: str, length: int) -> str:
    """
    Task 3a (4%)
    """
    line = ""
    while len(line) != length:
        line = input(prompt)
        if len(line) == length:
            break
        else:
            print("The text must be {} characters long".format(length))
    return line

def adjust_string(text: str, length: int) -> str:
    """
    Task 3b (4%)
    """
    line = text[0:length]
    diff = length - len(line)
    whitespace_before = " "*floor(diff/2)
    whitespace_after = " "*ceil(diff/2)
    adjusted_line = whitespace_before + line + whitespace_after
    return adjusted_line

def enter_line_smart(prompt: str, length: int) -> str:
    """
    Task 3c (3%)
    """
    return adjust_string(input(prompt), length)

def enter_show_text():
    """
    Task 3d (4%)
    """
    text_list = []
    for i in range(6):
        text_list.append(enter_line_smart("Line {}: ".format(i + 1), 30))
    show_display(text_list)

def scroll_display(content: list, line: int):
    """
    Task 3e (5%)
    """
    for i in range(30):
        string = content[line-1]
        string = string[-1:] + string[:29]
        content[line-1] = string
        show_display(content)
        sleep(0.1)

def display_from_file(filename: str):
    """
    Task 3f (10%)
    """
    text_file = open(filename)
    text = text_file.read()
    text_file.close()

    lines = text.split("\n")
    for i in range(0, int(len(lines)), 6):
        current = lines[i:i+6]
        displayable = list(map(lambda line: adjust_string(line, 30), current))
        show_display(displayable)
        if int(len(lines))-6 != i:
            sleep(10.0)


def main():
    display_from_file("message.txt")

if __name__ == "__main__":
    main()
    