
def fu1(a: int) -> int:
    r = 0
    while a > 0:
        s = a % 10
        r = r + s
        a = (a-s) / 10
    return r

def fu2(_input: str) -> float:
    r = 0
    s = 0
    t = 0
    u = 0
    n = len(_input)
    for c in _input:
        if c.isalpha():
            r = r + 1
        elif c.isdigit():
            s = s + 1
        elif c == ' ':
            t = t + 1
        else:
            u = u + 1
    r = 100*r/n
    s = 100*s/n
    t = 100*t/n
    u = 100*u/n
    return(r,s,t,u)

def fu3(a: int) -> int:
    if a <= 2:
        r = 1
    else:
        r = 1 + fu3(a/2)
    return r

def main():
    print(fu1(1234))
    print(fu2('Ut pa tur, aldri sur'))
    print(fu3(100))

if __name__ == "__main__":
    main()
