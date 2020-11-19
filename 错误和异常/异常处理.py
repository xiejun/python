
try:
    a = int(input('input year'))
except ValueError :
        print("请输入数字")

try:
    pass
except (ValueError,AttributeError,KeyError):
    pass

try:
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
