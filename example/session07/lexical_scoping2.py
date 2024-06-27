i = 4


def foo(x):
    def bar():
        print(i)

    for i in x:
        print(i)
    bar()


foo([1, 2, 3])
