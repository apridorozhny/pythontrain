__author__ = "OBL"
from model.group import Group
import random

def test_mod_some_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group1 = Group(name="new group")
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group1, group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)