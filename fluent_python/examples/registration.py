# Example 7-2. The registration.py module.
registery = []


def register(func):
    print("running register(%s)" % func)
    registery.append(func)
    return func


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():
    print("running f3()")


if __name__ == "__main__":
    print("running main()")
    print("registery ->", registery)
    f1()
    f2()
    f3()
