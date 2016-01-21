__author__ = "OBL"

from model.contact import Contact
import random

def test_mod_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact1 = Contact(firstname="1", lastname="1", homephone="1", mobilephone="1", phone="1")
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact1,contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)