from model.contact import Contact

def test_edit_firstname_contact(app):
    #app.session.login(username="admin", password="secret")
    app.contact.check_contact_existence()
    old_contacts_list = app.contact.get_contact_list()
    contact = Contact(contact_firstname="New firstname")
    contact.id = old_contacts_list[0].id #запоминание идентификатора
    contact.contact_lastname = old_contacts_list[0].contact_lastname
    contact.contact_address = old_contacts_list[0].contact_address
    app.contact.edit_first_contact(contact)
    new_contacts_list = app.contact.get_contact_list()
    assert len(old_contacts_list) == len(new_contacts_list)
    old_contacts_list[0] = contact
    print("/n old contact list: " + str(old_contacts_list))
    print("new contact list: " + str(new_contacts_list))
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    #app.session.logout()

'''def test_edit_lastname_contact(app):
    #app.session.login(username="admin", password="secret")
    app.contact.check_contact_existence()
    app.contact.edit_first_contact(Contact(contact_lastname="New lastname"))
    #app.session.logout()

def test_edit_adress_contact(app):
    #app.session.login(username="admin", password="secret")
    app.contact.check_contact_existence()
    app.contact.edit_first_contact(Contact(contact_address="New address"))
    #app.session.logout()'''