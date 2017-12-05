"""
Functions for task 2 of the 2016 - Kont exam from NTNU
"""

def load_bin(filename: str) -> str:
    """
    Task 2a (5%)
    """
    bin_file = open(filename)
    bin_string = "".join(bin_file.read().split("\n"))
    bin_file.close()
    return bin_string

def store_txt(filename: str, content: str):
    txt_file = open(filename, "w")
    txt_file.write(content)
    txt_file.close()

def bin_to_dec(binary: str) -> int:
    """
    Task 2b (5%)
    """
    value = 0
    for i, b in enumerate(binary[::-1]):
        if b == "1":
            value += 2**i
    return value

def dec_to_char(dec: int) -> str:
    """
    Task 2c (4%)
    """
    chars = " ,.ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    return chars[dec]

def bin_to_txt(bin_string: str) -> str:
    """
    Task 2d (4%)
    """
    string = ""
    for i in range(0, len(bin_string), 5):
        dec = bin_to_dec(bin_string[i:i+5])
        char = dec_to_char(dec)
        string += char
    return string

def main():
    """
    Task 2e (7%)
    """
    print("Binary to text converter")
    b_file = input("Name of binary file to load from: ")
    #b_file = "binary.txt"
    b_string = load_bin(b_file)
    txt = bin_to_txt(b_string)
    t_file = input("Name of text file to save to: ")
    #t_file = "out.txt"
    store_txt(t_file, txt)
    print("{} has been converted and saved to {}".format(b_file, t_file))

if __name__ == "__main__":
    main()
