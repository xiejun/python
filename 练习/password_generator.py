import randomchar

def generate_password(length):
    if length < 4:
        raise ValueError('密码至少为 4 位')

    random_char = randomchar.RandomChar()

    password  = random_char.uppercase()
    password += random_char.lowercase()
    password += random_char.digit()
    password += random_char.special()

    count = 5
    
    while count <= length:
        password += random_char.anyone()
        count += 1

    return password


password_length = input('请输入密码长度（8～20）：')
password_length = int(password_length)

if password_length < 8 or password_length > 20:
    raise ValueError('密码长度不符')

password = generate_password(password_length)
print(password)

# 循环若干次这里用了 while 循环，可以使用 for _ in range(x) 的方式替代
# 把随机数字当作索引然后从字符串中取值，可以直接使用 random.choice() 函数替代
# RandomChar 中的对象属性和对象方法，可直接定义成类属性和类方法
# ‘ABCDEFGHIJKLMNOPQRSTUVWXYZ’ 这类字符集合不需要手工书写，使用 string 模块即可获取，如 string.ascii_uppercase