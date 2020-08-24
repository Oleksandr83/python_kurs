# -*- coding: utf-8 -*-
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
#import unittest
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login( username="admin", password="secret")
    app.create_group(Group(name="new group", header="some info", footer="other"))
    app.logout()

def test_add__empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

    '''def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page(wd)

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self,  username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
    '''

    '''def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
       except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True'''

    '''def tearDown(self):
        self.app.destroy()
        self.wd.quit()'''


'''if __name__ == "__main__":
    unittest.main()'''