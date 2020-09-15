import re

def test_firstname_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.contact_firstname == clear(contact_from_edit_page.contact_firstname)





def clear(s):
    return re.sub("[() -]", "", s)

#def merge_phones_like_on_home_page(contact):
#    return "\n".join(filter(lambda x: x != "",
#                           map(lambda x: clear(x), [contact.contact_homephone, contact.contact_mobilephone, contact.contact_workphone,  contact.contact_secondaryphone])))