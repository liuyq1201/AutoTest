# import sys
# sums = 0
# def test1():
#     print("test")
#
#
# class A():
#     pass
#
#
# if __name__ == '__main__':
#     this_module = sys.modules[__name__]
#     print("s" + __name__)
#     print(this_module)
#
#     print(hasattr(this_module, "sums"))  # 变量
#     print(hasattr(this_module, "test1"))  # 方法
#     print(hasattr(this_module, "A"))  # 类
import requests


# class Web:
#     def login(self):
#         print('欢迎来到登录页面')
#
#     def register(self):
#         print('欢迎来到注册页面')
#
#     def save(self):
#         print('欢迎来到存储页面')
#
#
# while True:
#     obj = Web()
#     choose = input(">>>").strip()
#     # 判断对象是否有对应的方法
#     if hasattr(obj, choose):
#         # 获取对应的方法
#         f = getattr(obj, choose)
#         # 执行方法
#         f()

class BaseRequest:

    def get(self, url):
        print("==get==")
        return 1

    def post(self, url):
        print("==post==")
        return 2

    def put(self, url):
        resp = self.req.put(url)
        print("==put==")
        return 3

    def main_attr(self, method, url):
        if hasattr(self, method):
            func = getattr(self, method)
            return func(url)


if __name__ == '__main__':
    a = BaseRequest()
    b = a.main_attr('post', '111')
    print(b)
