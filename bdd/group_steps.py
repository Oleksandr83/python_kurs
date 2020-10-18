

from pytest_bdd import given, when, then
from model.group import Group

@given('a group list',target_fixture="group_list") #добавлено помимо лекции target_fixture="group_list", из переписки
def group_list(db):
    return db.get_group_list()

@given('a group with <name>, <header> and <footer>', target_fixture="new_group") #добавлено помимо лекции target_fixture="new_group"", из переписки
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group list is equal to the old group list with the added group')
def verify_group_edit(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


    '''интересно... судя по всему, в новых версиях pytest-bdd больше не создаётся автоматически фикстура с тем же именем, что и у функции, вместо неё создаётся фикстура со сложным именем "pytestbdd_given_a group with <name>, <header> and <footer>"
но, судя по документации, можно это исправить, добавив в описание шага параметр target_fixture
@given('a group with <name>, <header> and <footer>', target_fixture="new_group")
def create_new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)
при этом имя функции может быть любым, а фикстура будет создана с тем именем, которое указано в target_fixture'''

    '''у вас в логе перечисляется список доступных фикстур, вот он
>       available fixtures: app, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, check_ui, db, doctest_namespace, monkeypatch, pytestbdd_given_a group list, pytestbdd_given_a group with <name>, <header> and <footer>, pytestbdd_given_trace, pytestbdd_then_the new group list is equal to the old list with the added group, pytestbdd_then_trace, pytestbdd_when_I add the group to the list, pytestbdd_when_trace, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, stop, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
видно, что там создались фикстуры с этими странными именами'''