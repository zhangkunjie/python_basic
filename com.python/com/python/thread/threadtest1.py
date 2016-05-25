"""
函数式：调用thread模块中的start_new_thread()函数来产生新线程。语法如下:
thread.start_new_thread ( function, args[, kwargs] )
参数说明:
    function - 线程函数。
    args - 传递给线程函数的参数,他必须是个tuple类型。
    kwargs - 可选参数。
"""
# 为线程定义一个函数
import  _thread
import  threading
import  time
f=open("D://thread.txt","w")
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print( "%s: %s" % ( threadName, time.ctime(time.time()) ))
# 创建两个线程
def test():
  _thread.start_new_thread(print_time,("Thread-1", 2))
  _thread.start_new_thread( print_time, ("Thread-2", 4) )
test()
time.sleep(2000)
