x = 'abc'
if x == 'abc':
    print('x值和abc相等')
elif x=='':
        pass
else:
    pass

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# 输入是字符串，加入int强制转换成数字
year=int(input('请用户输入年份：'))
if(chinese_zodiac[year%12] == '狗'):
    print('狗年运势。。。')

# 在 if 语句中可以这样使用 not 关键字 ：
if not 1:
	pass