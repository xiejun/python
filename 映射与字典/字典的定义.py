#映射的类型：字典
# 字典包含哈希值和指向的对象
{'哈希值':'对象'}
{'length':1,'width':2}
dict1 = {}
print(type(dict1))
dict2={'x':1,'y':2}
dict2['z']=3
print(dict2)

# 如果通过键获取值时不希望 KeyError 异常抛出，可以使用 get 方法，若键不存在，则直接返回 None。
codes = {'beijing': '010', 'shanghai': '021'}
codes.get('a')
# 也可以给 get 方法传递第二个参数作为默认值，使得键不存在时直接返回默认值。
# 值 = 字典.get(键, 默认值)
codes.get('a', '000')

# 判断字典中是否包含某个键
# 布尔值 = 键 in 字典
codes = {'beijing': '010', 'shanghai': '021'}
'beijing' in codes

# 获取所有键
codes = {'beijing': '010', 'shanghai': '021'}
codes.keys()

# 可以用 list() 函数将迭代器转换为列表
print(list(codes.keys()))

# 获取所有值
codes = {'beijing': '010', 'shanghai': '021'}
codes.values()
print(list(codes.values()))

# 获取所有键值对的列表
codes = {'beijing': '010', 'shanghai': '021'}

# 获取到的所有键值对是以迭代器的形式存在，我们用 list() 函数将迭代器转换为列表
print(list(codes.items()))


chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiac_name = ('摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座',
                '处女座','天秤座','天蝎座','射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

dict_cz_num = {}
for i in chinese_zodiac:
    dict_cz_num[i]=0

dict_z_num = {}
for i in zodiac_name:
    dict_z_num[i] = 0

while True:
    int_year = int(input('输入年份:'))
    int_month = int(input('输入月份:'))
    int_day = int(input('输入日期:'))

    n = 0
    while zodiac_days[n] < (int_month,int_day):
        if int_month == 12 and int_day > 23:
            break
        n += 1
    print(zodiac_name[n])

    print(f'{int_year}年的生肖是{chinese_zodiac[int_year%12]}')
    dict_cz_num[chinese_zodiac[int_year%12]] += 1
    dict_z_num[zodiac_name[n]] += 1

    # 输出字典里所有的统计结果
    for k in dict_cz_num.keys():
        print(f'生肖{k}有{dict_cz_num[k]}')

    for k in dict_z_num.keys():
        print(f'星座{k}有{dict_z_num[k]}')

    

