chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
for cz in chinese_zodiac:
    print(cz)

for i in range(13):
    print(i)

for i in range(1,13):
    print(i)

for year in range(2018,2019):
    print('%s年的生肖是%s'%(year,chinese_zodiac[year%12]))

for year in range(2018,2019):
    print(f'{year}年的生肖是{chinese_zodiac[year%12]}')

import time
num = 5
while True:
    print('a')
    num = num +1
    if num > 10:
        break

# num = 5
# while True:
    
#     num = num +1
#     if num ==10:
#         continue
#     print(num)
#     time.sleep(1)

#循环语句中加入条件判断
zodiac_name = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',
                u'处女座',u'天秤座',u'天蝎座',u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

int_month = int(input('输入月份:'))
int_day = int(input('输入日期:'))

# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >= (int_month,int_day):
#         print(zodiac_name[zd_num])
#         break
#     elif int_month == 12 and int_day > 23:
#         print(zodiac_name[0])
#         break

num = 0
while zodiac_days[num] < (int_month,int_day):
    if int_month == 12 and int_day > 23:
        break
    num +=1
print(zodiac_name[num])
