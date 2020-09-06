from model.group import Group


def test_delete_first_group(app):
    #app.session.login( username="admin", password="secret")
    #if app.group.count() == 0:
    #    app.group.create(Group(name="test"))
    app.group.check_group_existence()
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    #app.session.logout()