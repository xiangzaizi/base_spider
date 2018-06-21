import re
pattern = re.compile(r"\d+")
s = "abcd1234bcda4321"
m = pattern.match(s)
print(m)
m = pattern.match(s, 3)
print(m)
m = pattern.match(s, 4)
print(m)
m.group()%hist -f re_match.py
