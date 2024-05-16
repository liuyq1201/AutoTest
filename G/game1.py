import time

timeStamp = "1677567380336"
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(timeStamp)/1000))
print(otherStyleTime)
