from functools import wraps
import time


def failure_retry(retry_count, retry_interval=5):
    """
    失败重试
    :param retry_count: 重试次数
    :param retry_interval: 重试间隔，默认5s
    """
    def wrapper(func):
        @wraps(func)
        def wrapper_(*args, **kwargs):
            for count in range(retry_count):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    import traceback

                    print(f"Case:{func.__name__} 开始执行第{count + 1}次重试...")
                    if count + 1 == retry_count:
                        print(f"异常堆栈信息为: {traceback.format_exc()}")
                    time.sleep(retry_interval)

        return wrapper_

    return wrapper


@failure_retry(retry_count=3)
def ceshi():
    print(1/0)


if __name__ == '__main__':
    ceshi()