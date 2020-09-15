import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    #assert contact_from_home_page.contact_homephone == clear(contact_from_edit_page.contact_homephone)
    #assert contact_from_home_page.contact_workphone == clear(contact_from_edit_page.contact_workphone)
    #assert contact_from_home_page.contact_mobilephone == clear(contact_from_edit_page.contact_mobilephone)
    #assert contact_from_home_page.contact_secondaryphone == clear(contact_from_edit_page.contact_secondaryphone)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.contact_homephone == contact_from_edit_page.contact_homephone
    assert contact_from_view_page.contact_workphone == contact_from_edit_page.contact_workphone
    assert contact_from_view_page.contact_mobilephone == contact_from_edit_page.contact_mobilephone
    assert contact_from_view_page.contact_secondaryphone == contact_from_edit_page.contact_secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), [contact.contact_homephone, contact.contact_mobilephone, contact.contact_workphone,  contact.contact_secondaryphone])))