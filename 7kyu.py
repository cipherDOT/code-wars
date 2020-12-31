
import math


def solution(stones):
    rem = 0
    for i in range(len(stones) - 1):
        if stones[i] == stones[i + 1]:
            rem += 1

    return rem


def reverse(n):
    return int(str(n)[::-1])


def get_count(input_str):
    count = 0
    for letter in input_str:
        if letter in 'aeiou':
            count += 1

    return count


def get_middle(s):
    # using recursion
    if len(s) <= 2:  # base case
        return s
    else:  # recursion case
        return get_middle(s[1:-1])


def even_or_odd(s):
    odds = []
    evens = []
    for n in s:
        if int(n) % 2 == 0:
            evens.append(int(n))
        else:
            odds.append(int(n))

    even_sum = sum(evens)
    odd_sum = sum(odds)

    if even_sum > odd_sum:
        return 'Even is greater than Odd'
    elif even_sum < odd_sum:
        return 'Odd is greater than Even'
    else:
        return 'Even and Odd are the same'


def remove_bmw(string):
    try:
        for letter in string:
            if letter.lower() in 'bmw':
                string = string.replace(letter, '')

        return string

    except:
        return "This program only works for text."


def binary_array_to_number(arr):
    result = 0
    power = 0

    for bit in arr[::-1]:
        result += bit*(2**power)
        power += 1

    return result


def calc_ms(n):
    return 20 ** n


def square_digits(num):
    res = ''
    for n in str(num):
        res += str(int(n) ** 2)

    return int(res)


def solve(arr):
    res = []
    while len(arr) > 0:
        if len(arr) == 1:
            res.append(arr[0])
            break

        else:
            max_arr = max(arr)
            min_arr = min(arr)
            res.append(max_arr)
            res.append(min_arr)
            arr.remove(max_arr)
            arr.remove(min_arr)

    return res


def next_perfect_square(n):
    try:
        n = math.floor(math.sqrt(n))
    except:
        return 0

    return (n + 1)**2


def high_and_low(numbers):
    s = ''
    num = list(int(i) for i in numbers.split(' '))
    num.sort()
    s += str(num[-1]) + ' ' + str(num[0])
    return s
