# 迭代器（Iterator）

# 迭代器是具有迭代功能的对象。我们使用迭代器来进行迭代操作。

# 列表、元组、字符串、集合、字典这些容器之所以能被迭代，是因为对它们调用内置函数 iter() 将返回一个迭代器，这个迭代器可被用于迭代操作。
# iter() 的使用方法：

# 迭代器 = iter(容器)
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
# 要使用迭代器，只需对迭代器调用内置函数 next()，便可逐一获取其中所有的值。

# next() 的使用方法：

# 值 = next(迭代器)
next(iterator)
next(iterator)

# for 循环的迭代过程

# for 循环的迭代就是通过使用迭代器来完成的。它在背后所做的事情是：

# 对一个容器调用 iter() 函数，获取到该容器的迭代器
# 每次循环时对迭代器调用 next() 函数，以获取一个值
# 若捕获到 StopIteration 异常则结束循环

# 什么是可迭代(的)？

# 从表面来看，所有可用于 for 循环的对象是可迭代的，如列表、元组、字符串、集合、字典等容器
# 从深层来看，定义了 __iter__() 方法的类对象就是可迭代的。当这个类对象被 iter() 函数使用时，将返回一个迭代器对象。如果对象具有__iter__() 方法，则可以说它支持迭代协议。

# 判断一个已有的对象是否是可迭代的，有两个方法：
# 通过内置函数 dir() 获取这个对象所有方法，检查是否有 '__iter__'
'__iter__' in dir(list)
#  使用内置函数 isinstance() 判断其是否为 Iterable 的对象
# from collections.abc import Iterable
# isinstance(对象, Iterable)
from collections.abc import Iterable
isinstance([1, 2, 3], Iterable)

# 自定义迭代器

# 我们可以自己来定义迭代器类，只要在类中定义 __next__() 和 __iter__() 方法即可。如：
# class MyIterator:
#     def __next__(self):
#         pass

#     def __iter__(self):
#         return self

class PowerOfTwo:
    def __init__(self):
        self.exponent = 0  					# 将每次的指数记录下来

    def __next__(self):
        if self.exponent > 10:
            raise StopIteration
        else:
            result = 2 ** self.exponent		# 以 2 为底数求指数幂
            self.exponent += 1
            return result

    def __iter__(self):
        return self

# 迭代器的好处

# 一方面，迭代器可以提供迭代功能，当我们需要逐一获取数据集合中的数据时，使用迭代器可以达成这个目的
# 另一方面，数据的存储是需要占用内存的，数据量越大所占用的内存就越多。如果我们使用列表这样的结构来保存大批量的数据，并且数据使用频率不高的话，就十分浪费资源了。而迭代器可以不保存数据，它的数据可以在需要时被计算出来（这一特性也叫做惰性计算）。在合适的些场景下使用迭代器可以节省内存资源。

# 生成器（Generator）

# 刚才我们自定义了迭代器，其实创建迭代器还有另一种方式，就是使用生成器。

# 生成器是一个函数，这个函数的特殊之处在于它的 return 语句被 yield 语句替代。
def power_of_two():
	for exponent in range(11):	# range(11) 表示左闭右开区间 [0, 11)，不包含 11
		yield 2 ** exponent		# 以 2 为底数求指数幂

p = power_of_two()				# 以函数调用的方式创建生成器对象
next(p)							# 同样使用 next() 来取值

# 这是因为生成器其实就是创建迭代器的便捷方法，生产器会在背后自动定义 __iter__() 和 __next__() 方法。

# 生成器表达式（Generator Expression）

# 可以用一种非常简便的方式来创建生成器，就是通过生成器表达式。生成器的写法非常简单，但是灵活性也有限，所能表达的内容相对简单。

# 生成器表达式的写法如下：

# 生成器 = (针对项的操作 for 项 in 可迭代对象)
letters = (item for item in 'abc')
letters
next(letters)
next(letters)

letters = (i.upper() * 2 for i in '')
next(letters)

