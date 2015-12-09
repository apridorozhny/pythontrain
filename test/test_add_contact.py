# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(name="oleg", middle="lol", home="321654", mobile="321654", phone="qwe123"))

def test_add_emptycontact(app):
    app.contact.create(Contact(name="", middle="", home="", mobile="", phone=""))
