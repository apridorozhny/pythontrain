# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname="oleg", lastname="lol", address="Lenin Street", homephone="321654", mobilephone="777777",
                       workphone="123456", phone="qwe123", mail1="oleg@yahoo", mail2="oleg@gmail", mail3="oleg@tut"))
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_emptycontact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(name="", middle="", home="", mobile="", phone="")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)