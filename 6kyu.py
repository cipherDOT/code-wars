def find_it(seq):
    for n in seq:
        if seq.count(n) % 2 != 0:
            return n


def digital_root(n):
    num = str(n)
    if len(num) == 1:
        return int(num)
    else:
        sum = 0
        for i in num:
            sum += int(i)

        return digital_root(sum)


def solution(number):
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum


def soln(s):
    res = []
    if len(s) % 2 != 0:
        s += '_'

    for i in range(0, len(s), 2):
        res.append(f'{s[i]}{s[i + 1]}')

    return res


def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


def count_bits(n):
    br = bin(n).replace('0b', '')
    count = 0
    for b in br:
        if b == '1':
            count += 1

    return count


def alphabet_position(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letnum = dict()
    for ind, let in enumerate(letters):
        letnum[let] = ind + 1

    for l in text:
        if not l.isalpha():
            text = text.replace(l, '')

    for l in text:
        text = text.replace(l, f'{str(letnum[l.lower()])} ')

    return text[:-1]


def array_diff(a, b):
    return [x for x in a if x not in b]


def create_phone_number(n):
    return f'({str(n[0]) + str(n[1]) + str(n[2])}) {str(n[3]) + str(n[4]) + str(n[5])}-{str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])}'


def matrix_addition(a, b):
    soln = []
    for i in range(len(a)):
        soln.append([])
        for j in range(len(a[0])):
            soln[i].append(a[i][j] + b[i][j])

    return soln


def persistence(n):
    # persistence of a number = 1 + persistence(product on it's digits) => recursion
    if len(str(n)) <= 1:
        return 0
    else:
        prd = 1
        for l in str(n):
            prd *= int(l)

        return 1 + persistence(prd)
