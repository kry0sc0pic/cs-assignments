"""
A file ‘sports’ contains information in following format :
Event participant (in notepad with a single space separating both).
Write a method that would read the contents and creates a file named ‘athletics’,
copying only those records from sports where the event name is ‘athletics’.

@author: Krishaay Jois
"""

def filterAthletics():
    try:
        f = open('files/sports.txt','r')
        f_new = open('files/athletics.txt','w')
        lines = []
        for line in f.readlines():
            if "athletics" in line:
                lines.append(line)
        f_new.writelines(lines)
        f.close()
        f_new.close()
    except:
        print("Error in filtering")
 
filterAthletics()