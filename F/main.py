import datetime
import time
from functools import wraps
print(int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")) * 1000))