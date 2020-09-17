from sys import maxsize


class Contact:

    def __init__(self, contact_firstname=None, contact_lastname=None, all_phones_from_home_page=None, id=None,
                 contact_homephone=None, contact_mobilephone=None, contact_workphone=None, contact_secondaryphone=None,
                 contact_address=None, contact_all_emails_from_home_page=None, contact_email=None, contact_email2=None, contact_email3=None ):
        self.contact_firstname = contact_firstname
        self.contact_lastname = contact_lastname
        self.all_phones_from_home_page=all_phones_from_home_page
        self.contact_homephone = contact_homephone
        self.contact_mobilephone = contact_mobilephone
        self.contact_workphone = contact_workphone
        self.contact_secondaryphone = contact_secondaryphone
        self.contact_address = contact_address
        self.id = id
        self.contact_all_emails_from_home_page = contact_all_emails_from_home_page
        self.contact_email = contact_email
        self.contact_email2 = contact_email2
        self.contact_email3 = contact_email3

    # representation в консоли - стандартная функция - определяет как будет выглядеть обтект при выводе на консоль (строкое представление)
    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.contact_firstname, self.contact_lastname, self.contact_address, self.all_phones_from_home_page, self.contact_all_emails_from_home_page)

    # стандартная функция equels - принимающая в качестве второго параметра обьект с которым мы должны сравнить текущий обьект self
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.contact_firstname == other.contact_firstname and \
               self.contact_lastname == other.contact_lastname and \
               self.contact_address == other.contact_address and \
               self.all_phones_from_home_page == other.all_phones_from_home_page and \
               self.contact_all_emails_from_home_page == other.contact_all_emails_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize    #специальная константа - максимальное чисто которое может использоваться в качестве индекса в списках и считается что для практическиъ целей мпжно использовать как максимальное целое число (import from sys)