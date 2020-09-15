from model.contact import Contact
import re # пакет для работы с реглярными выражениями

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
        self.contact_cache = None

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
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()
        # select edition for the first contact
        wd.find_elements_by_xpath("//img[contains(@title,'Edit')]")[index].click() #wd.find_elements_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img")[index].click()
        # edit contact info
        self.fill_contact_form(new_contact_data)
        # submit contact updating
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click() #wd.find_elements_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        # close popup
        wd.switch_to_alert().accept()
        #wd.find_element_by_css_selector("div.msgbox")
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") or wd.current_url.endswith("/index.php")):
            #wd.find_element_by_link_text("home page").click()
            wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()
        #wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_contact_existence(self):
        wd = self.app.wd
        if self.count() == 0:
            self.create(Contact(contact_firstname="TestName"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_xpath("//tr[contains(@name, 'entry')]"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value") #id = row.find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                #email = cells[4].text
                #address = cells[3].text
                # all_phones = cells[5].text.splitlines()
                all_phones = cells[5].text
                #print(all_phones)
                all_emails = cells[4].text
                print(all_emails)
                self.contact_cache.append(Contact(contact_firstname=firstname, contact_lastname=lastname, id=id, all_phones_from_home_page = all_phones, contact_all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    # открывает форму редактирование index контакта
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    # открывает странице просмотра деталей определенного index контакта
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        adress = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(contact_firstname=firstname, contact_lastname=lastname, contact_address=adress, id=id,
                       contact_homephone=homephone, contact_mobilephone=mobilephone,
                       contact_workphone=workphone, contact_secondaryphone=secondaryphone,
                       contact_email=email, contact_email2=email2, contact_email3=email3)  # постройка обьекта из данных


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(contact_homephone=homephone, contact_mobilephone=mobilephone,
                       contact_workphone=workphone, contact_secondaryphone=secondaryphone)  # постройка обьекта из данных
