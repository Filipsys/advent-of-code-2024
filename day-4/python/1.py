input_data = """XXXXXX
XSAMXX
XAXXAX
XMASXS
XXXXXX"""
converted_data = []

# Convert the data into a list of data
for line in input_data.split("\n"):
  converted_line = []

  for letter in line:
    converted_line.append(letter)
  converted_data.append(converted_line)

for line_index, line in enumerate(converted_data):
  possible_checks = ["north", "north-east", "east", "south-east", 
                     "south", "south-west", "west", "north-west"]

  # Check top and bottom lines
  if line_index == 0:
    possible_checks.remove("north")
  elif line_index == len(line) - 1:
    possible_checks.remove("south")

  for letter_index, letter in enumerate(line):
    possible_checks = ["north", "north-east", "east", "south-east", 
                     "south", "south-west", "west", "north-west"]

    if letter_index == 0:
      possible_checks.remove("west")

      if line_index == 0:
        possible_checks.remove("north-west")
        possible_checks.remove("south-west")
    if letter_index == len(line) - 1:
      possible_checks.remove("east")

      if line_index == len(converted_data) - 1:
        possible_checks.remove("south-west")
        possible_checks.remove("south-east")
    
    print(line_index, possible_checks)
