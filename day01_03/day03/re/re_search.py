import re
pattern = re.compile("\d+")
s = "abcd1234bcda4321"
m = pattern.search(s)
print(m)
m.group()
re.compile("([a-z]+)\s([a-z]+)", re.I) # 表示忽略字符串字母大小写
pattern = re.compile("([a-z]+)\s([a-z]+)", re.I) # 表示忽略字符串字母大小写
s= "Hello world, byebye World"
m = pattern.search(s)
print(m.group())
%hist -f re_search.py
