"""
Accept 2 strings and check if they are anagrams.

"""
s1 = input()
s2 = input()

if sorted(s1) == sorted(s2):
    print("anagrams")
else:
    print("not anagrams")