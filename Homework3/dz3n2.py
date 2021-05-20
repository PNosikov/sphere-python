from functools import reduce
from operator import add
from operator import setitem
import string
import re


def solution1(arg):
    return list(map(lambda y: int(str(re.sub('[^0-9]', '', y))[::-1]), arg))


def solution2(arg):
    return list(map(lambda y: y[0]*y[1], arg))


def solution3(arg):
    return list(filter(lambda y: (y % 6 in [0, 2, 5]), arg))


def solution4(arg):
    return list(filter(bool, arg))


def solution5(rooms):
    rooms = list(map(lambda x: setitem(x, 'square', x['width']*x['length']), rooms))
    return rooms


def solution6(rooms):
    return list(map(lambda x: dict(x, square=x['width'] * x['length']), rooms))


def solution7(arg):
    return reduce(lambda x, y: x.intersection(y), arg)


def solution8(arg):
    return reduce(lambda d, y: setitem(d, y, d.pop(y, 0) + 1) or d, arg, {})


def solution9(students):
    return list(map(lambda y: y['name'], list(filter(lambda d: d['gpa'] > 4.5, students))))


def solution10(arg):
    return list(filter(lambda y: sum(list(map(int, y[::2]))) == sum(list(map(int, y[1::2]))), arg))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}

# rooms = [
#    {"name": "комната1", "width": 2, "length": 4},
#   {"name": "комната2", "width": 2.5, "length": 5.6},
#    {"name": "кухня", "width": 3.5, "length": 4},
#    {"name": "туалет", "width": 1.5, "length": 1.5},
# ]

# students = [
#    {'name': 'Alina', 'gpa': 4.57},
#    {'name': 'Sergey', 'gpa': 5.0},
#    {'name': 'Nastya', 'gpa': 4.21},
#    {'name': 'Valya', 'gpa': 4.72},
#    {'name': 'Anton', 'gpa': 4.32},
# ]

# print(solution10(['165033', '477329', '631811', '478117', '475145', '238018', '917764', '394286']))
