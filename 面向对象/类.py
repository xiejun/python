# 定义类的方式是：
class 类名:
    pass

# 在类中定义方法：
class 类名2:
    def 方法(self, 参数1):
        self.数据1 = 参数1
        pass

# 可以在 __init__ 方法中定义对象属性，之后在实例化类的时候传入数据。
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
pair = Pair(10, 20)


class Pair2:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def swap(self):
        # 实现了 self.first 和 self.second 两个值的交换。
        self.first, self.second = self.second, self.first
