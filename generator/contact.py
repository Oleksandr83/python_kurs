from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys
#import json


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# случайным образом генерируемые данные
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_numbers(prefix, maxlen):
    #numbers = string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(string.digits) for i in range (random.randrange(maxlen))])

def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "@"*10 + "."
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata =[Contact(contact_firstname="", contact_lastname="", contact_address="",contact_homephone="", contact_email="")] + [
        Contact(contact_firstname=random_string("firstname", 15), contact_lastname=random_string("lastname", 20), contact_address=random_string("address", 10), contact_homephone=random_numbers("tel", 12), contact_email=random_email("email", 30))
        for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)  # параметры форматирования для нагладности в json файле
    out.write(jsonpickle.encode(testdata))
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))