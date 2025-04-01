from sys import getsizeof

# 生成器，节省内存，惰性求值
# 优点： 节省空间
# 缺点： 惰性求值，只能去取一次值，不能使用索引，只能挨个取值
list1 = [i for i in range(10000)]
print(list1)
print(type(list1), getsizeof(list1))

"""写法1.元组推导式"""
t = (i for i in range(10000))
print(type(t), getsizeof(t))

"""写法2.yield关键字"""


def generator():
    yield 10
    yield 100
    return 0, 1


g = generator()
try:
    while True:
        print(next(g))
except StopIteration as e:
    print(f'迭代出错{e}')
except Exception as e:
    print(f'其他错误{e}')
