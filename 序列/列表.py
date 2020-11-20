# 列表

# 列表中的数据可以是任意类型的
[100, 'about', True]

# # 存储内容可修改
[0,"abcd"]
# 想要获得列表的长度可以使用 len() 这个东西
fruits = [1,2]
len(fruits)

# # 添加列表元素
a_list=['abc','xyz']
a_list.append('x')
print(a_list)

# # 删除列表元素
a_list.remove('x')
print(a_list)

# 统计元素在列表中的个数，或者说是元素在列表中出现的次数。
numbers = [1, 2, 2, 3, 4, 5, 5, 7]
numbers.count(5)

# 向列表的任意位置插入元素
letters = ['a', 'b']
letters.insert(0, 'c')

# 列表末尾追加另一个列表的所有元素
letters = ['a', 'b']
letters.extend(['c', 'd', 'e'])

# 按索引删除元素
letters.pop(0)
# 也可以不传递索引，这样的话默认删除并返回最后一个元素。
letters.pop()

# 删除一个列表元素也可以使用 Python 中的 del 关键字
del letters[0]

# 直接删除元素
letters.remove('b')

# 清空所有元素
letters.clear()

# 通过赋值修改列表元素
letters[2] = 'd'

# 反转整个列表
letters.reverse()

# 列表元素排序
numbers.sort()
numbers.sort(reverse=True)




