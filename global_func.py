x = 1
def global_func():
    global x
    print(x)
    x = x + 1

global_func()  # 1
global_func()  # 2
global_func()  # 3