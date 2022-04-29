def new_tips(argv):
    def tips(func):
        def inner(a, b):
            print('start %s %s' % (argv, func.__name__))
            func(a, b)
            print('stop')
        return inner
    return tips


@new_tips('add_module')
def add(a, b):
    print(a + b)


@new_tips('del')
def sub(a, b):
    print(a - b)


add(4, 5)
