from model.group import Group


def test_delete_first_group(app):
    #app.session.login( username="admin", password="secret")
    #if app.group.count() == 0:
    #    app.group.create(Group(name="test"))
    app.group.check_group_existence()
    app.group.delete_first_group()
    #app.session.logout()