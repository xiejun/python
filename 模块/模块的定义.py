# 执行模块时传入参数
# python3 模块文件名 参数1 ...参数n
# import sys

# sys.argv[0] 保存当前被执行模块的文件名
# sys.argv[1] 保存第 1 个参数
# sys.argv[2] 保存第 2 个参数

import sys  # 新增
import tree

print('种下一棵果树。')
tree.fruit_name = sys.argv[1]   # 将 'apple' 改为 参数 sys.argv[1]

print('等啊等，树长大了，可以收获了！')
fruits = tree.harvest()
print(fruits)

