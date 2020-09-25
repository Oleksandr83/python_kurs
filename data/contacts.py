
from model.contact import Contact
import random
import string

'''@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture'''

# использование фиксированных данных
testdata = [
    Contact(contact_firstname="contact_firstname1", contact_lastname="contact_lastname1", contact_address="contact_address1",contact_homephone="contact_homephone1", contact_email="contact_email1"),
    Contact(contact_firstname="contact_firstname2", contact_lastname="contact_lastname2", contact_address="contact_address2",contact_homephone="contact_homephone2", contact_email="contact_email2")
]

# случайным образом генерируемые данные
#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + " "*5
#    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

#def random_numbers(prefix, maxlen):
#    #numbers = string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(string.digits) for i in range (random.randrange(maxlen))])

#def random_email(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + "@"*10 + "."
#    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

#testdata =[Contact(contact_firstname="", contact_lastname="", contact_address="",contact_homephone="", contact_email="")] + [
#        Contact(contact_firstname=random_string("firstname", 15), contact_lastname=random_string("lastname", 20), contact_address=random_string("address", 10), contact_homephone=random_numbers("tel", 12), contact_email=random_email("email", 30))
#        for i in range(2)
#]