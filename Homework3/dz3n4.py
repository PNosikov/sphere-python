import functools


def counter(func):
    counter.rdepth = 0
    counter.maxdepth = 0
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if (counter.rdepth == 0):
            counter.maxdepth = 0
            wrapper.ncalls = 0
        wrapper.ncalls += 1
        counter.rdepth += 1
        if (counter.rdepth > counter.maxdepth):
            counter.maxdepth = counter.rdepth
        wrapper.rdepth = counter.maxdepth
        res = func(*args, **kwargs)
        counter.rdepth -= 1
        return res
    wrapper.ncalls = 0
    wrapper.rdepth = 0
    return wrapper


# @counter
# def func2(n, steps):
#     if steps == 0:
#         return
#
# func2(n + 1, steps - 1)
# func2(n - 1, steps - 1)
#
# if __name__ == "__main__":
#     func2(0, 5)
#     print(func2.ncalls, func2.rdepth)
#
#     func2(0, 3)
#     print(func2.ncalls, func2.rdepth)
