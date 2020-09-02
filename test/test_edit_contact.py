from model.contact import Contact

def test_edit_firstname_contact(app):
    #app.session.login(username="admin", password="secret")
    app.contact.check_contact_existence()
    app.contact.edit_first_contact(Contact(contact_firstname="New firstname"))
    #app.session.logout()

def test_edit_lastname_contact(app):
    #app.session.login(username="admin", password="secret")
    app.contact.check_contact_existence()
    app.contact.edit_first_contact(Contact(contact_lastname="New lastname"))
    #app.session.logout()

def test_edit_adress_contact(app):
    #app.session.login(username="admin", password="secret")
    app.contact.check_contact_existence()
    app.contact.edit_first_contact(Contact(contact_address="New address"))
    #app.session.logout()