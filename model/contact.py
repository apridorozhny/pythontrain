__author__ = "OBL"
from sys import maxsize

class Contact:

    def __init__(self, name=None, middle=None, home=None, mobile=None, phone=None, id=None):
        self.name = name
        self.middle = middle
        self.home = home
        self.mobile = mobile
        self.phone = phone
        self.id = id

    def __repr__(self):
        return "%s" % (self.id)

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

