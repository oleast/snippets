#!/usr/bin/python3

def task_a():
    '''
    a) Nice onliner :P
    ''' 
    solution = sum([(x%2*2-1)*x**2 for x in range(int(input('n = '))+1)])
    answer = f'Summen av tallserien er {solution}'
    print(answer)

def task_b():
    k = int(input('k = '))
    solution = 0
    iterations = 0
    x = 0
    while True:
        x += 1
        if x % 2:
            next_solution = x**2
        else:
            next_solution = -x**2
        if solution + next_solution > k:
            break
        iterations += 1
        solution += next_solution

    answer = f'Summen av tallene før summen blir større enn k er {solution}. Antall iterasjoner: {iterations}'
    print(answer)

if __name__ == "__main__":
    task_a()
    task_b()
