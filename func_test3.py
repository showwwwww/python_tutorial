
def a_line(a, b):
    return lambda x: a * x + b


line1 = a_line(3, 5)
print(line1(10))
