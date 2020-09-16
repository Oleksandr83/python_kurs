import re
from random import randrange

def test_verification_contact_data(app):
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    print("\nThe random number from list of the contacts was: " + str(index))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.contact_firstname == contact_from_edit_page.contact_firstname
    assert contact_from_home_page.contact_lastname == contact_from_edit_page.contact_lastname
    assert contact_from_home_page.contact_address == contact_from_edit_page.contact_address
    assert contact_from_home_page.contact_all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                           map(lambda x: clear(x), [contact.contact_homephone, contact.contact_mobilephone, contact.contact_workphone,  contact.contact_secondaryphone])))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), [contact.contact_email, contact.contact_email2, contact.contact_email3])))
