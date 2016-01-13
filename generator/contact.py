from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts,args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptErroras as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
        for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))