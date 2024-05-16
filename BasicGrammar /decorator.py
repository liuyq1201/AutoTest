def decorator(func):
    def wrapper(*args, **kwargs):
        # 在调用原始函数之前执行的代码
        print("装饰器：在函数调用之前执行一些操作")

        # 调用原始函数
        result = func(*args, **kwargs)

        # 在调用原始函数之后执行的代码
        print("装饰器：在函数调用之后执行一些操作")

        return result

    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}!")

# 调用被装饰的函数
greet("Alice")