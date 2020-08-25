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
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(contact_firstname="Alex", contact_lastname="Myniuk", contact_adress="Sweden"))
    app.contact.return_to_home_page()
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(contact_firstname="", contact_lastname="", contact_adress=""))
    app.contact.return_to_home_page()
    app.session.logout()



