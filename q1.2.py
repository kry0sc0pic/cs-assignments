"""
Accept a string and check if it contains all unique
characters. Display the string and the message "unique"
or "not unique".

"""
s = input()
for i in s:
    if s.count(i) > 1:
        print("not unique")
        break
else:
    print("unique")
