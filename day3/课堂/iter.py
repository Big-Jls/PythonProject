""""""
"""
Iterable:可迭代，可以使用for循环，内部实现了__iter__方法
Iterator:迭代器，可迭代，内部实现了__iter__和__next__
迭代器一定可迭代，可迭代对象不一定是迭代器。
Generator:生成器，节省内存
"""
from collections.abc import Iterable, Iterator, Generator


class Color(Generator):

    def __init__(self):
        self.colors = ['red', 'white', 'black', 'green']

    # 仅仅是实现了__iter__ 方法,在方法内部什么都不做
    def __iter__(self):
        pass

    def __next__(self):
        pass




color_object = Color()
# 判断是否为可迭代对象
print(isinstance(color_object, Iterable))  # True
# 判断是否为迭代器
print(isinstance(color_object, Iterator))  # True

print(isinstance(color_object, Generator))  # True
