from sys import maxsize


class Contact:

    def __init__(self, contact_firstname=None, contact_lastname=None, contact_homephone=None, contact_mobilephone=None, contact_workphone=None, contact_secondaryphone=None, contact_address=None, id=None):
        self.contact_firstname = contact_firstname
        self.contact_lastname = contact_lastname
        self.contact_homephone = contact_homephone
        self.contact_mobilephone = contact_mobilephone
        self.contact_workphone = contact_workphone
        self.contact_secondaryphone = contact_secondaryphone
        self.contact_address = contact_address
        self.id = id

    # representation в консоли - стандартная функция - определяет как будет выглядеть обтект при выводе на консоль (строкое представление)
    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.contact_firstname, self.contact_lastname, self.contact_address)

    # стандартная функция equels - принимающая в качестве второго параметра обьект с которым мы должны сравнить текущий обьект self
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.contact_firstname == other.contact_firstname and self.contact_lastname == other.contact_lastname and self.contact_address == other.contact_address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize    #специальная константа - максимальное чисто которое может использоваться в качестве индекса в списках и считается что для практическиъ целей мпжно использовать как максимальное целое число (import from sys)