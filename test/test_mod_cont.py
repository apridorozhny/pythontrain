__author__ = "OBL"

from model.contact import Contact

def test_mod_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.mod_first_contact(Contact(name="1", middle="1", home="1", mobile="1", phone="1"))
    app.session.logout()