__author__ = "OBL"

from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_main_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.get("http://localhost:8080/addressbook/")

    def create(self, contact):
        wd = self.app.wd
    # init group creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
    # submit group creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.mail1)
        self.change_field_value("email2", contact.mail2)
        self.change_field_value("email3", contact.mail3)
        self.change_field_value("phone2", contact.phone)
        self.change_field_value("address", contact.address)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
           wd.find_element_by_name(field_name).click()
           wd.find_element_by_name(field_name).clear()
           wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_main_page()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None


   # def mod_first_contact(self, contact):
    #    wd = self.app.wd
        # submit new contact creation
      #  wd.find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        # init and fill contact
      #  wd.find_element_by_name("firstname").click()
       # wd.find_element_by_name("firstname").clear()
       # wd.find_element_by_name("firstname").send_keys(contact.name)
       # wd.find_element_by_name("middlename").click()
       # wd.find_element_by_name("middlename").clear()
       # wd.find_element_by_name("middlename").send_keys(contact.middle)
       # wd.find_element_by_name("home").click()
       # wd.find_element_by_name("home").clear()
       # wd.find_element_by_name("home").send_keys(contact.home)
       # wd.find_element_by_name("mobile").click()
       # wd.find_element_by_name("mobile").clear()
       # wd.find_element_by_name("mobile").send_keys(contact.mobile)
       # wd.find_element_by_name("phone2").click()
       # wd.find_element_by_name("phone2").clear()
       # wd.find_element_by_name("phone2").send_keys(contact.phone)
       # wd.find_element_by_name("update").click()

    def modify_first_contact(self,index):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.return_to_main_page()
        self.select_contact_by_index(index)
    # open modif form
        wd.find_elements_by_css_selector(".center>a>img[title=\"Edit\"]")[index].click()
    # fill group form
        self.fill_contact_form(new_contact_data)
    # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def select_contact_by_index(self, index):
    # select first group
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
    # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def open_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.return_to_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_main_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = wd.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = row.find_element_by_tag_name("input").get_attribute("value")
                all_mail = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                all_mail_from_home_page=all_mail, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        mail1 = wd.find_element_by_name("email").get_attribute("value")
        mail2 = wd.find_element_by_name("email2").get_attribute("value")
        mail3 = wd.find_element_by_name("email3").get_attribute("value")
        phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id, homephone=homephone,
                       workphone=workphone, mobilephone=mobilephone, mail1=mail1, mail2=mail2, mail3=mail3, phone=phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, phone=phone)