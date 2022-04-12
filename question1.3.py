"""
Accept 2 strings and check if they are anagrams

@author: Krishaay Jois
@notauthor: Suketu Patni (@SuketuPatni)
"""

if sorted(input("Enter First String: ")) == sorted(input("Enter Second String: ")): 
    print("ANAGRAM") 
else: 
    print("NON ANAGRAM")