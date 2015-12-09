__author__ = "OBL"

from model.group import Group

def test_mod_first_group(app):
    app.group.modify_first_group(Group(name="2", header="2", footer="2"))
