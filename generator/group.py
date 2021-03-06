from model.group import Group
import random
import string
import os.path
import jsonpickle
#import json
import getopt # для чтения опций командной строки
import sys # для того что бы получить доступ к опциям командной строки


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata =[Group(name="", header="", footer="")] + [
        Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
        for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)# параметры форматирования для нагладности в json файле
    out.write(jsonpickle.encode(testdata))
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2)) # функция dumps превращает некроторые данные в строку в формате json. Определяем функцию default когда json не знает как преобразовывать данные. преобразовываем в словарь c помощью lambda
# __dict__ стандартное свойство которое хранит все свойства которые мы присваиваем в __init__ переменныые self.name, header, footer, id
# indent=2 преобразовыват вид json файла в более читаемый вид   -n10 -f data/test.json