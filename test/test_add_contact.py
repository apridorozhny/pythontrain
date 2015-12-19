# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(name="oleg", middle="lol", home="321654", mobile="321654", phone="qwe123"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_emptycontact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(name="", middle="", home="", mobile="", phone=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
