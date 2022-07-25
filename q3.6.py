"""
Create a textfile having 10 email address in it. Each address is stored in a
separate line. Find out the most common domain name present in the file and
display it.

"""

def readfile(filename):
    fs = open(filename, "r")
    contents = fs.read()
    fs.close()
    return contents

def create(filename, content_to_write):
    fs = open(filename, "w")
    fs.write(content_to_write)
    fs.close()

def mode(list1):
    return sorted(list1, key=list1.count)[-1]

emails = []
for _ in range(10):
    emails.append(input("Enter email: "))

create("files/emails.txt", "\n".join(emails))

received_emails = readfile(emails)
domains = []
for i in received_emails.split("\n"):
    domains.append(i.split("@")[-1])

print(mode(domains))