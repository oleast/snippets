#!/usr/bin/python3

import math

def f(x):
    return math.exp(x**2)

def midpoint_rule(function, a, b, intervals):
    solution = 0
    h = (b - a) / intervals
    for k in range(intervals):
        midpoint = a + k*h + h*.5
        solution += f(midpoint)
    return solution * h

def simpsons_rule(function, a, b, intervals):
    solution = f(a)
    h = (b - a) / (intervals * 2)
    for k in range(1, intervals * 2):
        x = a + k*h
        if k % 2:
            solution += 4 * f(x)
        else:
            solution += 2 * f(x)
    solution += f(b)
    return solution * h / 3

def get_inputs():
    a = int(input('Enter starting point a: '))
    b = int(input('Enter stopping point b: '))
    intervals = int(input('Enter number of intervals N: '))
    return a, b, intervals

def task_a(a, b, intervals):
    ''' a) Midpoint rule '''
    solution = midpoint_rule(f, a, b, intervals)
    answer = f'The integral from {a} to {b} using {intervals} intervals is {solution}'
    print(answer)

def task_b(a, b, intervals):
    ''' b) Simpson's rule '''
    solution = simpsons_rule(f, a, b, intervals)
    answer = f'The integral from {a} to {b} using {intervals} intervals is {solution}'
    print(answer)

def task_c(a, b, intervals):
    ''' c) Error between midpoint and simpson's rule '''
    correct = 1.462651745907181
    error_m = abs(midpoint_rule(f, a, b, intervals) - correct)
    error_s = abs(simpsons_rule(f, a, b, intervals) - correct)
    answer_m = f'The integration error using the midpoint method with {intervals} intervals is {error_m}'
    print(answer_m)
    answer_s = f'The integration error using Simpson\'s method with {intervals} intervals is {error_s}'
    print(answer_s)

if __name__ == "__main__":
    a, b, intervals = get_inputs()
    task_a(a, b, intervals)
    task_b(a, b, intervals)
    task_c(a, b, intervals)
