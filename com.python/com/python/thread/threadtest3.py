"""
通过继承的方式来启动多线程
"""
import threading
import  time

class MyThread(threading.Thread):
    def __init__(self,name,intervals):
        threading.Thread.__init__(self,name=name)
        self.intervals=intervals
    def run(self):
        for i in range(5):
            time.sleep(self.intervals)
            print("我是",self.name,"线程",i)
a=MyThread("A",1)
# a.setDaemon(True)
a.start()
b=MyThread("B",4)
# b.setDaemon(True)
b.start()
a.join()
#b.join()
print("主线程退出，end！")