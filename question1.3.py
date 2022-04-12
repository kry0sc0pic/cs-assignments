"""
Accept 2 strings and check if they are anagrams
"""

string1 = input("Enter First String: ")
string2 = input("Enter Second String: ")
l1 = list(string1)
l2 = list(string2)
l1.sort()
l2.sort()
if(l1 == l2):
    print("ANAGRAM")
else:
    print("NON ANAGRAM")