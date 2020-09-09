# -*- coding: utf-8 -*-

# import pytest
from model.group import Group
#from fixture.application import Application
from sys import maxsize

'''''@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture'''

def test_add_group(app):
    #app.session.login( username="admin", password="secret")
    old_groups = app.group.get_group_list()
    group = Group(name="new group", header="some info", footer="other")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()

def test_add_empty_group(app):
    #app.session.login(username="admin", password="secret")
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()

