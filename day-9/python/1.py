data = open("../day-9.input", "r").read()

converted_data = ""
char_id = 0
for index, char in enumerate(data):
  if index % 2 == 1:
    converted_data += ".," * int(char)
    continue
  
  converted_data += (str(char_id) + ",") * int(char)
  char_id += 1

# Remove ending comma if exists
if converted_data[-1] == ",":
  converted_data = converted_data[:-1]

converted_data_length = len(converted_data)

# Remove the dots at the end if any
while converted_data[-2:] == ",.":
  converted_data = converted_data[:-2]
while converted_data[-1] == ".":
  converted_data = converted_data[:-1]

data_as_list = converted_data.split(",")

are_empty_spaces = True
while are_empty_spaces:
  try:
    check = data_as_list.index(".")
    
    data_as_list.pop(check)
    last_element = data_as_list[-1]
    data_as_list.pop(-1)
    data_as_list.insert(check, last_element)
  except ValueError:
    are_empty_spaces = False
    continue

converted_space = ",".join(data_as_list)

# Remove first unnecessary comma if exists
if converted_space[1:] == ",":
  converted_space = converted_space[1:]

checksum = 0
for index, char in enumerate(converted_space.split(",")):
  checksum += index * int(char)

print(checksum)