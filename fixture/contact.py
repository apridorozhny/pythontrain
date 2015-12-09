__author__ = "OBL"

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
    # init group creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
    # submit group creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.middle)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("phone2", contact.phone)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
           wd.find_element_by_name(field_name).click()
           wd.find_element_by_name(field_name).clear()
           wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.get("http://localhost:8080/addressbook/")
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

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

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.get("http://localhost:8080/addressbook/")
        self.select_first_contact()
    # open modif form
        wd.find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
    # fill group form
        self.fill_contact_form(new_contact_data)
    # submit modification
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
    # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))