from model.contact import Contact

def test_edit_firstname_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(contact_firstname="New firstname"))
    #app.contact.return_to_home_page()
    app.session.logout()

def test_edit_lastname_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(contact_lastname="New lastname"))
    #app.contact.return_to_home_page()
    app.session.logout()

def test_edit_adress_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(contact_address="New address"))
    #app.contact.return_to_home_page()
    app.session.logout()