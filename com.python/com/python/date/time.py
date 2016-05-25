# coding=utf-8
import time;  # This is required to include time module.
import calendar
import datetime


ticks = time.time()
print ("当前时间：", ticks)
localtime = time.localtime(time.time())
print ("当前时间 :", localtime)
#格式化
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
t_str = '2012-03-05 16:26:23'
d = datetime.datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S')
print(d)
#获取日历
cal = calendar.month(2008, 1)
print ("日历:")
print (cal)