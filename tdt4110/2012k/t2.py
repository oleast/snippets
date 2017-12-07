
def unknown(a, b, c):
    if (b >= a) and (a >= 10):
        b = a
    elif (a <= c) and (b >= a):
        if (c > a):
            c = a
        elif (b > c):
            a = b
        else:
            b = a
    else:
        b = c
    table = [a, b, c]
    return table

def unknown2(table):
    a = table[0]
    for i in range(0, len(table)-1):
        table[i]=table[i+1]
    table[len(table)-1] = a
    return table

def main():
    x = 4
    y = 6
    z = 4
    A = unknown(x, y, z)
    print(A)

    B = [1, 3, 6, 8, 12]
    C = unknown2(B)
    print(B)

if __name__ == "__main__":
    main()