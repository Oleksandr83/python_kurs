import random

from model.contact import Contact
#from random import randrange


def test_del_some_contact(app, db, check_ui):
    #app.session.login(username="admin", password="secret")
    #if app.contact.count() == 0:
    #   app.contact.create(Contact(contact_firstname="TestName"))
    app.contact.check_contact_existence()
    old_contacts_list = db.get_contact_list()
    contact = random.choice(old_contacts_list)
    #index = randrange(len(old_contacts_list))
    app.contact.del_contact_by_id(contact.id) #app.contact.del_first_contact()
    new_contacts_list = db.get_contact_list()
    assert len(old_contacts_list) - 1 == app.contact.count() #len(new_contacts_list)
    #old_contacts_list[index:index+1] = []
    old_contacts_list.remove(contact)
    assert old_contacts_list == new_contacts_list
    #app.contact.return_to_home_page()
    #app.session.logout()
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)