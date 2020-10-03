#import mysql.connector
import pymysql
#from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id="261"))
    for item in l:
        print(item)
    print(len(l))
    #cursor = connection.cursor()
    #cursor.execute("select * from group_list") # тут должен быть запрос в скобочках на языке sql
    #for row in cursor.fetchall():#fetchall возвращает всю информацию в виде строк
    #    print(row)

finally:
    pass
    #db.destroy()
    #connection.close()