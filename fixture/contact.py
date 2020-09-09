from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact.contact_firstname)
        self.change_contact_field_value("lastname", contact.contact_lastname)
        self.change_contact_field_value("address", contact.contact_address)

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()
        # select edition for the first contact
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        # edit contact info
        self.fill_contact_form(new_contact_data)
        # submit contact updating
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def del_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        # close popup
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        #self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") or wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home page").click()
        #wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_contact_existence(self):
        wd = self.app.wd
        if self.count() == 0:
            self.create(Contact(contact_firstname="TestName"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_to_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[contains(@name, 'entry')]"):
            cells = element.find_elements_by_tag_name("td")
            text2 = cells[1].text
            text1 = cells[2].text
            text3 = cells[3].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(contact_firstname=text1, contact_lastname=text2, contact_address=text3,  id=id))
        return contacts




    '''def get_group_list(self):
        wd = self.app.wd
        self.open_group_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text =element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups'''
