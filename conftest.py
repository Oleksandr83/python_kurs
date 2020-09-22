import pytest
import json
import os.path
from fixture.application import Application


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