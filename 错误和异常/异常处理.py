
try:
    a = int(input('input year'))
except ValueError :
        print("请输入数字")

try:
    pass
except (ValueError,AttributeError,KeyError):
    pass

try:
    # 主动抛出异常
    raise NameError('xxx')
except NameError:
    pass
finally:
    pass

try:
    file1 = open('name.txt')
except Exception as e:
    print(e)
finally:
    file1.close()

# Exception	大多数异常的基类
# SyntaxError	无效语法
# NameError	名字（变量、函数、类等）不存在
# ValueError	不合适的值
# IndexError	索引超过范围
# ImportError	模块不存在
# IOError	I/O 相关错误
# TypeError	不合适的类型
# AttributeError	属性不存在
# KeyError	字典的键值不存在
# ZeroDivisionError	除法中被除数为 0


