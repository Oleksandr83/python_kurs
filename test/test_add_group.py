# -*- coding: utf-8 -*-

from model.group import Group

# фикстура указывающая на источник данных
def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    #group = Group(name="new group", header="some info", footer="other")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == app.group.count() #len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()
