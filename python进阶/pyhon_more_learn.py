# 闭包
def num(num):
    def num_in(n_in):
        print("num + n_in:", num + n_in)
        return num + n_in
    print("num:", num)
    return num_in


a = num(100)  # 将参数为100的函数num接收，并赋值给a，只不过这个返回值是一个函数的引用。等于 a = num_in，注意这里接收的不光是函数本身，还有已经传递的参数
print(a)
b = a(101)
print(b)
