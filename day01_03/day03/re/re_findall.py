import re
pattern = re.compile(r"\d+")
s = "abcd1234bcda4321"

result_list = pattern.findall(s)
print(result_list)
pattern = re.compile(r"\d+\.\d+")
s = "3.14helloworld 2018 3.  ..5"
result_list = pattern.findall(s)
print(result_list)

