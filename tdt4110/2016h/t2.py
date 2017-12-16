
def flopp(mat):
    r = len(mat)
    c = len(mat[0])
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 1:
                mat[i][j] = 0
            else:
                mat[i][j] = 1
    return mat

def compute(d, m, y):
    M = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
    N = ('st', 'nd', 'rd', 'th')
    x = (d % 30) % 20 - 1
    if x > 3 or x == -1:
        x = 3
    return str(d) + N[x] + ' ' + M[m-1] + ' ' + str(y)

def fr(s):
    f = [0] * 26
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            f[ord(s[i]) - ord('a')] += 1
    a = max(f)
    b = chr(f.index(a) + ord('a'))
    return a, b

def f(x):
    y = 0
    while x > 0:
        y = y + x % 10
        x = int(x / 10)
    if y >= 10:
        y = f(y)
    return y

def main():
    M = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    print(flopp(M))

    print(compute(30, 11, 1337))

    print(fr('abcbcbd'))

    print(f(32145))

if __name__ == "__main__":
    main()
