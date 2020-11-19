alist=[]
for i in range(1,11):
    if(i%2==0):
        alist.append(i*i)

print(alist)

# 列表
blist = [i*i for i in range(1,11) if (i%2) == 0]

print(blist)

dict_z_num= {}
zodiac_name = ('摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座',
                '处女座','天秤座','天蝎座','射手座')
for i in zodiac_name:
    dict_z_num[i] = 0
# 字典
dict_z_num = {i:0 for i in zodiac_name}
print(dict_z_num)