import pytest
import json
import os.path
from fixture.application import Application
import importlib
import jsonpickle
from fixture.db import DbFixture
from fixture.orm import ORMFixture


fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture #(scope="session")
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

# фикстура для работы с базой данных
@pytest.fixture (scope="session")
def db(request): # request содержит инфо об опциях переданны при запеске фреймворка
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture (scope="session")
def orm(request): # request содержит инфо об опциях переданны при запеске фреймворка
    orm_config = load_config(request.config.getoption("--target"))['db']
    ormfixture = ORMFixture(host=orm_config['host'], name=orm_config['name'], user=orm_config['user'], password=orm_config['password'])
    #def fin():
    #    dbfixture.destroy()
    #request.addfinalizer(fin)
    return ormfixture

@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

# фикстура которая проверяет пользовательский интерфейс
@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")

def pytest_addoption (parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true") # опции для проверки пользовательского интерфейса
    #parser.addoption("--password", action="store", default="secret")

# загрузка и генерация тестовых данных
def pytest_generate_tests(metafunc): # особый обьект metafunc, через него можно получить практически полную информацию о тестовой функциию. а частности можем полуить инфо о фиксиурах как параметры тестовой функции
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"): # проюегая по всем параметрам, нас будет интересовать только те которые начинаются с префикса data
            testdata = load_form_module(fixture[5:]) # когда находим, загружаем тестовые данные из модуля котор имеет такое же название как фиестура но обрезанный fixture[5:1] удаляет первые пять символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_form_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_form_json(file):
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())