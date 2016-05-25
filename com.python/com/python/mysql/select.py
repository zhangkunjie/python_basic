# encoding: utf-8
#!/usr/bin/python
#导入pymysql的包
import pymysql 
#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库 
conn=pymysql.connect(host='localhost',user='root',passwd='mysql',db='test',port=3306,charset='utf8') 
cur=conn.cursor()#获取一个游标 
"""
查询
"""
selectSQL="select * from student"
cur.execute(selectSQL) 
data=cur.fetchall() 
for d in data : 
   #注意int类型需要使用str函数转义 
 print("ID:"+str(d[0])+str(' 名字：'+d[1] +"性别： "+str(d[2])+"  年龄： "+str(d[3])))
cur.close()#关闭游标 
conn.close()#释放数据库资源 
