# 创建包含元素的集合
# 集合 = {元素1, 元素2, 元素N}
numbers = {1, 2, 3}

# 创建空集合
empty_set = set()

# 向集合中添加一个元素
numbers.add(3)

# 向集合中添加重复元素时，会被去重处理。
numbers = {1, 2}
numbers.add(2)

# 从另一集合中批量添加元素
# 集合.update(另一集合)
numbers_1 = {1, 2}
numbers_2 = {2, 3, 4}
numbers_1.update(numbers_2)

# 查看元素是否存在于集合中
# 布尔值 = 元素 in 集合
letters = {'a', 'b', 'c'}
'a' in letters

# 集合元素的删除
# 随机删除一个元素，并返回这个元素
# 元素 = 集合.pop()
numbers = {1, 2, 3}
numbers.pop()
# 删除一个指定的元素
# 如果要删除的元素不存在，则抛出 KeyError 异常：
numbers.remove(1)
# 删除一个指定的元素，且不抛出 KeyError 异常
# 集合.discard(元素)
numbers.discard(4)


