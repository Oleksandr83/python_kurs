# -*- coding: utf-8 -*-
#import unittest
import pytest
from fixture.application import Application
from contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

'''class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()
        #self.wd = webdriver.Firefox()
        #self.wd.implicitly_wait(30)'''

    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(contact_firstname="Alex", contact_lastname="Myniuk", contact_adress="Sweden"))
    app.return_to_home_page()
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(contact_firstname="", contact_lastname="", contact_adress=""))
    app.return_to_home_page()
    app.logout()


    #def logout(self):
    #    wd = self.wd
    #    wd.find_element_by_link_text("Logout").click()

    

    '''def return_to_home_page(self:
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact):
        wd = self.wd
        self.open_contact_page()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.contact_firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.contact_lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.contact_adress)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()'''

    '''def login(self,username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")'''

    #def is_element_present(self, how, what):
     #   try: self.wd.find_element(by=how, value=what)
     #  except NoSuchElementException as e: return False
      #  return True
    
    #def is_alert_present(self):
     #   try: self.wd.switch_to_alert()
     #   except NoAlertPresentException as e: return False
     #   return True
    
    #def tearDown(self):
    #    self.app.destroy()

#if __name__ == "__main__":
#    unittest.main()
