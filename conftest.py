import pytest
import json
import os.path
from fixture.application import Application
import importlib


fixture = None
target = None

@pytest.fixture #(scope="session")

def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))  # __file__ специальная встроенная переменная Python, которая содержит информацию, о пути к текущему файлу, правда может быть не совсем правильный. Иногда как обсолютный путь, а иногда как относительный путь
        with open(config_file) as f: # переменная f будет содержать обьект, который указывает на открытый файл
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture

@pytest.fixture  (scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption (parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    #parser.addoption("--password", action="store", default="secret")

def pytest_generate_tests(metafunc): # особый обьект metafunc, через него можно получить практически полную информацию о тестовой функциию. а частности можем полуить инфо о фиксиурах как параметры тестовой функции
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"): # проюегая по всем параметрам, нас будет интересовать только те которые начинаются с префикса data
            testdata = load_form_module(fixture[5:1]) # когда находим, загружаем тестовые данные из модуля котор имеет такое же название как фиестура но обрезанный fixture[5:1] удаляет первые пять символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata