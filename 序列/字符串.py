
# 字符串
"abc"

# 字符串类型的值是不可变的（Immutable），我们不能在原地修改它其中的某个字符。

# 通过子串获取索引
string = 'happy'
string.index('p')
# 使用方式与 index 一致，不同点在于 find 方法未找到子串时返回数字 -1，而不抛异常
string.find('app')

# startswith：判断字符串是否以某个子串开头，返回布尔值
string.startswith('ha')
# endswith：判断字符串是否以某个子串结尾，返回布尔值
string.endswith('y')
string.replace('y', 'iness')
# strip：去除字符串前后的空白符号，如空格、换行符、制表符，返回一个新的字符串
string.strip()
# split：将字符串用某个子串分隔开，分隔后的各个部分放入列表中，并返回这个列表
string.split(' ')

words=['a','b','c']
''.join(words)
string.upper()
string.lower()

#  字符转义
print('第一行\n第二行')

# 原始字符串
print(r'第一行\n第二行')

# 多行字符串
string = '第一行\
第二行\
第三行'

# 如果想要输出内容为多行，需要在字符串中显式地使用 \n 进行换行。
string = '第一行\n\
… 第二行\n\
… 第三行'

# 使用三个单引号或三个双引号来表示字符串
# 这样字符串中的内容就可以多行书写，并且被多行输出。
string = '''第一行
第二行
第三行'''



# 查看字符是否存在于字符串中
'a' in string

# # 切片操作符
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
print(chinese_zodiac[0:4])
print(chinese_zodiac[-1])
year = 2020
print(chinese_zodiac[year%12])

# # 成员关系操作符
print("狗" in chinese_zodiac)

# # 连接操作符
print(chinese_zodiac + chinese_zodiac)

# # 重复操作符
print(chinese_zodiac*3)

# 字符串格式化
first_name = '1'
last_name = '2'
print(f'{first_name},{last_name}')

