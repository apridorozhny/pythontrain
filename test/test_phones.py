import re
from fixture.db import Dbfixture
from model.contact import Contact

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_all_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_homepage.all_mail_from_home_page == merge_mail_like_on_home_page(contact_from_edit_page)

def test_db_all_on_homepage(app, db):
    contact_from_db = db.get_contact_list()
    #contact = app.contact.get_contact_list()
    contact_from_homepage = sorted(app.contact.get_contact_list(), key = Contact.id_or_max)
    i = 0
    j = 0
    while i in range(len(contact_from_db)) and j in range(len(contact_from_homepage)):
        assert contact_from_db[i].id == contact_from_homepage[j].id
        assert contact_from_db[i].firstname == contact_from_homepage[j].firstname
        assert contact_from_db[i].lastname == contact_from_homepage[j].lastname
        assert contact_from_db[i].address == contact_from_homepage[j].address
        assert contact_from_homepage[j].all_phones_from_home_page == "\n".join(filter(lambda x: x is not None,[contact_from_db[i].homephone, contact_from_db[i].mobilephone, contact_from_db[i].workphone,contact_from_db[i].phone ]))
        assert contact_from_homepage[j].all_mail_from_home_page == "\n".join(filter(lambda x: x is not None,[contact_from_db[i].mail1, contact_from_db[i].mail2, contact_from_db[i].mail3]))
        i+=1
        j+=1

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.phone == contact_from_edit_page.phone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.homephone, contact.mobilephone, contact.workphone, contact.phone]))))

def merge_mail_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.mail1, contact.mail2, contact.mail3]))))