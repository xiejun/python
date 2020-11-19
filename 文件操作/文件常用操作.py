file4=open('name.txt')
print(file4.readline())

file5 = open('name.txt')
for line in file5.readlines():
    print(line)

file6=open('name.txt')
# 文件指针
print(file6.tell())
print(file6.read(1))
print(file6.tell())
# 文件指针返回文件开始处
file6.seek(0)
# 第一个参数代表偏移位置，第二个参数 0 表示从文件开头偏移 1表示从当前位置偏移 2从文件结尾
file6.seek(5,0)
print(file6.tell())
file6.close()