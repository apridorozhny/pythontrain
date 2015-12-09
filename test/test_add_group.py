# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.group.create(Group(name="666", header="666", footer="666"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))