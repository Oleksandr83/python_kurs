from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

def test_del_contact_from_grup(app, db, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.check_contact_existence()
    if len(orm.get_group_list()) == 0:
        app.group.check_group_existence()
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    old_contacts_list_in_group = orm.get_contacts_in_group(group)
    if old_contacts_list_in_group == []: # проверка на сдучайесли группа пустая, добавить контакт
        contacts_list = db.get_contact_list()
        contact = random.choice(contacts_list)
        app.contact.add_contact_in_group_by_id(contact.id, group.id)
    else:
        contact = random.choice(old_contacts_list_in_group)
    app.contact.del_contact_from_group_by_id(contact.id, group.id)
    new_contact_list_in_group = orm.get_contacts_in_group(group)
    old_contacts_list_in_group.remove(contact)
    assert sorted(old_contacts_list_in_group, key=Contact.id_or_max) == sorted(new_contact_list_in_group, key=Contact.id_or_max)