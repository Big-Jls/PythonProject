import time
def log(fun):
    def wrapper(x, y):
        start = time.time()
        print(f'开始时间{start}')
        fun(x, y)
        end = time.time()
        print(f'结束时间{end}，相差间隔{end - start}')
    return wrapper


def add(x,y):
    return print(x ** y)

@log
def add2(x,y):
    return print(x ** y)

add(999999999999999999,99)
print('-------------------------')
add2(998888888888889899,99)