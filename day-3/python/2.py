import re


data = open("./task1.input", "r").read().replace("\n", "")

regex_list = re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))", data)
print(regex_list)

temp = []
for value in regex_list:
  for tuple_value in value:
    if tuple_value != "":
      temp.append(tuple_value)
print(temp)

result = 0
for regex in regex_list:
  left, right = regex[4:][:-1].split(",")
  
  result += int(left) * int(right)

print(result)