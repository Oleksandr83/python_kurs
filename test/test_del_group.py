from model.group import Group
#from random import randrange
import random


def test_delete_some_group(app, db):
    #app.session.login( username="admin", password="secret")
    #if app.group.count() == 0:
    #    app.group.create(Group(name="test"))
    app.group.check_group_existence()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    app.group.delete_group_by_id(group.id) #app.group.delete_group_by_index(index)  #app.group.delete_first_group()
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group) #old_groups[index:index+1] = [] #old_groups[0:1] = []
    assert old_groups == new_groups
    #app.session.logout()