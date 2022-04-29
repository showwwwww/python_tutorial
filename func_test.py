from functools import reduce

# get parameter count
# def howlong(first, *other):
#     print(1 + len(other))
#
#
# howlong(123, 234, 456)
#
# var1 = 123
#
#
# def func():
#     global var1
#     var1 = 456
#     print(var1)
#
#
# func()
# print(var1)


# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))  # StopIteration Error

# for i in range(10, 20, 2):
#     print(i)

# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
#
#
# for i in frange(10, 20, 0.5):
#     print(i)


# def func2(item):
#     return item[1]
#
#
# adict = {'a': 'aa', 'b': 'bb'}
# for i in adict.items():
#     func2(i)

# a = [1, 2, 3, 4, 5, 6, 7]
# print(list(filter(lambda x: x > 2, a)))
# print(list(map(lambda x: x + 1, a)))
# b = [4, 5, 6]
# print(list(map(lambda x, y: x + y, a, b)))
#
# print(reduce(lambda x, y: x + y, [2, 3, 4], 1))
#
# for i in zip((1, 2, 3), (4, 5, 6)):
#     print(i)

# dicta = {'a': 'aa', 'b': 'bb'}
# dictb = zip(dicta.values(), dicta.keys(), dicta.values())
# print(list(dictb))


def func():
    a = 1
    b = 2
    return a + b


def func2(a, b):
    def add(c):
        return a + c
    return add(b)


num1 = func()
num2 = func2(2, 1)

print(type(num1))
print(type(num2))

