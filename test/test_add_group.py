# -*- coding: utf-8 -*-

# import pytest
from model.group import Group
import pytest
#from data.add_group import testdata
from data.add_group import constant as testdata
#import random
#import string
#from fixture.application import Application
from sys import maxsize

'''''@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture'''

#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


#testdata =[Group(name="", header="", footer="")] + [
#        Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
#        for i in range(5)
#]

#testdata = [
#        Group(name=name, header=header, footer=footer)
#        for name in ["", random_string("name", 10)]
#        for header in ["", random_string("header", 10)]
#        for footer in ["", random_string("footer", 10)]
#
#]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    #group = Group(name="new group", header="some info", footer="other")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == app.group.count() #len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()

'''def test_add_empty_group(app):
    #app.session.login(username="admin", password="secret")
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()'''

