"""
Create a textfile having 10 email address in it. Each address is stored in a
separate line. Find out the most common domain name present in the file and
display it.

@author: Krishaay Jois
"""

def find_domain():
    try:
        f = open('files/emails.txt', 'r')
        domains = {}
        for line in f.readlines():
            words = line.split()
            for word in words:
                domain = word.split('@')[1]
                if domain in domains:
                    domains[domain] += 1
                else:
                    domains[domain] = 1
        f.close()
        print("Most Common Domain: ",max(domains, key=domains.get))
    except:
        print("Error in finding domain")

find_domain()