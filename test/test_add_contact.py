# -*- coding: utf-8 -*-
import pytest
from fixture.application1 import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_new_contact()
    app.contact.create(Contact(name="oleg", middle="lol", home="321654", mobile="321654", phone="qwe123"))
    app.session.logout()

def test_add_emptycontact(app):
    app.session.login(username="admin", password="secret")
    app.open_new_contact()
    app.contact.create(Contact(name="", middle="", home="", mobile="", phone=""))
    app.session.logout()
