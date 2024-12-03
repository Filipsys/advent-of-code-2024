import re

data = open("../day-3.input", "r").read().replace("\n", "")
regex_list = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))", data)

result = 0
is_saving = True
for regex in regex_list:
  if regex[1] == "do()":
    is_saving = True
  elif regex[2] == "don't()":
    is_saving = False

  if not is_saving or regex[0] == "":
    continue

  left, right = regex[0][4:][:-1].split(",")
  result += int(left) * int(right)

print(result)