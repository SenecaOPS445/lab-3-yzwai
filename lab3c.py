#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author        : Ye Zin Wai
# Student ID    : yzwai, 133310227

def operate(number1, number2, operator):
    # Place logic in this function
    if operator == 'add':
        return int(number1 + number2)
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return('Error: function operator can be "add", "subtract", or "multiply"')

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))
