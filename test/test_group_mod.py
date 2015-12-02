__author__ = "OBL"

from model.group import Group

def test_mod_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(name="2", header="2", footer="2"))
    app.session.logout()