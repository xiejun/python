
# 字符串
"abc"
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

