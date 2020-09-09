# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.contact import Contact

'''@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture'''


def test_add_contact(app):
    #app.session.login(username="admin", password="secret")
    old_contacts_list = app.contact.get_contact_list()
    contact = Contact(contact_firstname="Alex", contact_lastname="Myniuk", contact_address="Sweden")
    app.contact.create(contact)
    new_contacts_list = app.contact.get_contact_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list)
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    #app.contact.return_to_home_page()
    #app.session.logout()

def test_add_empty_contact(app):
    #app.session.login(username="admin", password="secret")
    old_contacts_list = app.contact.get_contact_list()
    contact = Contact(contact_firstname="", contact_lastname="", contact_address="")
    app.contact.create(contact)
    new_contacts_list = app.contact.get_contact_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list)
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    #app.contact.return_to_home_page()
    #app.session.logout()



