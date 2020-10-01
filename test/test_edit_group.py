from model.group import Group
from random import randrange
import random


'''def test_edit_group_name(app):
    #app.session.login( username="admin", password="secret")
    app.group.check_group_existence()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group) #app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()'''

def test_edit_group_name(app, db, check_ui):
    #app.session.login( username="admin", password="secret")
    app.group.check_group_existence()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    new_data = Group(name="New group")
    #group.id = old_groups[index].id
    app.group.edit_group_by_id(group.id, new_data) #app.group.edit_first_group(group)
    new_groups = db.get_group_list()
    #assert len(old_groups) == len(new_groups)
    index = old_groups.index(group)
    data_with_id = Group(id=group.id, name="New group")
    old_groups[index] = data_with_id
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

'''def test_edit_group_header(app):
    #app.session.login(username="admin", password="secret")
    app.group.check_group_existence()
    old_groups = app.group.get_group_list()
    group = Group(header="New header")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()

def test_edit_group_footer(app):
    #app.session.login(username="admin", password="secret")
    app.group.check_group_existence()
    old_groups = app.group.get_group_list()
    group = Group(footer="New footer")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()'''