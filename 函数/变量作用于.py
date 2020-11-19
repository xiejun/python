var1 = 123
def func():
    global var1
    var1 = 456
    print(var1)

func()
print(var1)
