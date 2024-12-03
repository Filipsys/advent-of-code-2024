import re


data = open("../day-3.input", "r").read().replace("\n", "")
regex_list = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", data)

result = 0
for regex in regex_list:
  left, right = regex[4:][:-1].split(",")
  
  result += int(left) * int(right)

print(result)