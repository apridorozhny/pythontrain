# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxleng):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxleng))])

testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="", workphone="", phone="",
                    mail1="", mail2="", mail3="")] + \
[
        Contact(firstname=random_string("firstname", 12), lastname=random_string("lastname", 12),
address=random_string("firstname", 12), homephone=random_string("homephone", 7), mobilephone=random_string("mobilephone", 12),
workphone=random_string("workphone", 12), phone=random_string("phone", 12), mail1=random_string("mail1", 12),
mail2=random_string("mail2", 12), mail3=random_string("mail3", 12),)
        for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
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