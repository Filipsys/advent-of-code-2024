input_data = """XXXXXX
XSAMXX
XAXXAX
XMASXS
XXXXXX"""
converted_data = []

for line in input_data.split("\n"):
  converted_line = []

  for letter in line:
    converted_line.append(letter)
  converted_data.append(converted_line)

print(converted_data)

for line_index, line in enumerate(converted_data):
  possible_checks = ["north", "north-east", "east", "south-east", 
                     "south", "south-west", "west", "north-west"]

  if line_index == 0:
    possible_checks.remove("north-west")
    possible_checks.remove("north")
    possible_checks.remove("north-east")
  elif line_index == len(line) - 1:
    possible_checks.remove("south-west")
    possible_checks.remove("south")
    possible_checks.remove("south-east")

  print(possible_checks)

  for letter_index, letter in enumerate(line):
    # Try to check if there are letters around the checked letter

    if letter_index == 0:
      print("First letter of line")
    elif letter_index == len(line) - 1:
      print("Last letter of line")
