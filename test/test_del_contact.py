from model.contact import Contact

def test_del_first_contact(app):
    #app.session.login(username="admin", password="secret")
    #if app.contact.count() == 0:
    #   app.contact.create(Contact(contact_firstname="TestName"))
    app.contact.check_contact_existence()
    app.contact.del_first_contact()
    #app.contact.return_to_home_page()
    #app.session.logout()