import math


def warn_the_sheep(queue):
    queue = queue[::-1]
    if queue.index('wolf') != 0:
        return f"Oi! Sheep number {str(queue.index('wolf'))}! You are about to be eaten by a wolf!"
    else:
        return "Pls go away and stop eating my sheep"


def areYouPlayingBanjo(name):
    return f'{name} plays banjo'if name.lower()[0] == 'r' else f'{name} does not play banjo'


def array_plus_array(arr1, arr2):
    res = 0
    final = arr1 + arr2
    for number in final:
        res += number
    return res


def past(h, m, s):
    return h*3600000 + m*60000 + s*1000


def cockroach_speed(s):
    return math.floor(s * 27.778)


def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0


def capitalize_word(w):
    return w.capitalize()


def check_exam(arr1, arr2):
    res = 0
    for ans, choice in zip(arr1, arr2):
        if ans == choice:
            res += 4
        elif choice == '':
            pass
        else:
            res -= 1

    return res if res > 0 else 0


def even_or_odd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


def arr(n=0):
    res = []

    for i in range(n):
        res.append(i)

    return res


def square(n):
    return n * n


def flip(d, a):
    if d == 'R':
        return sorted(a)
    else:
        return sorted(a)[::-1]


def hello(name=''):
    if name == '':
        return 'Hello, World!'
    else:
        return f'Hello, {name.capitalize()}!'


def hero(b, d):
    return b >= d*2


def index(array, n):
    try:
        return array[n]**n
    except:
        return -1


def double_integer(i):
    return i*2


def enough(cap, on, wait):
    return 0 if (on + wait) <= cap else abs((on + wait) - cap)

def position(a):
    al = 'abcdefghijklmnopqrstuvwxyz'
    return f'Position of alphabet: {al.index(a) + 1}'

def add_five(num):
    return num + 5

boolean_to_string = lambda s:str(s)

def count_sheeps(sheep):
    return sheep.count(True)
