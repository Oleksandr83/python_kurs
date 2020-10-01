from model.contact import Contact
from random import randrange
import random

def test_edit_firstname_contact(app, db):
    #app.session.login(username="admin", password="secret")
    app.contact.check_contact_existence()
    old_contacts_list = db.get_contact_list()
    contact = random.choice(old_contacts_list)
    index = old_contacts_list.index(contact)
    #index = randrange(len(old_contacts_list))
    new_edit_contact_data = Contact(contact_firstname="New firstname")
    #contact.id = old_contacts_list[index].id #запоминание идентификатора
    new_edit_contact_data.contact_lastname = old_contacts_list[index].contact_lastname
    new_edit_contact_data.contact_address = old_contacts_list[index].contact_address
    app.contact.edit_contact_by_index(index, new_edit_contact_data)
    #app.contact.edit_contact_by_id(contact.id, new_data) #app.contact.edit_first_contact(contact)
    new_contacts_list = db.get_contact_list()
    assert len(old_contacts_list) == app.contact.count() #len(new_contacts_list)
    #index = old_contacts_list.index(contact)
    #data_with_id = Contact(id=contact.id, contact_firstname="New firstname" )
    old_contacts_list[index] = new_edit_contact_data
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    #app.session.logout()


'''def test_edit_firstname_contact(app):
    #app.session.login(username="admin", password="secret")
    app.contact.check_contact_existence()
    old_contacts_list = app.contact.get_contact_list()
    index = randrange(len(old_contacts_list))
    contact = Contact(contact_firstname="New firstname")
    contact.id = old_contacts_list[index].id #запоминание идентификатора
    contact.contact_lastname = old_contacts_list[0].contact_lastname
    contact.contact_address = old_contacts_list[0].contact_address
    app.contact.edit_contact_by_index(index, contact) #app.contact.edit_first_contact(contact)
    new_contacts_list = app.contact.get_contact_list()
    assert len(old_contacts_list) == app.contact.count() #len(new_contacts_list)
    old_contacts_list[index] = contact
    print("/n old contact list: " + str(old_contacts_list))
    print("new contact list: " + str(new_contacts_list))
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    #app.session.logout()'''