import re
from fixture.orm import ORMFixture
from model.contact import Contact


'''def test_verification_all_contact_data(app, orm):
    all_contacts_data = []
    for i in app.contact.get_contact_list():
        contact_from_home_page = app.contact.get_contact_list()[index]
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    print("\nThe random number from list of the contacts was: " + str(index))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_db = orm.get_contact_list
    assert contact_from_home_page.contact_firstname == contact_from_db.contact_firstname
    assert contact_from_home_page.contact_lastname == contact_from_db.contact_lastname
    assert contact_from_home_page.contact_address == contact_from_db.contact_address
    assert contact_from_home_page.contact_all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)'''

def test_verification_all_contact_data(app, orm):
    contact_from_ui_home_page = app.contact.get_contact_list()
    contact_from_db = orm.get_contact_list()
    assert len(contact_from_ui_home_page) == len(contact_from_db)
    x = len(contact_from_db)
    for i in range (x):
        contact_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)[i]
        contact_from_db = sorted(orm.get_contact_list(), key=Contact.id_or_max)[i]
        #contact_from_ui = app.contact.get_contact_list()[i] sorted(old_contact_list_in_group, key=Contact.id_or_max)
        #contact_from_db = orm.get_contact_list()[i]
        assert contact_from_ui.contact_firstname == contact_from_db.contact_firstname
        assert contact_from_ui.contact_lastname == contact_from_db.contact_lastname
        assert contact_from_ui.contact_address == contact_from_db.contact_address
        assert contact_from_ui.contact_all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)
        assert contact_from_ui.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(orm):
    return "\n".join(filter(lambda x: x != "",
                           map(lambda x: clear(x), [orm.contact_homephone, orm.contact_mobilephone, orm.contact_workphone,  orm.contact_secondaryphone])))

def merge_emails_like_on_home_page(orm):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), [orm.contact_email, orm.contact_email2, orm.contact_email3])))
