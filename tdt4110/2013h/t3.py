
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

def secret3(code):
    L = len(code) - 1
    if L >= 0:
        if code[L] == '0':
            decode = '0000'
        elif code[L] == '1':
            decode = '0001'
        elif code[L] == '2':
            decode = '0001'
        elif code[L] == '3':
            decode = '0011'
        elif code[L] == '4':
            decode = '0100'
        elif code[L] == '5':
            decode = '0101'
        elif code[L] == '6':
            decode = '0110'
        elif code[L] == '7':
            decode = '0111'
        elif code[L] == '8':
            decode = '1000'
        elif code[L] == '9':
            decode = '1001'
        elif code[L] == 'A':
            decode = '1010'
        elif code[L] == 'B':
            decode = '1011'
        elif code[L] == 'C':
            decode = '1100'
        elif code[L] == 'D':
            decode = '1101'
        elif code[L] == 'E':
            decode = '1110'
        elif code[L] == 'F':
            decode = '1111'
        else:
            decode = 'XXXX'
        if L == 0:
            return decode
        else:
            return secret3(code[0:L]) + decode
    else:
        return ''

def main():
    print(secret1(11, 3))

    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    answer = secret2(m)
    print(answer)

    print(secret3('148'))

if __name__ == "__main__":
    main()
