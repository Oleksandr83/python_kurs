# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.contact import Contact
import pytest
import random
import string

'''@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture'''


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
        for i in range(3)
]

#testdata = [
#        Contact(contact_firstname=name, contact_lastname=lastname, contact_address=address, contact_homephone=homephone, contact_email=contact_email)
#        for name in ["", random_string("name", 10)] # один раз берется пустоя значение, а другой из 10 символов
#        for lastname in ["", random_string("lastname", 10)]
#        for address in ["", random_string("address:", 15)]
#        for homephone in [random_numbers("tel ", 10)]
#        for contact_email in [random_email("email: ", 25)]
#]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata]) #где "contact" название параметра который будет передаваться, а testdata источник откуда будут браться значение параметра
def test_add_contact(app, contact):
    pass
    old_contacts_list = app.contact.get_contact_list()
    #contact = Contact(contact_firstname="Alex", contact_lastname="Myniuk", contact_address="Sweden")
    app.contact.create(contact)
    new_contacts_list = app.contact.get_contact_list()
    assert len(old_contacts_list) + 1 == app.contact.count()
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)

'''def test_add_empty_contact(app):
    #app.session.login(username="admin", password="secret")
    old_contacts_list = app.contact.get_contact_list()
    contact = Contact(contact_firstname="", contact_lastname="", contact_address="")
    app.contact.create(contact)
    new_contacts_list = app.contact.get_contact_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list)
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    #app.contact.return_to_home_page()
    #app.session.logout()'''



