import pymysql

#连接database
def connect():
    conn = pymysql.connect(
        host='10.1.250.22',
        user='root',
        password='123456',
        database='',
        charset='utf8'
    )

def insert_table():
    pass