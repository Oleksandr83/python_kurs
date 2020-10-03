from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture



def test_add_contact_in_group(app, db, orm):
    contacts_list = db.get_contact_list()
    contact = random.choice(contacts_list)
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    old_contact_list_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_in_group_by_id(contact.id, group.id)
    print("Contact with id " + str(contact.id) +" added to the group with id " + str(group.id))
    new_contact_list_in_group = orm.get_contacts_in_group(group)
    print(old_contact_list_in_group)
    #проверка на наличие не состоит ли контакт уже в группе
    if contact in old_contact_list_in_group:
        pass
    else:
        old_contact_list_in_group.append(contact)
    assert sorted(old_contact_list_in_group, key=Contact.id_or_max) == sorted(new_contact_list_in_group, key=Contact.id_or_max)
    #assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    #if check_ui:
    #    assert sorted(new_contacts_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)




# фикстура указывающая на источник данных
'''def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    #group = Group(name="new group", header="some info", footer="other")
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count() #len(new_groups)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)'''