from model.group import Group


def test_edit_group_name(app):
    #app.session.login( username="admin", password="secret")
    app.group.check_group_existence()
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    #app.session.logout()

def test_edit_group_header(app):
    #app.session.login(username="admin", password="secret")
    app.group.check_group_existence()
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    #app.session.logout()

def test_edit_group_footer(app):
    #app.session.login(username="admin", password="secret")
    app.group.check_group_existence()
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="New footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    #app.session.logout()