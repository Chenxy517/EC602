# Copyright 2022 XingyuChen chxy517@bu.edu

def divisorsum(n):
    sum = 1
    equation = '1'
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum += i
            equation += '+' + str(i)
    equation += ' = ' + str(sum)
    return equation

def convertbase(s, base1, base2):
    num = 0
    weight = 1
    for i in range(len(s) - 1, -1, -1):
        digit = ord(s[i]) - ord('0')
        num = num + digit * weight
        weight = weight * base1
    output = ''
    while num > 0:
        digit = num % base2
        num = num // base2
        output = chr(digit + ord('0')) + output
    return output

def heavy(y, N):
    visited = []
    while y not in visited:
        visited.append(y)
        y_nxt = 0
        while y > 0:
            digit = y % N
            y = y // N
            y_nxt += digit * digit
        y = y_nxt
        if y == 1:
            return True
    return False

print(convertbase('123:123', 11, 10))