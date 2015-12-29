__author__ = "OBL"
from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, homephone=None, mobilephone=None, workphone=None, phone=None,
                 mail1=None, mail2=None, mail3=None, id=None, all_phones_from_home_page=None, all_mail_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.phone = phone
        self.mail1 = mail1
        self.mail2 = mail2
        self.mail3 = mail3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mail_from_home_page = all_mail_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.id, self.firstname, self.lastname, self.address, self.homephone,
self.mobilephone, self.workphone, self.phone, self.mail1, self.mail2, self.mail3)

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

