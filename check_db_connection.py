#import mysql.connector
import pymysql

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list") # тут должен быть запрос в скобочках на языке sql
    for row in cursor.fetchall():#fetchall возвращает всю информацию в виде строк
        print(row)

finally:
    connection.close()