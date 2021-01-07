
from math import floor


def is_anagram(word, other):
    for l in other:
        if word.count(l) != other.count(l):
            return False
    return True


def anagrams(word, words):
    angs = []
    for w in words:
        if is_anagram(word, w):
            angs.append(w)

    return angs


def rgb(r, g, b):
    hexdict = {
        0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
        8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
    }

    # constraining the values between 0 and 255
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255

    hr = r / 16
    hg = g / 16
    hb = b / 16

    # converting it into hex
    return f'{hexdict[floor(hr)]}{hexdict[16 * (hr - floor(hr))]}{hexdict[floor(hg)]}{hexdict[16 * (hg - floor(hg))]}{hexdict[floor(hb)]}{hexdict[16 * (hb - floor(hb))]}'


def weight(n):
    r = 0
    for i in n:
        r += int(i)

    return r


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def order_weight(s):
    w = s.split(' ')
    w.sort(key=weight)
    n = len(w)

    # using the bubblesort algorithm to swap equal value
    # based on their string comparisions
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if weight(w[j]) == weight(w[j + 1]):
                if str(w[j]) > str(w[j + 1]):
                    swap(w, j, j + 1)

    return ' '.join(n for n in w)


def make_readable(seconds):
    sec = 0
    min = 0
    hr = 0
    for _ in range(seconds):
        sec += 1
        if sec >= 60:
            sec = 0
            min += 1

        if min >= 60:
            min = 0
            hr += 1

    return f'{str(hr).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}'


def scramble(s1, s2):
    for s in set(s2):
        if s1.count(s) < s2.count(s):
            return False
    return True


def rot13(message):
    if not message:
        return message
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    rotdict = dict()
    for l in alphabets:
        rotdict[l] = alphabets[(alphabets.index(l) + 13) % 26]
        rotdict[l.upper()] = alphabets[(alphabets.index(l) + 13) % 26].upper()

    new_message = ''
    for l in message:
        if l.isalpha():
            key = rotdict[l]
        else:
            key = l
        new_message += key

    return new_message


def first_non_repeating_letter(string):
    c = string.lower()
    for l in c:
        if c.count(l) == 1:
            return string[c.index(l)]

    return ''


def alphanumeric(p):
    return p.isalnum()


def how_many_times(a, b):
    if a == b:
        return a
    a, b = min(a, b), max(a, b)
    output = 0
    while a > 0:
        if b % a == 0:
            output += 1
        subtract = int(b / (int(b / a) + 1))
        a, b = subtract, b - (a - subtract)
    return output


def valid_parentheses(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            if count > 0:
                count -= 1
            else:
                return False

    return count == 0


def increment_string(s):
    r = ''
    for i in s[::-1]:
        if i.isdigit():
            r += i
        else:
            break
    r = r[::-1]
    s = s.replace(r, '')
    n = int(r) if r else 0
    s += str(n + 1).zfill(len(r))
    return s


def pig_it(text):
    words = text.split(' ')
    new = []
    for word in words:
        if word.isalpha():
            f = word[0]
            word = word.replace(f, '', 1)
            word = word + f + 'ay'
        new.append(word)

    return ' '.join(word for word in new)


def generate_hashtag(s):
    c = True
    if not s:
        return False
    else:
        s = s.strip()
        s = s.split(' ')
        hash = '#' + ''.join(w.capitalize() for w in s if w.isalpha())
        if len(hash) > 140:
            return False
        else:
            return hash


def move_zeros(arr):
    n = len(arr)

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    # using the bubble sort algorithm
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # since False is processed as a zero we need to input types.
            if type(arr[j]) == int or type(arr[j]) == float:
                if int(arr[j]) == 0:
                    arr[j] = 0
                    swap(arr, j, j + 1)

    return arr


def zeros(n):
    count = 0
    i = 5

    while (n / i >= 1):
        count += int(n/i)
        i *= 5

    return int(count)


def ips_between(start, end):
    start = [int(i) for i in start.split('.')]
    end = [int(i) for i in end.split('.')]
    start = start[0]*256**3 + start[1]*256**2 + start[2]*256 + start[3]
    end = end[0]*256**3 + end[1]*256**2 + end[2]*256 + end[3]
    return end - start

import numpy as np

def is_solved(b):
    # TODO: Check if the board is solved!
    b = np.array(b)
    print(b)
    if b[0][0] == b[1][1] == b[2][2]:
        if b[0][0] != 0:
            return b[0][0]
        else:
            return -1
    elif b[0][2] == b[1][1] == b[2][0]:
        if b[0][2] != 0:
            return b[0][2]
        else:
            return -1
    else:
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2]:
                if b[i][0] != 0:
                    return b[i][0]
            elif b[0][i] == b[1][i] == b[2][i]:
                if b[0][i] != 0:
                    return b[0][i]
        if 0 in b.flatten():
            return -1
        else:
            return 0
    
