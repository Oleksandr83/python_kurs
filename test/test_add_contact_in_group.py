from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture



def test_add_contact_in_group(app, db, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.check_contact_existence()
    if len(orm.get_group_list()) == 0:
        app.group.check_group_existence()
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    if len(orm.get_contacts_not_in_group(group)) == 0: #проверка наличия контактов не состоящих в группе
        app.contact.check_contact_existence() # создание контакта
    contacts_list = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts_list)
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
