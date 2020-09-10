from model.contact import Contact
from random import randrange

def test_del_some_contact(app):
    #app.session.login(username="admin", password="secret")
    #if app.contact.count() == 0:
    #   app.contact.create(Contact(contact_firstname="TestName"))
    app.contact.check_contact_existence()
    old_contacts_list = app.contact.get_contact_list()
    index = randrange(len(old_contacts_list))
    app.contact.del_contact_by_index(index) #app.contact.del_first_contact()
    new_contacts_list = app.contact.get_contact_list()
    print("old contact list: " + str(old_contacts_list))
    print("new contact list: " + str(new_contacts_list))
    assert len(old_contacts_list) - 1 == app.contact.count() #len(new_contacts_list)
    old_contacts_list[index:index+1] = []
    assert old_contacts_list == new_contacts_list
    #app.contact.return_to_home_page()
    #app.session.logout()