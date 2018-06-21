import re
pattern = re.compile(r"[\s\.;,]")
s = "a.. ,, .. ;;ab ..a"
result_list = pattern.split(s)
print(result_list)
pattern = re.compile(r"[\s\.;,]+")
result_list = pattern.split(s)
print(result_list)
%hist -f re_split.py
