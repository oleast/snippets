#!/usr/bin/python3

def task_a():
    '''
    a)
    '''
    s = 0
    for i in range(7):
        integer = int(input('Skriv inn et heltall: '))
        s += integer
    print('Summen av tallene ble', s)

def task_b():
    '''
    b) The sum of the numbers 1, 2, 3 ... sum < 1000
    '''
    product = 1
    i = 1
    while product <= 1000:
        i += 1
        product *= i
    print('Produkt over 1000 =>', product)

def task_c():
    '''
    c)
    '''
    attempts = 1
    answer = input('Hva er hovedstaden i Norge? ')
    while answer.lower() != 'oslo':
        attempts += 1
        print('Det var feil, prøv igjen.')
        answer = input('Hva er hovedstaden i Norge? ')
    print(f'Korrekt!! Du brukte {attempts} forsøk.')

if __name__ == "__main__":
    task_a()
    task_b()
    task_c()
