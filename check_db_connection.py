#import mysql.connector
import pymysql
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
    #cursor = connection.cursor()
    #cursor.execute("select * from group_list") # тут должен быть запрос в скобочках на языке sql
    #for row in cursor.fetchall():#fetchall возвращает всю информацию в виде строк
    #    print(row)

finally:
    db.destroy()
    #connection.close()