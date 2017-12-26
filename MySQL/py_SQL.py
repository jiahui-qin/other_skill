# 使用pymysql连接到本地数据库
import pymysql
db = pymysql.connect(host = "localhost", user = "root", password = "1234", db = "world") #连接参数也可以用字典来表示
cursor = db.cursor()
cursor.execute("select Name from city where District like 'shanxi';")
data = cursor.fetchall()
print (data)
db.close()