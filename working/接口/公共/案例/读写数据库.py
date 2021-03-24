#1、先导入MySQLdb库
import MySQLdb

#2、连接mysql
conn = MySQLdb.connect(                               #创建连接,将建立的连接赋给conn变量
    host = '127.0.0.1',                             #数据库的主机地址（因数据库装在本地，所以可以填127.0.0.1或localhost）
    user = 'root',                                   #连接数据库的用户名
    password = '123456',                            #连接数据库的密码
    db = 'sunck',                                   #连接的数据库库名
    port = 3306,                                     #连接数据库的端口
    charset = 'utf8'                                #编码格式
)


#3、建立游标（python通过游标执行sql语句）
c = conn.cursor()




#使用游标执行查询语句select * from students，执行语句的结果将保留在游标中
c.execute('select * from students')

#fetchone：获取结果中的一条数据,按从上到下的顺序获取，不会重复，超过最后一条就会返回空
result1 = c.fetchone()
result2 = c.fetchone()

#获取全部的结果
result3 = c.fetchall()
print(result3)


#执行插入、修改、删除语句，执行完后需进行commit
c.execute("insert into students(sname,sgender,sage,scontend,isDelete,lastTime,createTime,sgrade_id) values('aa1',1,25,'bb1','0','2020-11-14 15:32:00','2020-11-14 15:32:00','1');")
conn.commit()

conn.close()

