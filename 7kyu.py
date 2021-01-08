
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

def uncensor(i, d):
    c = 0
    for l in i:
        if l == '*':
            i = i.replace('*', d[c], 1)
            c += 1
            
    return i

def after(nums):
    r = []
    for i in nums:
        if nums.count(i) > 1:
            continue
        else:
            if i % 2 == 0:
                r.append(i)
        if i == 237:
            break
            
    return r

def caesar_encode(phrase, shift):
    words = phrase.split(' ')
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    for ind, word in enumerate(words):
        w = ''
        for l in word:
            w += alphas[(alphas.index(l) + shift) % 26]
            
        words[ind] = w
        shift += 1
        
    return ' '.join(w for w in words)

def check_parity(parity, bin_str): 
    s = bin_str.count('1')
    if (s % 2 == 0 and parity == 'odd') or (s % 2 != 0 and parity == 'even'):
        return 1
    else:
        return 0
    
def solution(n):
    r = [4,7]
    try:
        r.remove(n)
        return r[0]
    except:
        return False
    
def single_digit(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    else:
        a = eval('+'.join(i for i in bin(int(n))[2:]))
        return single_digit(a)

def make_checkered_board(n):
    r = []
    count = 0
    for i in range(n):
        r.append([])
        for j in range(n):
            if (count + j) % 2 == 0:
                r[i].append('X')
            else:
                r[i].append('O')
        count += 1
                
    return r

def get_product_id(url): 
    return url.split('/')[-1].split('-')[-2]

def divisible_by_last(n):
    n = str(n)
    r = [False]
    for i in range(1, len(n)):
        try:
            r.append(int(n[i]) % int(n[i - 1]) == 0)
        except:
            r.append(False)
    return r

def score_to_tally(score):
    n = dict()
    tallies = ['', 'a', 'b', 'c', 'd', 'e']
    for i in range(6):
        n[i] = tallies[i]
    r = ''
    if score >= 5:
        r +=  ' <br>'.join('e' for _ in range(score // 5)) + ' <br>'
    r += n[score % 5]
    return r
