data = open("../day-6.input", "r").read()
data = data.split("\n")
row_length = len(data[0])
column_length = len(data)

guard_location = (0, 0) # x & y
guard_direction = "N"
guard_locations_visited = []

movement_dict = {
  "N": (0, -1),
  "E": (1, 0),
  "S": (0, 1),
  "W": (-1, 0)
}
direction_cursor_dict = {
  "N": "^",
  "E": ">",
  "S": "V",
  "W": "<"
}

# Format data to be an array of arrays
temp_list_data = []
for element in data:
  temp_list = []
  for char in element:
    temp_list.append(char)
  
  temp_list_data.append(temp_list)
data = temp_list_data

def updateMap():
  global data, guard_location
  
  data[guard_location[1]][guard_location[0]] = "."
  data[guard_location[1] + movement_dict[guard_direction][1]][guard_location[0] + movement_dict[guard_direction][0]] = direction_cursor_dict[guard_direction]
  guard_location = (guard_location[0] + movement_dict[guard_direction][0], guard_location[1] + movement_dict[guard_direction][1])
  
  if guard_location not in guard_locations_visited:
    guard_locations_visited.append(guard_location)

def rotate_direction():
  global data, guard_direction
  
  if guard_direction == "N":
   guard_direction = "E"
  elif guard_direction == "E":
   guard_direction = "S"
  elif guard_direction == "S":
   guard_direction = "W"
  elif guard_direction == "W":
   guard_direction = "N"
  
  x, y = guard_location
  data[y][x] = direction_cursor_dict[guard_direction]

def check_guard_direction(data_char):
  if data_char == "^":
    return "N"
  elif data_char == ">":
    return "E"
  elif data_char == "V":
    return "S"
  elif data_char == "<":
    return "W"
  else:
    return ValueError

def displayMap():
  temp_string = ""
  
  for i in data:
    for j in i:
      temp_string += j
    temp_string += "\n"
  print(temp_string)

def check_if_guard_path_blocked(x, y):
  new_y = y + movement_dict[guard_direction][1]
  new_x = x + movement_dict[guard_direction][0]

  if new_y < 0 or new_y >= column_length or new_x < 0 or new_x >= row_length:
    print("Blocked: Out of bounds")
  elif data[new_y][x] == "#" or data[y][new_x] == "#":
    print("Blocked: Wall")
    rotate_direction()

def move_forward():
  check_if_guard_path_blocked(guard_location[0], guard_location[1])
  
  if (guard_location[0] + movement_dict[guard_direction][0] < 0 or 
      guard_location[0] + movement_dict[guard_direction][0] > row_length):
    raise IndexError
  
  if (guard_location[1] + movement_dict[guard_direction][1] < 0 or
      guard_location[1] + movement_dict[guard_direction][1] > column_length):
    raise IndexError
  
  # displayMap()
  updateMap()
  
# Find the guard initial location
for data_line_index, data_line in enumerate(data):
  for data_char_index, data_char in enumerate(data_line):
    if data_char == "^":
      guard_location = (data_char_index, data_line_index)
      guard_direction = check_guard_direction(data_char)
      
      check_if_guard_path_blocked(guard_location[0], guard_location[1])

running = True
while running:
  try:
    move_forward()
    print("Guard location: ", guard_location)
  except IndexError:
    running = False
    print("Out of bounds")
    print("Guard direction: ", guard_direction)
    print("Guard location: ", guard_location)

print("Sum of unique places visited: ", len(guard_locations_visited) + 1) # Counting the exit spot