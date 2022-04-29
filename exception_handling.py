# i = j
# NameError

# print(()
# SyntaxError

# a = "123"
# print(a[3])
# IndexError

# d = {'a': 1, 'b': 2}
# print(d['c'])
# KeyError

# year = int(input("input year: "))
# ValueError if input a string

# def test():
#     try:
#         year = int(input("input year: "))
#     except ValueError:
#         print("年份要输入数字!")
#     finally:
#         test()
#
#
# test()

# a = 123
# a.append()
# AttributeError

# except (ValueError, AttributeError, KeyError)

# try:
#     print(1 / 'a')
# except Exception as e:
#     print("0不能做除数 %s" % e)

try:
    raise NameError("helloError")
except NameError as e:
    print("my custom error %s" % e)
