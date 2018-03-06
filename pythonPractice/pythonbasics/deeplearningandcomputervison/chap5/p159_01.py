def say_hello():
    print('Hello Word!')


def greetings(x='Good morning'):
    print(x)
    return x


say_hello()
greetings()
a = greetings('123456')
print(a)


def create_a_list(x, y=2, z=3):
    print([x, y, z])
    return [x, y, z]


b = create_a_list(1)
c = create_a_list(3, 3)
d = create_a_list(6, 7, 8)


def traverse_args(*args):
    for arg in args:
        print(arg)


traverse_args(1, 2, 3)
traverse_args('A', 'B', 'C', 'D')


def traverse_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


traverse_kwargs(x=1, y=2, z=3)
traverse_kwargs(fighter1='Fedor', fighter2='Randleman')


def foo(x, y, *args, **kwargs):
    print(x, y)
    print(args)
    print(kwargs)


foo(1, 2, 3, 4, 5, a=6, b=7, c=8)
