
def secret1(a, b):
    r = 0
    while a >= b:
        a = a - b
        r = r + 1
    s = a
    return r, s

def secret2(m):
    r = len(m)
    c = len(m[0])
    if r == c:
        for i in range(0, r-1):
            for j in range(i+1, c):
                temp = m[i][j]
                m[i][j] = m[j][i]
            m[j][i] = temp
        return m
    else:
        return -1

def main():
    print(secret1(11, 3))

    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    answer = secret2(m)
    print(answer)

if __name__ == "__main__":
    main()
