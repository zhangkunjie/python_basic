# encoding: utf-8
#!/usr/bin/python
#导入pymysql的包
import pymysql 
#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库 
conn=pymysql.connect(host='localhost',user='root',passwd='mysql',db='test',port=3306,charset='utf8') 
cur=conn.cursor()#获取一个游标 
"""
更新
"""
insertSQL=" update student set sex=0 where id=5"
cur.execute(insertSQL)
conn.commit()
cur.close()#关闭游标 
conn.close()#释放数据库资源 
