# 元组
("abc","def")
# # 存储内容不可变更
zodiac_name = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',
                u'处女座',u'天秤座',u'天蝎座',u'射手座') # u表示采用unicode方式存储字符串，在python3中已统一使用unicode，因此中文字符串前是否增加无影响
# # 元组嵌套
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# # # 元组中两个数字的大小比较
print((1,20)>(2,19))
# # # 取出元组中满足条件的元素
(month,day) = (3,15)
zodiac_day = filter(lambda x: x<=(month,day),zodiac_days)
# # # 转换成序列
a=(1,3,5,7)
b=4
print(list(filter(lambda x: x<b,a)))

zodiac_len = len(list(zodiac_day))%12
# # # # 这里使用的filter()函数的返回类型叫迭代器，它是我们后面要讲的一种函数功能。
# # # # filter函数返回的内容类似一根长长的管子，里面按顺序依次存好要输出的元素，使用list()函数可以一次性将管子里的数据都取出来，第二次再去取管子中自然是空的了。
print(list(zodiac_day))
print(list(filter(lambda x: x<=(month,day),zodiac_days)))

print(zodiac_name[zodiac_len])

