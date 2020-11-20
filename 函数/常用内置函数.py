# 数据类型相关

# 内置函数	功能	示例	示例结果
# dict()	将参数转换为字典类型	dict(a=1, b=2, c=3)	{'a': 1, 'b': 2, 'c': 3}
# float()	将字符串或数字转换为浮点型	float('0.22')	0.22
# int()	将字符串或数字转换为整数型	int(1.23)	1
# list()	将元组、字符串等可迭代对象转换为列表	list('abc')	['a', 'b', 'c']
# tuple()	将列表、字符串等可迭代对象转换为元组	tuple([1, 2, 3])	(1, 2, 3)
# set()	1.创建空集合；2.将可迭代对象转换为列表集合	set('abc')	{'b', 'a', 'c'}
# str()	将参数转换为字符串	str(3.14)	'3.14'
# bytes()	将参数转换为字节序列	bytes(4)	b'\x00\x00\x00\x00

# 数值计算相关

# 内置函数	功能	示例	示例结果
# max()	求最大值	max([13, 2, 0.6, -51, 7])	13
# min()	求最小值	min([13, 2, 0.6, -51, 7])	-51
# sum()	求和	sum([13, 2, 0.6, -51, 7])	-28.4
# abs()	求绝对值	abs(-51)	51
# pow()	求次方	pow(2, 10)	1024
# bin()	转换为二进制	bin(77)	'0b1001101' （注意结果为字符串）
# hex()	转换为十六进制	hex(77)	'0x4d' （注意结果为字符串）
# round()	浮点数四舍五入	round(4.5678, 2) （第二个参数为小数精度）	4.57

# bool 值判断相关

# 内置函数	功能
# bool()	判断参数是否为真，为真则返回 True，否则返回 False。「为真」指的是，表达式的结果为布尔值 True，或非零数字，或非空字符串，或非空列表
# all()	如果可迭代对象中的所有值，在逐一应用 bool(值) 后结果都为 True，则返回 True，否则返回 False
# any()	如果可迭代对象中的任意一个或多个值，在应用 bool(值) 后结果为 True，则返回 True，否则返回 False
bool(2)
True
bool(0)
False
bool([1, 2, 3])
True
bool([])
False
bool('abc')
True
bool('')
False

all(['a', 1, [1]])
True
all(['a', 0, [1]])
False

any(['', 0, []])
False
any(['a', 0, []])
True

# IO 相关

# IO 即输入输出。

# 内置函数	功能
# input()	从标准输入中读取字符串
# print()	将内容写入标准输出中
# open()	打开一个文件。之后便可以对文件做读写操作。详见 IO 操作章节
# 元数据相关

# 内置函数	功能
# type()	获取对象的类型
# isinstance()	判断对象是否是某个类（或其子类）的对象
# dir()	获取类或对象中的所有方法和属性；无参数时获取当前作用域下的所有名字
# id()	返回一个对象的唯一标识。在我们所使用的 CPython 中这个唯一标识实际为该对象在内存中的地址
# isinstance() 示例：

numbers = [1, 2, 3]
isinstance(numbers, list)
# True
isinstance(numbers, str)
# False

# 也可以把多个类型放在元组中，其中一个与对象的类型相符即为 True，若无相符则为 False。如：

numbers = [1, 2, 3]
isinstance(numbers, (list, str))
# True

# dir() 示例：

dir(list)
# [’__add__’, '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__, '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# id() 示例：

number = 1
id(number)
# 4411695232

# help()

# 解释器交互模式下获取某个函数、类的帮助信息，非常实用。

# 比如查看内置函数 any() 的用法：

# 按下 q 键退出上述界面。

# sorted()

# 对可迭代对象中的数据进行排序，返回一个新的列表。

numbers = (4, 5, 2, 8, 9, 1, 0)
sorted(numbers)

sorted(numbers, reverse=True)

codes = [('上海', '021'), ('北京', '010'), ('成都', '028'), ('广州', '020')]
sorted(codes, key=lambda x: x[1])

# range()

# 获取一个整数序列。可指定起始数值，结束数值，增长步长。
# range() 返回的并不是容器，而是可迭代对象
l = range(2,6)
print(list(l))
for i in range(2, 6):
    print(i)
# 注意，生成的数值范围为左开右闭区间，即不包括所指定的结束数值。

# 只指定结束数值，此时起始数值默认为 0
for i in range(4):
    print(i)

# 指定步长（第三个参数）
for i in range(3, 15, 3):
    print(i)