"""
Functions for task 4 of the 2017 - Kont exam from NTNU
"""

def myst1(s1, s2,s3):
    """
    Task 4a (5%)
    """
    string = ''
    for i in range(len(s1)):
        string += s1[i]+s2[i]+s3[i]
    return string

def myst2(m):
    """
    Task 4b (5%)
    """
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == 0 or i == len(m)-1:
                m[i][j] = 0
            elif j == 0 or j == len(m)-1:
                m[i][j] = 0
    return m

def myst3(s):
    """
    Task 4c (5%)
    """
    string = ''
    for i in range(len(s)-1, -1, -2):
        string += s[i]
    return string

def myst4(x, y, z):
    """
    Task 4d (5%)
    """
    if y < z:
        return myst4(x*x, y+1, z)
    else:
        return x

def main():
    t_a = myst1("G dg", "omd!", "dia!")
    print(t_a)

    matrix = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
    t_b = myst2(matrix)
    print(t_b)

    t_c = myst3("xsidrwteasMc hedhfT")
    print(t_c)

    t_d = myst4(2, 1, 4)
    print(t_d)

if __name__ == "__main__":
    main()
