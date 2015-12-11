__author__ = "OBL"

from model.contact import Contact

def test_mod_first_contact(app):
    if app.contact.count() == 0:
         app.contact.create(Contact(name="test"))
    app.contact.modify_first_contact(Contact(name="1", middle="1", home="1", mobile="1", phone="1"))