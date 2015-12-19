__author__ = "OBL"

from model.contact import Contact

def test_mod_first_contact(app):
    if app.contact.count() == 0:
         app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(name="1", middle="1", home="1", mobile="1", phone="1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)