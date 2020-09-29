# -*- coding: utf-8 -*-

from model.group import Group

# фикстура указывающая на источник данных
def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    #group = Group(name="new group", header="some info", footer="other")
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count() #len(new_groups)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()
