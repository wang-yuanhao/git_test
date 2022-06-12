import time
import datetime
#时间戳
dt1 = 1462451334 #"2016-05-05 20:28:54"
dt2 = 1462451534 #"2016-05-05 20:28:59"
#转换时间格式
startTime = time.localtime(dt1)
endTime = time.localtime(dt2)
startTime = time.strftime("%Y-%m-%d %H:%M:%S",startTime)
endTime = time.strftime("%Y-%m-%d %H:%M:%S",endTime)
#计算秒数
startTime= datetime.datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S")
endTime= datetime.datetime.strptime(endTime,"%Y-%m-%d %H:%M:%S")
print(endTime.timestamp())
seconds = (endTime- startTime).seconds  # 相减得到秒数
print(seconds)
